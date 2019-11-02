#将csv格式转换为html格式

#e13.1csv2html.py
#标签开始及表格、表头的开始，还有一些样式设置
seg1 = '''
<!DOCTYPE HTML>\n<html>\n<body>\n<meta charset=gb2312>
<h2 align=center>2016年7月部分大中城市新建住宅价格指数</h2>
<table border='1' align="center" width=70%>
<tr bgcolor='orange'>\n'''
#表头结尾
seg2 = "</tr>\n"
#结尾标签
seg3 = "</table>\n</body>\n</html>"
#填充表格内容
def fill_data(locls):
    seg = '<tr><td align="center">{}</td><td align="center">{}</td><td align="center">{}</td><td align="center">{}</td></tr>\n'.format(*locls)
    return seg
#从csv文件中读入数据，全部存放在一个二维列表中
fr = open("price2016.csv", "r",encoding='utf-8')
ls = []
for line in fr:
    line = line.replace("\n","")
    ls.append(line.split(","))
fr.close()
#将内容处理后写入html文件
fw = open("price2016.html", "w",encoding='utf-8')
fw.write(seg1)
#ls[0]  写入表头信息
fw.write('<th width="25%">{}</th>\n<th width="25%">{}</th>\n<th width="25%">{}</th>\n<th width="25%">{}</th>\n'.format(*ls[0]))
#结束表头信息
fw.write(seg2)
# 逐行写入内容信息
for i in range(len(ls)-1):
    fw.write(fill_data(ls[i+1]))
#写入结尾信息
fw.write(seg3)
fw.close()
