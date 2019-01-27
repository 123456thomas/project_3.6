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

"""
    1、什么是 cookie？什么是session？
            由于HTTP协议是无状态的协议，所以服务端需要记录用户的状态时，就需要用某种机制来识具体的用户.
        比如:购物车，当往购物车增加商品时，由于HTTP协议无状态，服务端并不知道是哪个用户操作的，所以服务端
        要为特定的用户创建了特定的Session，标识 并且 跟踪用户，这样才知道 谁的购物车里面有几本书
            Session是保存在服务端的，保存Session的方法很多，内存、数据库、文件都行。
        
            Cookie常用的地方比如，用户的自动登陆。是客户端保存用户信息的一种机制，用来记录用户的一些信息。
        服务器可以通过响应浏览器的set-cookie的标头，得到Cookie的信息。你夜可以给这个文件设置一个期限，
        这个期限不会因为浏览器的关闭而消失。
            第一次创建Session的时候，服务端会在HTTP协议中告诉客户端，需要在 Cookie 里面记录一个Session ID，
        以后每次请求把这个会话ID发送到服务器，我就知道你是谁了。
        
            Session是在服务端保存的一个数据结构，用来跟踪用户的状态，这个数据可以保存在集群、数据库、文件中；
            Cookie是客户端保存用户信息的一种机制，用来记录用户的一些信息，也是实现Session的一种方式
    
    2、get 方法和 post 方法的区别？
         (1) 在客户端， Get 方式在通过 URL 提交数据，数据 在URL中可以看到；POST方式，数据放置在HTML HEADER内提交。
        
        （2） GET方式提交的数据最多只能有1024字节，而POST则没有此限制。
        
        （3） 安全性问题。正如在（ 1 ）中提到，使用  Get  的时候，参数会显示在地址栏上，而  Post  不会。所以，
            如果这些数据是中文数据而且是非敏感数据，那么使用  get ；如果用户输入的数据不是中文字符而且包含敏感数据，
            那么还是使用  post 为好。
        
        （4） 安全的和幂等的。所谓安全的意味着该操作用于获取信息而非修改信息。幂等的意味着对同一  URL  的多个请求
            应该返回同样的结果。完整的定义并不像看起来那样严格。换句话说， GET 请求一般不应产生副作用。从根本上讲，
            其目标是当用户打开一个链接时，她可以确信从自身的角度来看没有改变资源。比如，新闻站点的头版不断更新。虽
            然第二次请求会返回不同的一批新闻，该操作仍然被认为是安全的和幂等的，因为它总是返回当前的新闻。反之亦然。
            POST  请求就不那么轻松了。 POST  表示可能改变服务器上的资源的请求。仍然以新闻站点为例，读者对文章的注
            解应该通过  POST  请求实现，因为在注解提交之后站点已经不同了（比方说文章下面出现一条注解）.
            
    3、常见的状态码有哪些？
        
        1XX 信息性状态码（Informational）  服务器正在处理请求
        
        2XX 成功状态码（Success）          请求已正常处理完毕
            200 OK  表示请求被服务器正常处理
            204 No Content    表示请求已成功处理，但是没有内容返回
            206 Partial Content    表示服务器已经完成了部分GET请求
            
        3XX 重定向状态码（Redirection）     需要进行额外操作以完成请求
            301 Moved Permanently    永久重定向，表示请求的资源已经永久的搬到了其他位置
            302 Found  临时重定向，表示请求的资源临时搬到了其他位置
            303 See Other  表示请求资源存在另一个URI，应使用GET定向获取请求资源
            304 Not Modified  客户端发送附带条件的请求（GET方法请求报文中的IF…）时，条件不满足
            
        4XX 客户端错误状态码（Client Error）客户端原因导致服务器无法处理请求
            400 Bad Request  请求报文存在语法错误或参数错误，服务器不理解
            401 Unauthorized  表示发送的请求需要有HTTP认证信息或者是认证失败了
            403 Forbidden    表示对请求资源的访问被服务器拒绝了
            404 Not Found  表示服务器找不到你请求的资源
        
        5XX 服务器错误状态码（Server Error）服务器原因导致处理请求出错
            500 Internal Server Error  表示服务器执行请求的时候出错了
            503 Service Unavailable  表示服务器超负载或正停机维护，无法处理请求
        
        600 表示服务器没有返回响应头部，只返回实体内容，也算做服务器错误状态码吧，不过绝对不常见
        
        
    
"""

# 1、用cookie模拟登录人人网
#
# rikuedu9527


# 导入模块
from urllib import request,parse
import chardet,os
# cookie模块
import http.cookiejar

# 1.创建cookiejar对象，保存cookie
cookie = http.cookiejar.CookieJar()

# 2.创建cookie处理器对象
cookie_handler = request.HTTPCookieProcessor(cookie)

# 3.通过处理器对象构建Opener
opener = request.build_opener(cookie_handler)
opener.addheaders = [("User-Agent", 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)')]

# 4.创建登陆账户
data = {'email': "17752558702",'password':'qikuedu9527'}
postdata = parse.urlencode(data).encode('utf8')
print(postdata)

# 5.构建请求对象
req = request.Request("http://www.renren.com/PLogin.do",postdata)

# 6.通过opener发动登陆请求,cookie存于opener中
opener.open(req)

# 7.登录后进行登陆,获取响应response,登录后的url:http://www.renren.com/966924492
response = opener.open("http://www.renren.com/966924492")

# 8.存储响应页面
html = response.read().decode('utf8','ignore')
if not os.path.exists('files'):
    os.mkdir('files')
with open('files/myrenren.html','w',encoding='utf8') as f:
    f.write(html)








