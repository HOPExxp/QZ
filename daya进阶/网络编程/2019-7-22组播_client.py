# socket_echo_client_dgram.py
import socket
import struct

#发送端  -- 发送信息给组播地址
#添加的操作
#1.为接收相应设置超时值
#2.转换为组播套接字

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #买手机

#也不需连接 -- connect操作，直接发送信息，带上目标地址信息即可
#  其余均相同 ； 即udp协议下的连接不需反馈信息，每端只需做好自己的事情，不管对反是否正常接收到信息

server_address = ("localhost", 10000)
message = b'This is the message.  It will be repeated.'

#1
sock.settimeout(0.5)

#2
# 数据---数据的转换
ttl = struct.pack('b',1)

# 转化成为组播套接字
sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,ttl)

try:

    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()