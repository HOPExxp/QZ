import random
li = []
for i in range(65,91):
    li.append(chr(i))
for j in range(97,123):
    li.append(chr(j))
for k in range(10):
    li.append(k)

for h in range(10):
    res = random.sample(li, 8)
    print(''.join(map(str, res)))


# def check_code():
#     import random
#     checkcode = ''
#     for i in range(4):
#         current = random.randrange(0,4)
#         if current != i:
#             #ascii 65-90 对对应大写英文字母
#             temp = chr(random.randint(65,90))
#         else:
#             temp = random.randint(0,9)
#         checkcode += str(temp)
#     return checkcode