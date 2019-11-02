#顺序和反序相同
s = str(input('>>'))
if s == s[::-1]:
    print('是回文值')
else:
    print('不是回文值')
    print('本值：{}，反转值{}'.format(s,s[::-1]))
