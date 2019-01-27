"""
numpy入门
"""
import json

a =[1,2,3,4]
jso_a = json.dumps(a)
# str1 = ",".join(jso_a)
with open('jp.csv','w',encoding='utf8') as f:
    f.write(jso_a)
print(jso_a,type(jso_a))