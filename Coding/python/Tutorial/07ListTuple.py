#本文学习链接:https://www.liaoxuefeng.com/wiki/1016959663602400/1017092876846880
#list使用 元素可以随意修改 list之中也可以包含list
classmate = ['a','bc','def']
classmate.append('g')
classmate.insert(1,'h')
classmate.pop()
classmate.pop(1)
#空list
s = []
print(len(classmate))
print(classmate[0])
print(classmate[-1])
#列表生成式
a = [x*x for x in range(10)]
print(a)
#生成器
b = (x*x for x in range(10000))
print(next(b))
print(next(b))
print(next(b))



