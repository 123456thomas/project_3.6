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
from sklearn.feature_selection.variance_threshold import VarianceThreshold

import numpy as np
def variance():
    van = VarianceThreshold(threshold=0.0)
    data = van.fit_transform([[0,2,0,3],[0,1,4,3],[0,1,1,3]]);
    print(data)

variance()




