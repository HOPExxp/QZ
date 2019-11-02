import re
import requests
import time
import json

url = 'http://www.sodig.com/dir/人才招聘-公司企业/2/'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
             (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
html = requests.get(url ,headers = headers)

pattern = re.compile(
    #公司名称
    '.*?item-title">.*?>(.*?)</a>'+
    #公司网址
    '.*?item-cat">\n                                                    \
(.*?)\n\n                                                </div>',re.S
)

res = re.findall(pattern,html.text)
for i in res:
    print(i)