# x = chr(0x4dc0)
# print(x)
# print(type(x))

x = int(0x4df2)
print("二进制{0}、十进制{1}、八进制{2}、十六进制{3}".format(bin(x),x,oct(x),hex(x)))

y = int(0x4dc0)+50
print("二进制{0}、十进制{1}、八进制{2}、十六进制{3}".format(bin(y),y,oct(y),hex(y)))

print("二进制{0:b}、十进制{0}、八进制{0:o}、十六进制{0:x}".format(0x4DC0+50))
