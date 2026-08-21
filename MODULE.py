#difference btw module nd package
'''1.A module in python is a single python file it consists python code
2.examples of module inclide math.py , random.py and my module.py
3.it contain functions , classes nd vairables

#package
one or more python modules and __init__.py file
examples of package includes request,numpy,pandas

#library
it consists both modules nd packages
examples of libraries numpy ,pandas and matplotlib

#note:- Every python file is a module and import is a key word and every python file is saved internally
with vairable name as __main__.'''

def greetings(name):
    print("welcome",name)


'''a=int(input("a value"))
b=int(input("b value))
print("the sum is" ,a+b)
#import mymodule
details={"idnos":[10,30,20]
         "names":["charm","pran","neha"],
         "marks":[70,80,90]}'''

#pending code verify through video

'''if __name__=="__main__":
 a=[10,20,30,40,50]
 a.append("code")
 a.extend("code")
 print(a)'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''

#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,4))
print(math.log(2))
print(math.tan(45))
print(math.sin(70))
print(math.cos(0))
print(math.ceil(2.9))
print(math.ceil(5.9))#round of value
print(math.ceil(8))
print(math.floor(2.7))'''#starting number

from math import pi,log,sqrt,ceil
'''print(pi)
print(log(10))
print(sqrt(2))

#system module
import sys
print(sys.path)
print(sys.version)'''

#os module
'''import os
print(os.path)
print((os.getcwd())
print(os.listdir())'''

'''print(os.mkdir("aug4"))
print(os.listdir())

print(os.chdir("C:\\Users\\vasu\\Downloads"))
print(os.listdir())'''

#ASCII
'''print(chr(100))

print(chr(65))

print(chr(90))

print(ord("a"))

print(ord("z"))

#print(ord(97))#error
print(chr(97))

for i in range(97,123):
    print(chr(i),end=" ")'''
#ASCII
'''print(chr(67))

print(chr(65))

print(chr(90))

print(ord("a"))

print(ord("z"))

#print(ord(97))#error
print(chr(97))'''

'''for i in range(97,123):
     print(chr(i), end=" ")'''

'''a=input("name")
for i in a:
    print(i,"-",ord(i))'''











