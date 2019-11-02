import socket
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