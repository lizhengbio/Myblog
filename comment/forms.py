#coding:utf-8
from django import forms
from models import BlogComment
from Article.models import article_list

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['user_name','user_email','body']
        widgets = {
            # 为各个需要渲染的字段指定渲染成什么html组件，主要是为了添加css样式。
            # 例如 user_name 渲染后的html组件如下：
            # <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon1">

            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入昵称",
                'aria-describedby': "sizing-addon1",
            }),
            'user_email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "请输入邮箱",
                'aria-describedby': "sizing-addon1",
            }),
            'body': forms.Textarea(attrs={
                'placeholder': '我来评两句~',
                'style': "width:100%;height:100px",
            }),
        }

