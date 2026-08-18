#oops
#syntax
'''class classname():
    #attributes
    name="pooja"
    age=28
    place="vij"
    def fname(method_name):
        print("statements.......")
a=classname()
print(dir(a))
a.fname()'''

#class declaration
'''class Details():
    name="geeth"
    age=21
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#object instantiation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("geethika",22,"vja")
a.display()
b=Details()
b.data("ketan",21,"vij")
b.display()'''

#object intialisation  -__init__ constructor
'''class data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=data("sailu",21,"vij")
print(dir(a))
a.display()'''

#runtime ,method1
'''class data():
    def __init__(self):
        self.name=input("enter the name")
        self.age=int(input("enter the age"))
        self.place=input("enter the place")
    def display(self):
        print(self.name,self.age,self.place)
a=data()
print(dir(a))
a.display()'''

#method2
'''class data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=data(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()'''

'''diff btw_ and __ when user want to create a vairable in python by using double leading underscore our pyton
interpretor treats it as a special vairable to avoid name conflicts with methods nd inner classes'''     

'''class Employee1():
    def __init__(self):
        self.name="pooja"
        self._mailid="pooja@codegnan.com"
        self.__salary=10000#private vairable
class Employee2():
    def __init__(self):
        self.name="geethika"
        self._mailid="geethika@codegnan.com"
        self.__salary=80000
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee1__salary)
b=Employee2()
print(dir(b))
print(b.name)
print(b._mailid)
print(b._Employee2__salary)'''

#polymorphism
#operator overloading
#operator overloading
'''a=4 ;b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(2))
print(a.__mul__(6))
print(a.__pow__(2))
#print(a.__div (4))
print(a.__eq__(5))
print(a.__le__(8))
print(a.__ge__(10))
a=[1, 2, 3, 4, 5];b= [6, 71, 8, 9, 10]
print(a.__add__(b))
print(a.__getitem__(3))
print(a.__getitem__(4))
a="poython";b="course"
print(a.__add__ (" "+b).title())
a="poython";b="course"
print(a.__add__(b))'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
    def __add__(self,value):
        return self.b*value.a
x=A(7)
y=B(4)
#x=8
#y=6
print(x+y)'''

#method  overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is" ,a+b+c)
        elif a!=None and b!=None:
            print("products is",a*b)
        else:
            print("program ends.....")
a=new()
#a.sum
#a.sum(4,6,7)
a.sum(4,5)'''

#method overriding
'''class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

'''class vehical():
    def speak(self):
        print("my favourite vehical")
class car():
    def speak(self):
        print("is car")
a=vehical()
b=car()
a.speak()
b.speak()'''

#inheritence
#single inheritence
'''class RBI():#parent
    cash=100000
    def available_cash(cls):#child2
        #print("available cash is",cls.cash
        print("available cash is",RBI.cash)
class SBI(RBI):#child1
    pass
class HDFC(RBI):#child2
    cash=50000
    def new_cash(cls):
        #print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#multiple inheritence

'''class Father:#parent class1
    def height(self):#OR (cls)
        print("Father's height: 6 feet")

class Mother:#parent class2
    def weight(self):
        print("Mother's weight is 60kgs")

class Child(Father, Mother):
    def dob(self):
        print("just born...")

c=Child()
c.height()
c.weight()
c.dob()'''

#without inheritence 

'''class Father:#parent class1
    def height(self):#OR (cls)
        print("Father's height: 6 feet")

class Mother:#parent class2
    def weight(self):
        print("Mother's weight is 60kgs")

class Child():
    def dob(self):
        print("just born..")
a=Father()
b=Mother()
c=Child()
a.height()
b.weight()
c.dob()'''

#multilevel
'''class Grandfather():
    def land(self):
        print("grandfather's land 1acre")

class Father(Grandfather):
    def house(self):
        print("Father's house 100sqft ")

class Child(Father):
    def bike(self):
        print("pulsar")

c = Child()
c.land()
c.house()
c.bike()'''

#hierarchical inheritence:-Where one parent class is inherited by multiple child classes

'''class employee():
    def company(self):
        print("company name is myntra")

class Trainer(employee):
    def teaching(self):
        print(" trainer teaches the code")

class Developer(employee):
    def develop(self):
        print("Developer develops code")
a=Trainer()
a.company()
a.teaching()
b=Developer()
b.develop()
b.company()'''


#hybrid inheritence is combining one or more than one type of inheritence for example multiple inheritence plus hierarchical
'''class person:
    def details(self):
        print("geethika")
class trainer(person):
    def teach(self):
        print("teaching")
class student(person):
    def study(self):
        print("learning")
class program_manager(trainer,student):
    def manager(self):
        print("assign classes")
a=program_manager()
a.details()
a.teach()
a.study()
a.manager()'''

#super()
'''class parent:
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):#sub class
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("pooja",28)
print(a.age)
print(a.name)'''

#combing multiple units into single unit is called encapsulation
#protected data ,private data,public data

#public data
'''class A():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)
obj1=B()
obj1.method1()
obj1.method2()'''

#protecteddata
'''class A():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)
obj1=B()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#___privatedata
class A():
    __privatedata="geethika"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
obj1=B()
obj1.method1()
obj1.method2()
