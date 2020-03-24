#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2020/3/24
# @Author  : 圈圈烃
# @File    : translateBodyData
# @Description:
#
#
from bs4 import BeautifulSoup
import json
import requests
import random
import hashlib
import time


def translateBody():
    """解析页面数据"""
    bodyData = {"name": "e-human-adult-male-body_cn"}
    bodyData["groups"] = []
    with open("../templates/MaleBodyApp/male.html", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    svg = soup.find('svg')
    # 未分组
    ngpaths = svg.find_all("path", recursive=False)
    for path in ngpaths:
        group = {"elements": []}
        ele = {}
        ele["type"] = "path"
        try:
            ele["d"] = path["d"]
        except:
            ele["d"] = ""
        ele["id"] = path["id"]
        ele["fill"] = path["fill"]
        ele["style"] = path["style"]
        ele["stroke"] = path["stroke"]
        group["resource"] = "useless"
        try:
            ele["datagroup"] = path["data-group"]
        except:
            ele["datagroup"] = ""
        try:
            ele["strokewidth"] = path["stroke-width"]
        except:
            ele["strokewidth"] = ""
        group["elements"].append(ele)
        bodyData["groups"].append(group)
    # 有分组
    gs = svg.find_all('g')
    datagroupDict = {}
    for g in gs:
        group = {"elements": []}
        try:
            group["data-group"] = g["data-group"]
        except:
            group["data-group"] = ""
        try:
            group["resource"] = g["resource"]
        except:
            group["resource"] = ""
        paths = g.find_all()
        for path in paths:
            ele = {}
            if path.name == "g":
                pass
            else:
                if path.name == "path":
                    ele["type"] = "path"
                    try:
                        ele["d"] = path["d"]
                    except:
                        ele["d"] = ""
                elif path.name == "circle":
                    ele["type"] = "circle"
                    ele["cx"] = path["cx"]
                    ele["cy"] = path["cy"]
                    ele["r"] = path["r"]
                elif path.name == "ellipse":
                    ele["type"] = "ellipse"
                    ele["cx"] = path["cx"]
                    ele["cy"] = path["cy"]
                    ele["rx"] = path["rx"]
                    ele["ry"] = path["ry"]
                else:
                    pass
                # 公共属性
                ele["id"] = path["id"]
                ele["fill"] = path["fill"]
                ele["style"] = path["style"]
                ele["stroke"] = path["stroke"]
                # 翻译
                if datagroupDict.get(path["data-group"]):
                    ele["datagroup_cn"] = datagroupDict[path["data-group"]]
                else:
                    _, ele["datagroup_cn"] = translate_en2ch(path["data-group"])
                    datagroupDict[path["data-group"]] = ele["datagroup_cn"]
                    time.sleep(1)
                try:
                    ele["datagroup"] = path["data-group"]
                except:
                    ele["datagroup"] = ""
                try:
                    ele["strokewidth"] = path["stroke-width"]
                except:
                    ele["strokewidth"] = ""
            group["elements"].append(ele)
        bodyData["groups"].append(group)
    # print(svg)
    # print(bodyData)
    with open("../static/MaleBodyApp/assets/illustrations/" + bodyData["name"] + ".json", 'w', encoding="utf-8") as fw:
        json.dump(bodyData, fw, ensure_ascii="utf-8")


def translate_en2ch(txt_data):
    """
    翻译英文字幕稿为中文
    :param txt_data:
    :return:
    """
    appid = "20181026000225882"
    secretKey = "oQlAk9oQKPd5Bu2VIMjC"
    salt = random.randint(32768, 65536)
    sign = appid + txt_data + str(salt) + secretKey
    m1 = hashlib.md5(sign.encode("utf-8"))
    sign_md5 = m1.hexdigest()
    translate_url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
    data = {
        "from": "en",
        "to": "zh",
        "q": txt_data,
        "appid": appid,
        "salt": salt,
        "sign": sign_md5,
    }
    res = requests.post(translate_url, data=data)
    ch_dict = res.json()
    print(ch_dict)
    en_txt = ch_dict['trans_result'][0]['src']
    ch_txt = ch_dict['trans_result'][0]['dst']

    return en_txt, ch_txt


if __name__ == '__main__':
    translateBody()
    # _, ch_txt = translate_en2ch("brain")
