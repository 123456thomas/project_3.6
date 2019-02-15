from django.shortcuts import render
from django.http import HttpResponse
from . import models
from user.models import Users
# Create your views here.


# 第一种方案
def create(request):
    # 第一种方法
    # user = models.Users.create_user("zhangsan",18)
    # 第二种方法
    # user = models.Users(name='yyqx',age=18)
    # 第三种方法
    user = models.Users.usermanage.create_user(name='wjk',age=18)
    user.save()
    return HttpResponse('<h1 align="center">增加成功</h1>')

# 删除数据
def delete(request):

    user = models.Users(id=5)
    user.delete()
    return HttpResponse('<h1 align="center">删除成功</h1>')

# 修改数据
def update(request):
    user = models.Users(id=7)
    user.name='wy'
    user.save()
    return HttpResponse('<h1 align="center">修改成功</h1>')

# 查找数据
def index(request):

    # 查询id为3的数据
    # user =Users.usermanage.filter(id=3).values()

    # 查询所有数据
    user = Users.usermanage.values()
    return HttpResponse(user)

