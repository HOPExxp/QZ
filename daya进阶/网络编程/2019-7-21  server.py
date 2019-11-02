# socket_echo_server.py
#实现：  IPV4/IPV6  TCP/UDP  主机地址   端口，监听

import socket
class server_user():
    def __init__(self):
        #基本设置
        self.sock,self.server_address = self.base_settings()
        print("starting server:adress {}---port {}".format(*self.server_address))
        #开启服务端
        self.start_server()
        self.handle_data()
    def base_settings(self):
        # 设置IPV4/IPV6  TCP/UDP
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 设置 主机地址   端口
        server_address = ("localhost",1112)
        return (sock,server_address)
    def start_server(self):
        # 开启一个server服务。
        self.sock.bind(self.server_address)
        # 每个1秒做监听
        self.sock.listen(1)
    def handle_data(self):
        # 一旦有信息，接收并且输出---反馈
        while True:
            #接受客户端的请求
            connection, client_adress = self.accept_data()
            try:
                #处理信息--接收/反馈
                self.rec_send_data(connection,client_adress)
            finally:
                # 关闭和某一个客户端的链接
                connection.close()
    def accept_data(self):
        print("wait for connect:")
        # 接收客户端的信息
        connection, client_adress = self.sock.accept()
        return (connection, client_adress)
    def rec_send_data(self, connection, client_adress):
        print("connection", client_adress)
        while True:
            # 从通道上接收发送过来的数据
            data = connection.recv(16)
            print("recivered{!r}".format(data))
            if data:
                print("sending data back to client")
                # 反馈给客户端一个信息,接收客户端是32，返回也是32
                connection.sendall(data)
            else:
                print("no data from", client_adress)
                break

server_user()