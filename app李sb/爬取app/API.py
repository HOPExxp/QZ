import json
import requests
url1 = 'https://www.iesdouyin.com/aweme/v1/challenge/aweme/?ch_id=1574030716416014&count=9&cursor=0&aid=1128&screen_limit=3&download_click_limit=0&_signature=QAbfVBAYHTaObVmG1P-pVkAG30'
url = 'https://www.iesdouyin.com/aweme/v1/challenge/aweme/?ch_id=1574030716416014&count=9&cursor=0&aid=1128&screen_limit=3&download_click_limit=0&_signature=XFt5MRAVAWqSMP.jPenjdVxbeS'
# print(url)
html1 = requests.get(url1).text
# 此html包含json格式，需解析
print(html1)
dict_url = json.loads(html1)
print(dict_url)