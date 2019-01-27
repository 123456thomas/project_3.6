"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/25'
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

"""这里mpl_finance是原来的matplotlib.finance，但是现在独立出来了
（而且好像没什么人维护更新了），我们将会使用它提供的方法来绘制K线图
；tushare是用来在线获取股票数据的库；
matplotlib.ticker中有个FuncFormatter()方法可以帮助我们调整坐标轴；
matplotlib.pylab.date2num可以帮助我们将日期数据进行必要的转化"""

# 模块导入
import tushare as ts

import seaborn as sns

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

import mpl_finance

from matplotlib import ticker

from matplotlib.pylab import date2num

"""ts.set_token('your token here')
以上方法只需要在第一次或者token失效后调用，完成调取tushare数据凭证的设置，正常情况下不需要重复设置。也可以忽略此步骤，直接用pro_api('your token')完成初始化

初始化pro接口

pro = ts.pro_api()
如果上一步骤ts.set_token('your token')无效或不想保存token到本地，也可以在初始化接口里直接设置token:

pro = ts.pro_api('your token')"""

sns.set()
# ts.set_token('5d9dbd8feda953676c849289d7edd09e70743d8eba672e9b5b1e49f6')
pro = ts.pro_api('5d9dbd8feda953676c849289d7edd09e70743d8eba672e9b5b1e49f6')

# 1.代码实现
df = pro.index_daily(ts_code='000001.SZ', start_date='20180901')
df = df.sort_values(by='trade_date', ascending=True)
df['trade_date2'] = df['trade_date'].copy()
df['trade_date'] = pd.to_datetime(df['trade_date']).map(date2num)
df['dates'] = np.arange(0, len(df))
df.head()

# 2.绘制k线图

fig, ax = plt.subplots(figsize=(10, 5))
mpl_finance.candlestick_ochl(
    ax=ax,
    quotes=df[['trade_date', 'open', 'close', 'high', 'low']].values,
    width=0.7,
    colorup='r',
    colordown='g',
    alpha=0.7)
ax.xaxis_date()
plt.xticks(rotation=30)


# 3.解决空白问题
def format_date(x, pos):
    if x < 0 or x > len(date_tickers) - 1:
        return ''
    return date_tickers[int(x)]

date_tickers = df.trade_date2.values
fig, ax = plt.subplots(figsize=(10, 5))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
mpl_finance.candlestick_ochl(
    ax=ax,
    quotes=df[['dates', 'open', 'close', 'high', 'low']].values,
    width=0.7,
    colorup='r',
    colordown='g',
    alpha=0.7)
ax.set_title('上证综指K线图(2018.9-)', fontsize=20);
