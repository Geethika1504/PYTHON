#abstraction;- hiding unnessary info from user is called abstraction
#there are two type abstract calss  & abstract methods
#abstract class:- one or more abstract methods is called abastract class
#abstract method;-the method is declared without implimentation is called abstract method
'''class A():
    def method1(self):
        pass

obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("python course")
obj1=A()
obj1.method()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("data science")
obj1=A()
obj1.method1()'''#error

from abc import ABC,abstractmethod
class A(ABC):#parent class
    def method1(self):
        pass
    def method2(self):
        print("python full stack")
    def method3(self):

        pass
class B(A):
    def method1(self):
        print("datastructures")
    def method3(self):
        print("java fullstack")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()
        
        

