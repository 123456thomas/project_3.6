# 导入服务器模块
from wsgiref.simple_server import make_server

#构建方法
def Index(env,response):
    response("200 OK", [("Content-type", "text/html")])
    # 判断输入路径
    if env["PATH_INFO"]=="/Findall":
        print("+++")
        return ["""<meta charset='utf-8'><ul>查看员工名单
			<li>张三</li>
			<li>王武</li>
			<li>依兰</li></ul>""".encode("utf8")]
    elif env["PATH_INFO"]=="/Addgood":
        return ["""<meta charset='utf-8'><ul>增添员工名单
			<li>张三</li>
			<li>王武</li>
			<li>依兰</li></ul>""".encode("utf8")]
    elif env["PATH_INFO"]=="/Delbad":
        return ["""<meta charset='utf-8'><ul>删除员工名单
			<li>张三</li>
			<li>王武</li>
			<li>依兰</li></ul>""".encode("utf8")]
    else:
        pass
    print(env["QUERY_STRING"])
    return ["<meta charset='utf-8'><p>Hello World绣春刀</p>".encode("utf8")]

# 创建服务器
hppt=make_server("",9110,Index)

# 启动服务器
hppt.serve_forever()

# str1="qwer&yuy78"
# wq=str1.rpartition("&")[2]
# print(wq)







# def Findall():
#     return ["""<meta charset='utf-8'><ul>添加员工名单
# 			<li>张三</li>
# 			<li>王武</li>
# 			<li>依兰</li></ul>""".encode("utf8")]
#
# def Addgood():
#     return ["""<meta charset='utf-8'><ul>员工名单
# 			<li>张三</li>
# 			<li>王武</li>
# 			<li>依兰</li></ul>""".encode("utf8")]
# def Delbad():
#     return ["""<meta charset='utf-8'><ul>删除员工名单
# 			<li>张三</li>
# 			<li>王武</li>
# 			<li>依兰</li></ul>""".encode("utf8")]

