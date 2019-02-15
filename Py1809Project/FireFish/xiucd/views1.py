from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#  构建反馈方法
def addone(request):
    print("+++")
    return HttpResponse("<p>添加名单</p><p><h1>张三</h1><h1>王武</h1><h1>疯子</h1></p>\n"
                        "我讨厌你的飞鱼服，还有那把绣春刀")