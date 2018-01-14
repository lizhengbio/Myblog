#coding:utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class article_list(models.Model):
    title = models.CharField(max_length=32,verbose_name="文字标题")
    date = models.DateTimeField(verbose_name="发表日期")
    tag = models.CharField(max_length=32,verbose_name="标签")
    short_content = RichTextUploadingField(verbose_name="摘要")
    content = RichTextUploadingField(verbose_name="文章内容")
    src = models.CharField(max_length=64)
    delete_flag = models.CharField(max_length=4)
    views = models.PositiveIntegerField(default=0)
    like = models.PositiveIntegerField(default=0)
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
    def increase_like(self):
        self.like += 1
        self.save(update_fields=['like'])

