from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#  构建反馈方法
def findall(request):
    print("+++")
    return HttpResponse("<p>查询名单</p><p><h1>张三</h1><h1>王武</h1><h1>疯子</h1></p>")