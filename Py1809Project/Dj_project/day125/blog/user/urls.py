from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index/$',views.index),
    url(r'^create/$', views.create),
    url(r'^delete/$', views.delete),
    url(r'^update/$', views.update),
]