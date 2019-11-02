# socket_echo_client.py
import socket
class client_user():
    def __init__(self):
        #基本设置
        self.sock,self.server_address = self.base_settings()
        print("connecting to {} port{}".format(*self.server_address))
        #连接服务器
        self.connect_server()
    def base_settings(self):
        # 设置IPV4/IPV6  TCP/UDP
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 设置 主机地址   端口
        server_address = ("localhost",1112)
        return (sock,server_address)
    #用户数据
    def get_data(self):
        # msg = hex(input('输入你想发送的数据：'))
        msg = b"This is megssge   ,It will be repearted."
        return msg
    def connect_server(self):
        self.msg = self.get_data()
        self.sock.connect(self.server_address)
        try:
            #发送数据
            self.send_data()
            #处理反馈数据
            self.rec_feedback()
        finally:
            print("colsing socket")
            self.sock.close()
    #发送数据
    def send_data(self):
        print("sending{!r}".format(self.msg))
        self.sock.sendall(self.msg)
    # 处理反馈数据
    def rec_feedback(self):
        # 服务器发送，  好多值，服务器发送多少次信息过来，取决于你发送多次信息
        # len(msg)--防止一个极端
        accept = 0
        server_accept = len(self.msg)
        while accept < server_accept:
            # reciv的值一定要大于等于server的resv
            data = self.sock.recv(20)
            # 接收一次accept改变一次长度
            accept += len(data)
            print("recived{!r}".format(data))

client_user()