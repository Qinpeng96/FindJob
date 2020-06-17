#python数据类型
#整数、浮点数、字符串、布尔值、
#空值 用Null来表示 不可与0等同
#可以把任意数据类型肤质给变量 一个变量也可以接受多个不同类型的赋值
#len()函数统计字符个数 中文和英文算作一个字符 在bytes中 中文算两个字节 在utf-8中 中文算三个字节
#python的格式化输出
print('my name is %s,my age is %d'%('ax',22))
#字符串str与字节bytes之间的相互转换
a = b'num'
print(len(a))
a = "中文"
print(len(a.encode('utf-8')))
print(type(a.encode('utf-8')))