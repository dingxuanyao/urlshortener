from django.urls import path
from .views import post_url, redirect_url
from django.conf.urls import url

urlpatterns = [
    url(r'^submit/$', post_url),
    url(r'^.*', redirect_url),
]