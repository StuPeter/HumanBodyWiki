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


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    # path('api/v1/get/', views.split_home_get_api),
    # path('api/v1/post/', views.split_home_post_api),
]

