import requests
url = 'http://m.ip138.com/ip.asp?ip='
ip = str(input('请输入你的ip：'))
urll = url + ip
try:
    f = requests.get(urll)
    f.raise_for_status()
    f.encoding = f.apparent_encoding
    print(f.text)
except:
    print('爬取失败')
