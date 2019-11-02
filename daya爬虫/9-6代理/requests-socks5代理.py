import requests


proxy = '127.0.0.1:1080'
proxies = {
    'socks5':'socks5://'+proxy
    }
try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)

# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0"
#   },
#   "origin": "223.104.170.112, 223.104.170.112",
#   "url": "https://httpbin.org/get"
# }