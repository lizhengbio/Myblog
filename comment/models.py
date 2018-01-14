#coding:utf-8
from django.db import models
from Article.models import article_list
# Create your models here.
class BlogComment(models.Model):
    user_name = models.CharField(max_length=50,verbose_name="评论者名字")
    user_email = models.EmailField(max_length=50,verbose_name="评论者邮箱")
    body = models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="评论发表时间")
    article = models.ForeignKey(article_list,verbose_name="评论所属文章",on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]