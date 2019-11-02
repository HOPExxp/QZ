from urllib.request import ProxyHandler,build_opener
from urllib.error import URLError

# 构造协议
# proxy = "127.0.0.1:808"
# 加上认证
proxy = "user1:123@127.0.0.1:808"
proxy_handler = ProxyHandler({
    "http":"http://"+proxy,
    "https":"https://"+proxy,
})

# 执行
opener = build_opener(proxy_handler)
try:
    response = opener.open("http://httpbin.org/get")
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)