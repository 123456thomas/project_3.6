from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#  构建反馈方法
def delone(request):
    print("+++")
    return HttpResponse("<p>删除名单</p><p><h1>张三</h1><h1>王武</h1><h1>疯子</h1></p>\n"
                        "若不是因为我，你也不会是今天这个样子")