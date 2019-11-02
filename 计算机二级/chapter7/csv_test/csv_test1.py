#。。。
fo = open("price2016.csv", "r",encoding="utf-8")
ls = []
for line in fo:
    # print(line)
    line = line.replace("\n","")
    print(line)
    #存入列表，列表存入列表，全部存入列表中才退出循环打印整个列表
    ls.append(line.split(","))
print(ls)
fo.close()
