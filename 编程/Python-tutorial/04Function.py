#call function C++
#python当中的数据类型转换
#int() 将参数转换为int型 str() bool  以此类推
from selfFunctions import add
import functools
from selfFunctions import nop
from selfFunctions import divde
import module


c = add(10,5)
print(c)

#返回多个参数 tuple
s = divde(45)
print(s)
module.hello();
#关于函数参数 
#默认参数 同C++ 
#定义默认参数要牢记一点：默认参数必须指向不变对象！
#可变参数 *
#递归参数

#闭包
def add(x,y):
    def selfSum():
        return x+y;
    return selfSum
f = add(5,10)
print(f())
#匿名函数
#偏函数
int2 = functools.partial(int,base = 2)
c = int2('10010')
print(c)
