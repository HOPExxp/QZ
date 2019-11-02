import random
from math import sqrt
from time import clock

datas = 10000
hits = 0
for i in range(datas):
    random.seed(i+1)
    a , b = random.random(),random.random()
for i in range(datas):
    random.seed(i+1)
    a , b = random.random(),random.random()
    if sqrt(a**2 + b**2) < 1:
        hits += 1
print(4*hits/datas)

# random.seed(23)
# print('{}{}{}'.format(random.random(),random.random(),random.random()))
# #0.92486525162594520.94860577799317710.8924333440485793
# print('{}{}{}'.format(random.random(),random.random(),random.random()))
# #0.083550676830683620.59202722688573530.4237474082349614
# random.seed(23)
# print('{}{}{}'.format(random.random(),random.random(),random.random()))
# #0.92486525162594520.94860577799317710.8924333440485793
