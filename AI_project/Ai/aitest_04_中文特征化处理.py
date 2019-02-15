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

import jieba
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def cutword():
    """
    分词后的字符串结果
    :return: c1,c2,c3
    """
    # 将内容进行分词
    content1 = jieba.cut('今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。')

    content2 = jieba.cut('我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。')

    content3 = jieba.cut('如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。')

    # 建立列表取出迭代器数据
    con1 = []
    con2 = []
    con3 = []

    for word in content1:
        con1.append(word)

    for word in content2:
        con2.append(word)

    for word in content3:
        con3.append(word)

    # 将列表转换成字符串
    c1 = ' '.join(con1)
    c2 = ' '.join(con2)
    c3 = ' '.join(con3)

    return c1, c2, c3



# 中文特征值化
def countvec():
    """
    文本特征抽取
    :return: None
    """
    # 调用分词分割中文文章
    c1, c2, c3 = cutword()

    print("分词结果：",c1, c2, c3)

    # 实例化
    cv = CountVectorizer()

    data = cv.fit_transform([c1, c2, c3])

    print(cv.get_feature_names())
    print(data.toarray())

    return None


# 中文特征值化tf-idf
def tfidfvec():
    """
    文本特征抽取
    :return: None
    """
    # 调用分词分割中文文章
    c1, c2, c3 = cutword()

    print("分词结果：",c1, c2, c3)

    # 实例化
    tf = TfidfVectorizer(stop_words=['一种', '不会'])

    data = tf.fit_transform([c1, c2, c3])

    print(tf.get_feature_names())
    print(data.toarray())

    return None

countvec()