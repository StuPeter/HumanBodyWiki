#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2020/3/18
# @Author  : 圈圈烃
# @File    : parserBodyData
# @Description:
#
#
from bs4 import BeautifulSoup
import json


def parserBody():
    """解析页面数据"""
    bodyData = {"name": "e-human-adult-male-body"}
    bodyData["groups"] = []
    with open("../templates/MaleBodyApp/index.html", "r", encoding="utf-8") as f:
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


if __name__ == '__main__':
    parserBody()
