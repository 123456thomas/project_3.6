"""
__environment：python 3.6;
__author__ = 'Thompson'
__mtime__ = '2019/2/15'

<span class="YKRG">190</span>
<div style="display:none">.</div>
95
<span class="UTYG">.</span>
<span class="HUTE">204</span>
<span class="HUTE">.</span>
<span style="display:inline">113</span>

"""
# import requests, time
# from lxml import etree

import re
import lxml.html
import requests
from fake_useragent import UserAgent

encoderchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="


# 重写js生成session的算法
def f1(a):
    i, len_str = 0, 0
    c, c2, c3 = 0, 0, 0
    len_str = len(a)
    i = 0
    b = ""
    while i < len_str:
        c = ord(a[i]) & 0xff
        i += 1
        if i == len_str:
            b += encoderchars[c >> 2]
            b += encoderchars[(c & 0x3) << 4]
            b += "=="
            break
        c2 = ord(a[i])
        i += 1
        if i == len_str:
            b += encoderchars[c >> 2]
            b += encoderchars[(((c & 0x3) << 4) | ((c2 & 0xf0) >> 4))]
            b += encoderchars[((c2 & 0xf) << 2)]
            b += "="
            break
        c3 = ord(a[i])
        b += encoderchars[c >> 2]
        b += encoderchars[(((c & 0x3) << 4) | ((c2 & 0xf0) >> 4))]
        b += encoderchars[(((c2 & 0xf) << 2) | ((c3 & 0xc0) >> 6))]
        b += encoderchars[c3 & 0x3f]
        i += 1
    return b

s = requests.session()
result = s.get('http://datamining.comratings.com/exam')
session_id = result.cookies.get_dict()['session']
# 调用算法生成session
r_cookies = 'session={};c1={}; c2={}; path=/'.format(session_id, f1(session_id[1:4]), f1(session_id))
headers = {"User-Agent": UserAgent().random, "Cookie": r_cookies}
ss = s.get('http://datamining.comratings.com/exam3', headers=headers).text
print(ss)
pattern = re.compile(r'<body>(.*?)<body>', re.DOTALL)  # 用正则切出body内容
result = pattern.findall(ss)
result1 = result[0].split('<br>')  # 根据<br>切出来的十一个片段
print(result1[0])
sty = re.compile(r'<style>(.*?)</style>', re.DOTALL)
sty1 = sty.findall(ss)  # style里面的内容
print(sty1)
sty2 = re.compile(r'.(.*?){')
sty22 = sty2.findall(sty1[0])  # style里面定义的四个属性组成的集合
print(sty22)
data = []  # 空数组，存放十个IP
data.append(result1[0])
print(data)
for data_res in result1[1:]:  # 遍历按照换行切开的十段字符串
    line_array = data_res.split('\n')  # 每一行组成的数组
    ip_data = []  # 组成IP的四个数字存放的数组
    ip_str = ''
    for line_str in line_array:  # 遍历每一行
        ip_regex = re.compile(r'\d+')
        if sty22[0] not in line_str and sty22[1] not in line_str and 'none' not in line_str:  # 利用正则切出符合条件的数字
            ip_array = ip_regex.findall(line_str)
            if ip_array != []:
                ip_data.append(ip_array[0])
        # 把筛选出来的的四个数字组合成IP
    # print(ip_data)
    ip_str = ip_data[0] + '.' + ip_data[1] + '.' + ip_data[2] + '.' + ip_data[3]
    # 把每一个IP存到数组里
    data.append(ip_str)
    # print(data)
    for i in data:
        print(i)
