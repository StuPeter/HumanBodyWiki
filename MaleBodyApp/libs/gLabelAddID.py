#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2020/3/25
# @Author  : 圈圈烃
# @File    : gLabelAddID
# @Description:
#
#
import json
from collections import Counter


def addId():
    with open("../static/MaleBodyApp/assets/illustrations/e-human-adult-female-body_cn_1.json", 'r',
              encoding="utf-8") as fr:
        bodyData = json.load(fr)
    for g in bodyData['groups']:
        nameList = []
        for ele in g['elements']:
            try:
                nameList.append(ele['datagroup'])
            except:
                pass
        c = Counter(nameList)
        c_dict = dict(c)
        # print(list(c_dict.keys())[0])
        g['gid'] = list(c_dict.keys())[0]
        print(g)
    with open("../static/MaleBodyApp/assets/illustrations/e-human-adult-female-body_cn_2.json", 'w', encoding="utf-8") as fw:
        json.dump(bodyData, fw, ensure_ascii="utf-8")


if __name__ == '__main__':
    addId()
