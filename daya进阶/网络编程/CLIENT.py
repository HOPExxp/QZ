# socket_echo_client.py
import socket
import sys
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 设置 主机地址   端口
server_address = ("localhost",1000)
print("connecting to {} port{}".format(*server_address))
sock.connect(server_address)

try:
    msg = input('>>')
    print("sending{!r}".format(msg))
    sock.sendall(msg.encode('utf-8'))
    # 服务器发送，  好多值，服务器发送多少次信息过来，取决于你发送多次信息
    # len(msg)--防止一个极端
    accept = 0
    server_accept = len(msg)
    while accept < server_accept:
        # reciv的值一定要大于等于server的resv
        data = sock.recv(20)
        # 接收一次accept改变一次长度
        accept +=len(data)
        print("recived{!r}".format(data))
finally:
    print("colsing socket")
    sock.close()