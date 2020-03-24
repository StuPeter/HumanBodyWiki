from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
import json


# Create your views here.

def getData(request):
    """解析json"""
    with open("MaleBodyApp/static/MaleBodyApp/assets/illustrations/human-adult-male-body.json") as f:
        jData = json.load(f)
    for els in jData['groups']:
        for index, el in enumerate(els['elements']):
            try:
                els['elements'][index] = jData['elements'][el]
            except:
                pass
            print(index)
            print(el)
    return render(request, 'MaleBodyApp/test1.html', jData)
    # return JsonResponse(jData)


def getData2(request):
    """解析json"""
    with open("MaleBodyApp/static/MaleBodyApp/assets/illustrations/e-human-adult-male-body_cn.json") as f:
        jData = json.load(f)
    bodyPartsDict = {}
    for g in jData["groups"]:
        for el in g["elements"]:
            try:
                bodyPartsDict[el["datagroup"]] = (el["datagroup_cn"])
            except Exception as e:
                print(e)
    jData["bodyParts"] = bodyPartsDict
    return render(request, 'MaleBodyApp/test2.html', jData)
    # return JsonResponse(jData)


def getData2_1(request):
    """解析json"""
    with open("MaleBodyApp/static/MaleBodyApp/assets/illustrations/e-human-adult-female-body_cn.json") as f:
        jData = json.load(f)
    bodyPartsDict = {}
    for g in jData["groups"]:
        for el in g["elements"]:
            try:
                bodyPartsDict[el["datagroup"]] = (el["datagroup_cn"])
            except Exception as e:
                print(e)
    jData["bodyParts"] = bodyPartsDict
    # return render(request, 'MaleBodyApp/test2.html', jData)
    return JsonResponse(jData)
