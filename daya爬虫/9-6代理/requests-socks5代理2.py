import requests
import socks
import socket

socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',1080)
socket.socket = socks.socksocket

try:
    res = requests.get('http://httpbin.org/get')
    print(res.text)
except requests.exceptions.ConnectionError as e:
    print('err',e.args)