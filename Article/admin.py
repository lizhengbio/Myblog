#coding:utf-8
from django.contrib import admin
from models import *

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title","date"]

admin.site.register(article_list,NewsAdmin)
