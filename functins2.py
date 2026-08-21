#split bill
'''def splitbill():
    a=int(input("enter the no.of friends"))
    b=int(input("enter the amount"))
    print("per head bill is",b//a)
splitbill()'''
#using f string split bill
'''def splitbill():
    a=int(input("enter the no.of friends"))
    b=int(input("enter the amount"))
    c=b//a
    print(f"per head bill is {c}")
    print("per head bill is{}"
          .format(c))
splitbill()'''

#keywords and positional arguments
'''def details(id,name,mailid): #decalring functional arguments
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")#calling positional arguments
details(id=20,name="ketu",mailid="m@gmail.com")
details(id=69,name="rahu",mailid="r@gmail.com")
details(40,"geethika","geethika@gmail.com")
details("ram","r@gmail.com","88")
details(name="lahari",mailid="b@gmail.com",id=60)'''

#default arguments
#def is a keyword
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''

'''def Grocery(item="ghee",price):
    #not def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''

#cake,price,quantity
'''def deserthouse(cake,price,quantity): #decalring functional arguments
    print("cake is %s" %cake)
    print("price is %f" %price)
    print("quantity is %s" %quantity)
deserthouse("rasmalia",600,"1kg")
deserthouse("choco",670,"1kg")
deserthouse("butterscotch",570,"1kg")'''
# * argument (* is used unpack the elements)
'''a=[10,20,30,40]
print(a)
print(*a)'''

'''a=(10,20,30,40)
print(a)
print(*a)'''

'''a={10,20,30,40}
print(a)
print(*a)'''

'''a={"year":2026,"month":"july"}
print(a)
print(*a)'''


'''a,b,c=6,7,9
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8
print(a)
print(*b)
print(c)'''
'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''
'''a,b,c="cod"
print(a)
print(b)
print(c)'''

a,b,*c="codegnan"
print(a)
print(b)
print(c)


      



















    
