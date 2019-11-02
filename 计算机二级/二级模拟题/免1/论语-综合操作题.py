with open("论语-网络版.txt",'r',encoding="utf-8") as f:
    lines = f.readlines()
i = 0
li = []
with open("论语-提取版.txt", 'w', encoding="utf-8") as f1:
    for l in lines:
        if "原文" in l:
            # print(lines[i+2])
            # print(lines[i+2].strip())
            li.append(lines[i+2])
        i += 1
    # print(li)

    for j in li:
        j = j.strip()
        # print(j)
        for k in j:
            if k == "·":
                j = j.replace(k,"")
                # print(j)
        for m in j[:4]:
            if m.isdecimal():
                j = j.replace(m,"")
        # print(j)
        f1.write(j+"\n")



#进一步处理提取版论语
# with open("论语-提取版.txt",'r',encoding="utf-8") as f2:
#     r = f2.readlines()
# for i in r:
#     i = i.replace("()","")
#     i = i.replace("(1)","")
#     i = i.replace("(2)","")
#     i = i.replace("(3)","")
#     i = i.replace("(4)","")
#     i = i.replace("(5)","")
#     i = i.replace("(6)","")
#     i = i.replace("(7)","")
#     i = i.replace("(8)","")
#     i = i.replace("(9)","")
#     i = i.replace("(10)","")
#     with open("论语-原文.txt","a+",encoding="utf-8") as f3:
#         f3.write(i)