# fi = open("论语-网络版.txt", "r", encoding="utf-8")
# fo = open("论语-提取版2.txt", "w",encoding="utf-8")
# wflag = False            #写标记
# for line in fi:
#     if "【" in line:     #遇到【时，说明已经到了新的区域，写标记置否
#         wflag = False
#     if "【原文】" in line:  #遇到【原文】时，设置写标记为True
#         wflag = True
#         continue
#     if line != "\n":
#         if wflag == True:    #根据写标记将当前行内容写入新的文件
#             for i in range(-25,0):
#                 for j in range(-45,0):
#                     line = line.replace("{}·{}".format(-i,-j),"**")
#             #  for i in range(0,25):
#             #     for j in range(0,25):
#             #         line = line.replace("{}·{}".format(i,j),"**")
#             # for i in range(0,10):
#             #     line = line.replace("*{}".format(i),"")
#             # for i in range(0,10):
#             #     line = line.replace("{}*".format(i),"")
#             line = line.replace("*","")
#             fo.write(line.strip()+"\n")
# fi.close()
# fo.close()


#=====================================
fi = open("论语-提取版2.txt", "r",encoding="utf-8")
fo = open("论语-原文2.txt", "w",encoding="utf-8")
for line in fi:   #逐行遍历
    for i in range(1,15):  #对产生1到22数字
        line=line.replace("({})".format(i), "")  #构造(i)并替换
    fo.write(line)
fi.close()
fo.close()