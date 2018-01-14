#coding:utf-8
"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from views import *

#指出所有的二级路由
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^article/',include('Article.urls')),
    url(r'^comment/',include('comment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#展示主url直接指出的路由
urlpatterns += [
    url(r'^$',index),
    url(r'^index/',index),
    url(r'^about/',about),
    url(r'^tags/',tag),
    url(r'^archives/',archives),
    url(r'^search/$',search),
]