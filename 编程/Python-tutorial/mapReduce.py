#map实现
def add_1(x,y):
    return x+y

l = [1,3,5,7,9]
r = [2,4,6,8,10]
res = map(add_1,l,r)
print(list(res))

#reduce实现
from functools import reduce
def add_2(x,y):
    return x*10+y
res1 = reduce(add_2,[1,3,5,7])
print(int(res1))