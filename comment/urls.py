from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^post/(\w+)/$',post_comment),
]