# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
#     'Cookie': 'c6ccb2be7a233c2f8637b82c1457820c5f9ea0f5b4a47a8cf641bbf526d6e3df00aa0900504fbcd4f047c8',
# }
# session = requests.Session()
# # 登录后，我们需要获取另一个网页中的内容
# response = session.get('https://yzapi.yazio.com/v1/user',headers = headers)
# print(response.status_code)
# print(response.text)
#
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    }
data = {
    'username':'383@qq.com',
    'password':'123',
}
url ='https://yzapi.yazio.com/v1/oauth/token'
session = requests.Session()
session.post(url,headers = headers,data = data)
# 登录后，我们需要获取另一个网页中的内容
response = session.get('https://yzapi.yazio.com/v1/user',headers = headers)
print(response.status_code)
print(response.text)
