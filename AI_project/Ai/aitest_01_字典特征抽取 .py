"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/6/25'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from sklearn.feature_extraction import DictVectorizer
from fake_useragent import UserAgent
# 如果结果不用toarray，请开启sparse=False
dv = DictVectorizer()
instances = [{'city': '北京','temperature':100},{'city': '上海','temperature':60}, {'city': '深圳','temperature':30}]
data = dv.fit_transform(instances).toarray()
print(data)
print(dv.get_feature_names())
print(dv.inverse_transform(data))

ua = UserAgent()
print(ua.random)

