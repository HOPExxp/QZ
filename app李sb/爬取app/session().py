import requests
#****************     1
# #创建session对象
# s = requests.Session()
# #设置cookies
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# print(s.cookies)
# #发起另一个get请求，获取cookies
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

#****************     2
# s=requests.Session()
# #设置session对象的auth属性，用来作为请求的默认参数
# s.auth=('user','pass')
# #设置session的headers属性，通过update方法，将其余请求方法中的headers属性合并起来作为最终的请求方法的headers
# s.headers.update({'x-text':'true'})
# #发送请求，这里没有设置auth会默认使用session对象的auth属性，这里的headers属性会与session对象的headers属性合并
# r=s.get('http://httpbin.org/headers',headers={'x-test2':'true'}) #如果设置相同的'x-text'则会覆盖上面设置的header
# print(r.text)

#****************     3
#函数参数中的数据只会使用一次，并不会保存到session中
import requests
s=requests.Session()
s.auth=('user','pass')
s.headers.update({'x-text':'true'})
r=s.get('http://httpbin.org/headers',headers={'x-test2':'true'})
print(r.text)
r=s.get('http://httpbin.org/headers')
print('第二次访问结果')
print(r.text)