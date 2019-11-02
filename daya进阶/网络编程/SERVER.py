# socket_echo_server.py
import socket
import sys
#  IPV4/IPV6  TCP/UDP  主机地址   端口，监听

# 设置IPV4/IPV6  TCP/UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 坚持    你努力就对了---你努力的结果交给命运
# 设置 主机地址   端口
server_address = ("localhost",1000)
print("starting server:adress{}---port{}".format(*server_address))
# 开启一个server服务。
sock.bind(server_address)
# 每个1秒做监听
sock.listen(1)

# 一旦有信息，接收并且输出---反馈
while True:
    print("wait for connect:")
    # 接收客户端的信息
    connection,client_adress = sock.accept()
    try:
        print("connection",client_adress)
        while True:
            # 从通道上接收发送过来的数据
            data = connection.recv(16)
            print("recivered{!r}".format(data))
            if data:
                print("sending data back to client")
                # 反馈给客户端一个信息,接收客户端是32，返回也是32
                connection.sendall(data)
            else:
                print("no data from",client_adress)
                break
    #  关闭和某一个客户端的链接
    finally:
        connection.close()