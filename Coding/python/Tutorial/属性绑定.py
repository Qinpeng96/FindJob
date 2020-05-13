from types import MethodType

class Student():
    def __init__(self,_score,_age):
        self.score = _score
        self.age = _age
    
def setAge(self,_age):
    self.age = _age;
    print("调用")

def main():
    s1 = Student(21,20) 
    s1.setAge = MethodType(setAge,s1) #给实例绑定方法
    s1.setAge(25)
    Student.setAge = MethodType(setAge,Student)#给类绑定方法
    s2 = Student(15,16)
    s2.setAge(17)
    print(s1.age)
    print(s2.age)
main() 
