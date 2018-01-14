#coding:utf-8

from django.conf.urls import url
from views import *
urlpatterns = [
        url(r'^(\w+)/$',article_details),
        url(r'^like/(\w+)/$',like),
        ]
