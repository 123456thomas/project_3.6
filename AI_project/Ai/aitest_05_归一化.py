"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/6/26'
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
from sklearn.preprocessing import MinMaxScaler
def mms():
    minmax = MinMaxScaler(feature_range=(2,4))
    #data = minmax.fit_transform([[90,2,10,46],[60,4,15,45],[75,3,13,46]])
    data = minmax.fit_transform([[90, 2, 10, 46],[60,4,15,45],[75,3,13,46]])
    print(data)

mms()


