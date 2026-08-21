#built in functions print(),max(),min(),len(),range,pow,type,sum
#print(dir())

#print(dir("__builtins__"))

#fromkeys
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))'''
#print(dict(a))#error so we use fromkeys.
#fromkeys only work for dict
'''b=dict.fromkeys(a)
print(b)#you none for duplicate values
c=dict.fromkeys(a,"geethika")#To replace that none to any word you prefer we use this
print(c)

c["o"]="python" 
print(c)'''# in place of none you give geethika now you cange o:geethika to 0:python or anything 


#eval()
'''while True:
 a=int(input("a value"))#int dont conver to float
 b=int(input("b value"))
 print(a+b)'''

'''while True:
 a=float(input("a value"))#float accepts int
 b=float(input("b value"))
 print(a+b)'''

'''while True:
 a=string(input("a value"))#float accepts int
 b=string(input("b value"))
 print(a+b)'''

'''while True:
 a=eval(input("a value"))
 b=eval(input("b value"))
 print(a+b)'''
#zip we can combine multiple collections into one collections
'''a=[10,20,30,40,50,60]
names=["harini","neha","priya","pam","junkook"]
print(a+names)
#should be matching extra value ends up being empty
b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)

d=list(zip(a,names))#* for (10:'harini),(40:'priya')
print(*d)'''

#enumarate- we can give counter to the collection
'''names=["hema","vasu","ram","sita","geeth"]
for i in range(len(names)):
print(i,names[i])#without enumarate
b=dict(enumerate(names))
print(b)

b=dict(enumerate(names,100))
print(b)

b=list(enumerate(names))
print(b)

b=set(enumerate(names))
print(b)'''

#Task railway ticket
   #ticket=1000
   #gender-female nd male >60 30% <60 50%
'''while True:
    def railway_ticket():
         ticket=1000
         gender=input("enter the gender")
         age=int(input("enter the age"))
         if gender=="male":
             if age>=60:
                 print("senior citizen")
                 ticket=ticket-30/100*ticket
                 print(ticket)
             elif age<60:
                 print("normal citizen")
                 print(ticket)
         elif gender=='female':
             if age>=60:
                 print("senior citizen")
                 ticket=ticket-50/100*ticket
                 print(ticket)
             elif age<60:
                 print("normal citizen")
                 ticket=ticket-30/100*ticket
                 print(ticket)
    railway_ticket()'''
                 
#ANNONYMOUS FUNCTIONS are name less function we use keyword called as lambda to create annonymous functions           
#write a function to calculate 2*x+5 where x=5

'''def calculate():
    x=5
    print(2*x+5)
calculate()'''

#a=lambda arg:expression
'''a=lambda x:2*x+5
print(a(5))'''

#runtime
'''a=int(input("value"))
b=lambda x:2*x+5
print(b(a))'''

#Task
'''a="codegnan"
b=lambda x:a.upper()
print(b(a))'''

'''a="python course"
b=lambda x:a.title()
print(b(a))'''

#multiply
'''a=int(input("enter the value"))    
b=int(input("enter the value"))      
c=lambda a,b:a*b
print(c(a,b))'''

'''a=str(input("enter firstname"))
b=str(input("enter lastname"))
c=lambda a,b:(a+" "b).title()
print(c(a,b))'''

'''a,b=[x for x in input("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''#generaters concept 30/8/25

#filter()
'''a=[10,20,30,40,50,80,23,73,100]
if a%2==0:
 print(a)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''
#(),[],{}

'''a=[[],{},set(),{}," ",None,3,3.8,"python",7+9j,True,False]
b=list(filter(None,a))
print(b)'''

#map()-each object from acollection and forms a new collection
'''a=[2,5,7,9,10,20,30,80]
b=[1,9,20,50,60,4,25,80]#2>1=2,5<9=9,7<20=20,9<50=50 #extra element take as none
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)'''

'''a=input("data1")
b=input("data2")
print(a+b)

a,b=input("enter the data").split(",")
print(a+b)

a,b=[x for x input("enter the names").split(",")
print(a+b)

a,b=map(str,input("enter the data").split(","))
print(a+b)

a=int(input("a value"))
b=int(input("b value"))
print(a+b)

a,b=[int(x) for x in input("enter the values").split(",")]
print(a+b)

a,b=int(input("enter the values").split(","))
print(a+b) #error'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)

a=tuple(map(int,input("values").split(",")))
print(a)
print(type(a))

a=list(map(int,input("values").split(",")))
print(a)
print(type(a))

a=set(map(int,input("values").split(",")))
print(a)
print(type(a))'''


'''a=input("enter the key and values")
b=dict(i.split(":") for i in a.split(","))
print(b)'''

'''a=list(map(str,input("values").split(",")))
print(a)
print(type(a))'''

'''a=list(map(eval,input("values").split(",")))
print(a)
print(type(a))'''











        




        











      
      
