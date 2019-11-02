import requests

# 登录人人网的url
url0 = "http://www.renren.com/PLogin.do"
# 登录到个人主页的url
url1 = "http://www.renren.com"
data = {'email': "13870668046",
        'password': '41632543xxp'}
# 进行登录，并保存cookie
req = requests.Session()

response = req.post(url0, data=data)
# 可以直接访问个人主页了

zhuye = req.get(url1)
print(zhuye.text)
