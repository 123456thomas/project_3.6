from django.conf.urls import url,include
from django.contrib import admin
# 导入视图
from . import views

urlpatterns = [
    url(r'^$', views.index0),
    url(r'^create/$', views.Create_author),
    url(r'^findall/$', views.findall),
    url(r'^find/$', views.find),
    url(r'^delete/$', views.delete),
    url(r'^update/$', views.update),
    url(r'^(\w+)/param/$', views.param),
    url(r'^(\d+)/param2/$', views.param2),
    url(r'^(?P<username>\w+)/params/$', views.params),
    url(r'^req/$', views.reqmeth),
    url(r'^index1/$', views.index1),
    url(r'^index2/$', views.index2),
    url(r'^index/$', views.index),
    url(r'^login/$', views.login,name="login"),
    url(r'^register/$', views.register,name="register"),
    url(r'^Hans/$', views.logsend,name="Hans"),
    url(r'^success/$', views.registsend,name="success"),
    url(r'^Hans1/$', views.logsuccess,name="Hans1"),
    url(r'^read/$', views.read,name="read"),
    url(r'^writer/$', views.writing,name="writer"),
    ]