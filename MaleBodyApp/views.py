from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
import json

# Create your views here.

maleSourcePath = "MaleBodyApp/static/MaleBodyApp/assets/illustrations/e-human-adult-male-body_cn_2.json"
femaleSourcePath = "MaleBodyApp/static/MaleBodyApp/assets/illustrations/e-human-adult-female-body_cn_2.json"


def showMale(request):
    """男性"""
    if request.method == 'GET':
        jData = readJsonFile(maleSourcePath)
    return render(request, 'MaleBodyApp/body.html', jData)


def showFemale(request):
    """女性"""
    if request.method == 'GET':
        jData = readJsonFile(femaleSourcePath)
    return render(request, 'MaleBodyApp/body.html', jData)


def getData(request):
    """返回json"""
    if request.method == 'GET':
        bodyType = request.GET.get("type")
        if bodyType == "male":
            jData = readJsonFile(maleSourcePath)
        elif bodyType == "female":
            jData = readJsonFile(femaleSourcePath)
        else:
            jData = {"msg": "parameter error"}
        return JsonResponse(jData)


def readJsonFile(path):
    """读取解析json"""
    bodyPartsDict = {}
    with open(path, "r") as f:
        jData = json.load(f)
    for g in jData["groups"]:
        for el in g["elements"]:
            try:
                bodyPartsDict[el["datagroup"]] = (el["datagroup_cn"])
            except Exception as e:
                pass
    jData["bodyParts"] = bodyPartsDict
    return jData
