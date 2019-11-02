# ipaddress_addresses.py
import binascii
import ipaddress
class checkAddress():
    def __init__(self,addresses):
        self.addresses = addresses
        for ip in self.addresses:
            addr = ipaddress.ip_address(ip)
            print('{!r}'.format(addr))
            print('   IP version:', addr.version)
            print('   is private:', addr.is_private)
            print('  packed form:', binascii.hexlify(addr.packed))
            print('      integer:', int(addr))
            print()
ADDRESSES = [
    '10.9.0.6',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]
checkAddress(ADDRESSES)

# ipaddress_networks.py
import ipaddress
class checkNetwork():
    def __init__(self,networks):
        self.networks = networks
        for n in self.networks:
            net = ipaddress.ip_network(n)
            print('{!r}'.format(net))
            print('     is private:', net.is_private)
            print('      broadcast:', net.broadcast_address)
            print('     compressed:', net.compressed)
            print('   with netmask:', net.with_netmask)
            print('  with hostmask:', net.with_hostmask)
            print('  num addresses:', net.num_addresses)
            print()
NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
]
checkNetwork(NETWORKS)

import ipaddress
class checkNetworkIps():
    def __init__(self,networks):
        self.networks = networks
        for n in self.networks:
            net = ipaddress.ip_network(n)
            print('{!r}'.format(net))
            for i, ip in zip(range(3), net):
                print(ip)
                # return ip
            print()
NETWORKS = [
    '10.9.0.0/24',
    'fdfd:87b5:b475:5e3e::/64',
]
checkNetworkIps(NETWORKS)

# # ipaddress_addresses.py
# import binascii
# import ipaddress
# class checkAddress():
#     def __init__(self,addresses):
#         self.addresses = addresses
#     def printResult(self):
#         for ip in self.addresses:
#             addr = ipaddress.ip_address(ip)
#             # print('{!r}'.format(addr))
#             # print('   IP version:', addr.version)
#             # print('   is private:', addr.is_private)
#             # print('  packed form:', binascii.hexlify(addr.packed))
#             # print('      integer:', int(addr))
#             # print()
#             return '{!r}'.format(addr) , 'IP version:', addr.version , 'packed form:', binascii.hexlify(addr.packed) , \
#                    'integer:', int(addr)
#
# ADDRESSES = [
#     '10.9.0.6',
#     'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
# ]
# init = checkAddress(ADDRESSES)
# result = init.printResult()
# for i in result:
#     print(i)

###########################

# # ipaddress_network_iterate.py
# import ipaddress
#
# class checkNetworkIps():
#     def __init__(self,networks):
#         self.networks = networks
#     def printResult(self):
#         for n in self.networks:
#             net = ipaddress.ip_network(n)
#             # print('{!r}'.format(net))
#             ips = []
#             for i, ip in zip(range(3), net):
#                 # print(ip)
#                 ips.append(ip)
#             # print()
#             return net,ips
# NETWORKS = [
#     '10.9.0.0/24',
#     'fdfd:87b5:b475:5e3e::/64',
# ]
# init = checkNetworkIps(NETWORKS)
# result = init.printResult()
# print('{!r}'.format(result))

