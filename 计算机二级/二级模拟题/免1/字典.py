ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", "综合", "综合", \
      "师范", "理工", "综合", "理工", "综合", "综合", "综合", "综合", "综合", "理工", \
      "理工", "理工", "理工", "师范", "综合", "农林", "理工", "综合", "理工", "理工", \
      "理工", "综合", "理工", "综合", "综合", "理工", "农林", "民族", "军事"]

# dic = {}
# zh,lg,sf,nl,mz,js = 0
# for l in ls:
#     if l == "综合":
#         zh += 1
#     if l == "理工":
#         zh += 1
#     if l == "师范":
#         zh += 1
#     if l == "农林":
#         zh += 1
#     if l == "民族":
#         zh += 1
#     if l == "军事":
#         zh += 1
#     if l == "综合":
#         zh += 1

#=======================================

# dic = {}
# for a in ls:
#     dic[a] = 1
# print(dic)
#
# for l in ls:
#     if dic[l]:
#         dic[l] += 1
# print(dic)
#
# # sorted(dic.items(),key = lambda x:x[1],reverse = False)
#
# for i,j in sorted(dic.items(),key = lambda x:x[1]):
#     print(i+":"+str(j))

#======================================
d = {}
for word in ls:
    d[word] = d.get(word, 0) + 1
for k in d:
    print("{}:{}".format(k, d[k]))
