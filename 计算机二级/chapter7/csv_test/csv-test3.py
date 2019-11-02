#加入数据
fo = open("price2016.csv", "a",encoding='utf-8')
ls = ['萍乡', '101.5', '120.7', '121.4']
fo.write(",".join(ls)+ "\n")
fo.close()