
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #买手机

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)        #买电话卡

#  ** 不需要监听（开机）--监听多个电话  ，  也不需要接通电话  -- 不用反馈信息给发送端，不用建立连接

#  原本是接听电话得到链接和地址，再从链接上接收信息  用recv  ；反馈信息时只需发送信息（已建立链接）
#  现在直接接收信息 用recvfrom   ； 反馈信息时除了信息外，还要指定目标地址（未建立链接）

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(sent, address))
# 使用 recvfrom() 从套接字读取消息，然后按照客户端地址返回数据。