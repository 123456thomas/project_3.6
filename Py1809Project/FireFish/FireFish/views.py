from django.http import HttpResponse
from django.shortcuts import render


#  构建反馈方法
def index(request):
    print("+++")
    return HttpResponse("<h1>绣春刀</h1><p>心存侥幸，赌徒是也</p>")
