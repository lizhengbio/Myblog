#coding:utf-8
from django.shortcuts import render_to_response
from models import *
from comment.forms import BlogCommentForm
from django.shortcuts import get_object_or_404,render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def article_details(request,src):
    paper = get_object_or_404(article_list,src=src)
    #阅读量 +1
    paper.increase_views()
    tags = []
    papers = article_list.objects.filter(delete_flag="N").order_by("-date")
    for p in papers:
        if p.tag not in tags:
            tags.append(p.tag)
    form = BlogCommentForm()
    #获取这篇post下的全部评论
    comment_list = paper.blogcomment_set.all()
    return render(request,"article.html",locals())


def like(request,src):
    result = {"statue":"error","data":""}
    if request.method == "POST":
        paper = get_object_or_404(article_list,src=src)
        #点赞数+1
        paper.increase_like()
        result["statue"] = "success"
        result["data"] = str(paper.like)
    return JsonResponse(result)