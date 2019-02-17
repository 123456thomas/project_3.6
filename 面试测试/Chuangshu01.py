import requests
import execjs
from bs4 import BeautifulSoup
import re

# 待执行的js函数
js_str = '''
function getCookie(a,b) {
    var c = b.split("; ");
    for (var i = 0; i < c.length; i++) {
        var d = c[i].split("=");
        if (a == d[0]) {
            return d[1]
        }
    }
    return ""
}

function f1(a) {
    var b, i, len;
    var c, c2, c3;
    len = a.length;
    i = 0;
    b = "";
    var encoderchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="; 
    while (i < len) {
        c = a.charCodeAt(i++) & 0xff;
        if (i == len) {
            b += encoderchars.charAt(c >> 2);
            b += encoderchars.charAt((c & 0x3) << 4);
            b += "==";
            break
        }
        c2 = a.charCodeAt(i++);
        if (i == len) {
            b += encoderchars.charAt(c >> 2);
            b += encoderchars.charAt(((c & 0x3) << 4) | ((c2 & 0xf0) >> 4));
            b += encoderchars.charAt((c2 & 0xf) << 2);
            b += "=";
            break
        }
        c3 = a.charCodeAt(i++);
        b += encoderchars.charAt(c >> 2);
        b += encoderchars.charAt(((c & 0x3) << 4) | ((c2 & 0xf0) >> 4));
        b += encoderchars.charAt(((c2 & 0xf) << 2) | ((c3 & 0xc0) >> 6));
        b += encoderchars.charAt(c3 & 0x3f)
    }
    return b
}

function reload(session) {


    var a = "";
    var b = "";
    //a = "c1=" + f1(session.substr(1, 3)) + "; path=/";    
    //b = "c2=" + f1(session) + "; path=/";
    a = f1(session.substr(1, 3));    
    b = f1(session);
    return a + ";" + b
}
'''

url = 'http://datamining.comratings.com/exam'
def web_get(url):
    # 创建一个session会话
    sess = requests.session()
    sess.get(url)
    cookies = sess.cookies["session"]
    # print(cookies)
    ctx = execjs.compile(js_str)
    # 执行js代码
    result = ctx.call("reload", cookies)
    # print(result)
    # 获取新cookie
    ls = result.split(";")
    dict = {"session": cookies, 'c1': ls[0], 'c2': ls[1]}
    sess.cookies = requests.utils.cookiejar_from_dict(dict)
    # print(sess.cookies)
    response = sess.get(url)
    txt = response.text
    # print('txt:',txt)
    soup = BeautifulSoup(txt, 'lxml')
    while len(soup.select('iframe')) > 0:
        # 获取新链接地址
        src = 'http://datamining.comratings.com' + soup.select('iframe')[0]['src']
        # print('src:', src)
        response = sess.get(src)
        txt = response.text
        soup = BeautifulSoup(txt, 'lxml')
    return txt

# print('txt:', txt)

def parse_data(ss):
    pattern = re.compile(r'<body>(.*?)<body>', re.DOTALL)  # 用正则切出body内容
    result = pattern.findall(ss)
    result1 = result[0].split('<br>')  # 根据<br>切出来的十一个片段
    print(result1)
    sty = re.compile(r'<style>(.*?)</style>', re.DOTALL)
    sty1 = sty.findall(ss)  # style里面的内容
    # print(sty1)
    sty2 = re.compile(r'.(.*?){')
    sty22 = sty2.findall(sty1[0])  # style里面定义的四个属性组成的集合
    print(sty22)
    data = []  # 空数组，存放十个IP
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
        yield i

def main():
    text = web_get(url)
    ip_list=[]
    for i in parse_data(text):
        ip_list.append(i)
    print(ip_list)

if __name__ == '__main__':
    main()