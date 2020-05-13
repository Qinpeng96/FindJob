#类的使用
#和静态语言不同，Python允许对实例变量绑定任何数据，
#实例可以随时创造新的成员变量
class Student(object): #创建一个类
    count = 0 #类属性 
    #在内部和外部都采用类名.属性名访问
    #类属性为所有变量共用 因此可以用做计数器来使用
    def __init__(self,name,score): 
    #类的自定义构造函数
    #注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
        self.name = name
        self.score = score
        self.__age = 15;#通过添加__创建private变量

    def printInfo(self):  #类的第一个参数永远是self
        print(self.name)
        print(self.score)
    def printGender(self):
        print('no gender')
    @staticmethod  #静态方法
    def returnInfo():
        print('静态方法')

class man(Student):#继承父类 Student
    pass #继承全部方法
class woman(Student):#继承父类 Student
    def printGender(self):#覆盖方法
        print('i\'m woman')
        
def main():
    ming = Student('xiaoming',55) #对象的初始化
    ming.printInfo()
    ming.age = 10
    print(ming.age) #随时绑定新的数据
    a_man = man('man',1)
    a_woman = woman('woman',2)
    a_man.printGender()#调用父类 
    a_woman.printGender()#使用自己的方法
    woman.returnInfo()
main()