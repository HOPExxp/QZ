import re
#daya 0730 11223344 pythoncollege

# content='daya 073011223344 pythoncollege'
# r = re.match('.*(\d{2}).*',content)
# r1 = re.match('.*(\d{12}).*',content)
# print(r.group())
# print(r.group(1))
# print(r1.group(1))



# content='daya 073011223344 pythoncollege'
# r = re.match('.*?(\d{2}).*',content)
# r1 = re.match('.*?(\d{12}).*',content)
# print(r.group())
# print(r.group(1))
# print(r1.group(1))

import re

content1 = '2019-8-14 09:00'
content2 = '2019-8-14 14:00'
content3 = '2019-8-14 21:00'

p = re.compile('\d{2}:\d{2}')
r1 = re.sub(p,'',content1)
r2 = re.sub(p,'',content2)
r3 = re.sub(p,'',content3)
print(r1,r2,r3)