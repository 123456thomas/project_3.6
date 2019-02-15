from django.conf.urls import url
from django.contrib import admin
# 导入视图
from . import views,views1,views2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^findall/$', views.findall),
    url(r'^addone/$', views1.addone),
    url(r'^delone/$', views2.delone)
]