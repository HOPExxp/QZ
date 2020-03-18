import time
import requests
import re
import json
share_id = '88445518961'
share_url = 'https://www.douyin.com/share/user/' + share_id

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
dytk_search = re.compile(r"dytk: '(.*?)'")
tac_search = re.compile(r"<script>tac=(.*?)</script>")
# print(dytk_search)
response = requests.get(url = share_url,headers = header)
# print(response.text)
dytk = re.search(dytk_search,response.text).group(1)
tac = "var tac="+ re.search(tac_search,response.text).group(1) +";"
print(dytk)
print(tac)

with open('html_head.txt','r') as f1:
    f1_read = f1.read()

with open('html_foot.txt','r') as f2:
    f2_read = f2.read().replace("&&&",share_id)

with open('test.html','w') as f_w:
    f_w.write(f1_read + '\n' + tac + '\n' +f2_read)

signature = input('密钥为')
movie_url = 'https://www.douyin.com/web图书馆书/api/v2/aweme/post/?user_id='+share_id+'&sec_uid=&count=21&max_cursor=0&aid=1128&_signature='+signature+'&dytk=' + dytk
while True:
    movie_response = requests.get(url = movie_url,headers = header)
    if json.loads(movie_response.text)['aweme_list'] ==[]:
        print(movie_response.text)
        time.sleep(1)
        continue
    else:
        print(movie_response.text)
        break