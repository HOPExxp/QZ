import socket
from urllib.parse import urlparse
class socket_test():
    def __init__(self,hosts,urls):
        self.hosts = hosts
        self.urls = urls
    def getHostName(self):
        print(socket.gethostname())
    def getHostbyName(self):
        for host in self.hosts:
            try:
                print('{} : {}'.format(host, socket.gethostbyname(host)))
            except socket.error as msg:
                print('{} : {}'.format(host, msg))
    def getHostByName_Ex(self):
        for host in self.hosts:
            print(host)
            try:
                name, aliases, addresses = socket.gethostbyname_ex(host)
                print('  Hostname:', name)
                print('  Aliases :', aliases)
                print(' Addresses:', addresses)
            except socket.error as msg:
                print('ERROR:', msg)
            print()
    def getFqdn(self):
        for host in ['www.python.org', 'pymotw.com']:
            print('{:>10} : {}'.format(host, socket.getfqdn(host)))
    def getHostbyAddr(self):
        hostname, aliases, addresses = socket.gethostbyaddr('192.168.1.104')
        print('Hostname :', hostname)
        print('Aliases  :', aliases)
        print('Addresses:', addresses)
    def getServerbyName(self):
        for url in self.urls:
            parsed_url = urlparse(url)
            port = socket.getservbyname(parsed_url.scheme)
            print('{:>6} : {}'.format(parsed_url.scheme, port))
    def getServerbyPort(self):
        for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
            url = '{}://example.com/'.format(socket.getservbyport(port))
            print(url)
    def getProtobyName(self):
        def get_constants(prefix):
            """Create a dictionary mapping socket module
            constants to their names.
            """

            return {
                # getattr就是工厂模式，能够按照n的模型输出结果
                getattr(socket, n): n
                for n in dir(socket)
            # 开头prefix规则以后给
            if n.startswith(prefix)
        }
        protocols = get_constants('IPPROTO_')

        for name in ['icmp', 'udp', 'tcp']:
            proto_num = socket.getprotobyname(name)
            const_name = protocols[proto_num]
            print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(
                name, proto_num, const_name,
                getattr(socket, const_name)))

HOSTS = [
        'CN-20190430AHQN',
    'pymotw.com',
    'www.python.org',
    'nosuchname',
]

URLS = [
    'http://www.python.org',
    'https://www.mybank.com',
    'ftp://prep.ai.mit.edu',
    'gopher://gopher.micro.umn.edu',
    'smtp://mail.example.com',
    'imap://mail.example.com',
    'imaps://mail.example.com',
    'pop3://pop.example.com',
    'pop3s://pop.example.com',
]

test = socket_test(HOSTS,URLS)
test.getHostbyName()