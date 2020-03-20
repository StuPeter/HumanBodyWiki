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
    with open("MaleBodyApp/static/MaleBodyApp/assets/illustrations/e-human-adult-female-body.json") as f:
        jData = json.load(f)
    bodyParts = []
    for g in jData["groups"]:
        for el in g["elements"]:
            try:
                bodyParts.append(el["datagroup"])
            except:
                pass
    bodyParts.remove("")
    bodyParts = list(set(bodyParts))
    bodyParts.remove("")
    jData["bodyParts"] = bodyParts
    return render(request, 'MaleBodyApp/test2.html', jData)
    # return JsonResponse(jData)


def getData2_1(request):
    """解析json"""
    with open("MaleBodyApp/static/MaleBodyApp/assets/illustrations/e-human-adult-female-body.json") as f:
        jData = json.load(f)
    bodyParts = []
    for g in jData["groups"]:
        for el in g["elements"]:
            try:
                bodyParts.append(el["datagroup"])
            except:
                pass
    bodyParts = list(set(bodyParts))
    bodyParts.remove("")
    jData["bodyParts"] = bodyParts
    # return render(request, 'MaleBodyApp/test2.html', jData)
    return JsonResponse(jData)
