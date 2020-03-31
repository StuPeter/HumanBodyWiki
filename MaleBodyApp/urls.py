#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2020/3/12
# @Author  : 圈圈烃
# @File    : urls
# @Description:
#
#
from django.urls import path, re_path
from django.views.generic.base import TemplateView
from . import views

app_name = "MaleBodyApp"
urlpatterns = [
    path('male', views.showMale, name="Male"),
    path('female', views.showFemale, name="Female"),
    path('api/v1/', views.getData),
]

