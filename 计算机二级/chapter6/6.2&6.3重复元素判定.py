# def choice(li):
#     counts = {}
#     for i in li:
#         counts[i] = counts.get(i,0) + 1
#     counts_f = dict([val,key] for key,val in counts.items())
#     for j in counts_f:
#         if j > 1:
#             return True
#     else:
#         return False
# # l = [1,2,3,4,1]
# while True:
#     l = eval(input('>>'))
#     if l == 'q' or l == '':
#         break
#     res = choice(l)
#     print(res)


while True:
    l = eval(input('>>'))
    if l == 'q' or l == '':
        break
    set_l = set(l)
    # print(set_l)
    if len(l) != len(set_l):
        print('True')
    else:
        print('False')