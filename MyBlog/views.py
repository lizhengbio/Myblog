#coding:utf-8

from django.shortcuts import render_to_response,render
from Article.models import *
import random
from django.core.paginator import Paginator
from django.db.models import Q

def obtain_data(func):
    def obtain_tag(request,*args,**kwargs):
        tags = []
        papers = article_list.objects.filter(delete_flag="N").order_by("-date")
        for p in papers:
            if p.tag not in tags:
                tags.append(p.tag)
        return func(request,tags,papers)
    return obtain_tag

@obtain_data
def index(request,tags,papers):
    if request.method == "GET":
        page = request.GET.get("page",1)
        get_page = Paginator(papers,5) #指出要分页的对象和每页的条数
        article_data = get_page.page(int(page)) #获取第几页的内容
    return render_to_response("index.html",locals())

@obtain_data
def about(request,tags,papers):
    return render_to_response("about.html",locals())

@obtain_data
def tag(request,tags,papers):
    tag_col = {}
    color = ["#9F79EE","#00BFFF","#7B68EE","#BEBEBE","#B22222","#1C1C1C"]
    for t in tags:
        random_color = random.choice(color)
        tag_col.update({t:random_color})

    return render_to_response("tags.html",locals())

@obtain_data
def archives(request,tags,papers):
    return render_to_response("archives.html",locals())

@obtain_data
def search(request,tags,papers):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "请输入关键词"
        return render(request,'index.html',{'error_msg':error_msg,"tags":tags})

    article_data = article_list.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
    return render(request,'index.html',locals())
