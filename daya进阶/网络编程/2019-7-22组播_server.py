# socket_echo_server_dgram.py
import socket
import struct

#接收端
#增加的操作：
#1.监听的用户的地址（谁需要从组播中拿信息）
#2.转换为组播套接字  涉及ip地址的转换（成二进制）

#1 组播地址 -- 从哪里接收信息
group_address = '224.3.29.73'

# Create a UDP socket
# AF_INET使用ipv4， SOCK_DGRAM 类型的 socket 特点: 只有一个接收缓冲#区,而不存在发送缓冲区。
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #买手机

# Bind the socket to the port
server_address = ("localhost", 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)        #买电话卡

#  ** 不需要监听（开机）--监听多个电话  ，  也不需要接通电话  -- 不用反馈信息给发送端，不用建立连接

#  原本是接听电话得到链接和地址，再从链接上接收信息  用recv  ；反馈信息时只需发送信息（已建立链接）
#  现在直接接收信息 用recvfrom   ； 反馈信息时除了信息外，还要指定目标地址（未建立链接）

#2
# IP地址的转化
group = socket.inet_aton(group_address)
# 传输物理设备--网卡  INADDR_ANY表示所有的网卡--编程二进制的数据
mreq = struct.pack('4sL',group,socket.INADDR_ANY)
#  IP_ADD_MEMBERSHIP添加一个组播，接收的组播信息
sock.setsockopt(
   socket.IPPROTO_IP,
   socket.IP_ADD_MEMBERSHIP,
   mreq)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(sent, address))
# 使用 recvfrom() 从套接字读取消息，然后按照客户端地址返回数据。