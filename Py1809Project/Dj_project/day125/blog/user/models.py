from django.db import models



# 第三种方法，类管理器
class Usermanage(models.Manager):
    def create_user(self,name,age):
        user = self.create(name=name,age=age)
        return user


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)

    # 第一种方案：类方法
    # @classmethod
    # def create_user(cls,name,age):
    #     user = cls(name=name,age=age)
    #     return user
    def __str__(self):
        return self.name
    # 第三种方法时，不能忘记这里要写上这句话，是和Users连接关系
    usermanage = Usermanage()

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    # 一对多的时候，ForeignKey要放在多方
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

#第二种方案，对象属性操作方式
# model.py 不需要任何的操作，只在 views.py 文件中构建对象，完成保存即可。