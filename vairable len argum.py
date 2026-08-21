#vairable length argument
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[2,3,4,5,6,7]
check(*b)
c={6,7,8,9,10}
check(*c)
d={"name":"pooja","city":"vij"}
check(*d)'''

#kwargs(**)
'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "name":["sai","siva","ravi"],
         "status":["p","a","p"]}'''
'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "name":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''

#both * and ** usage
'''def final(*a,**b):
    d=3#creating a vairable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6.2)
final(*data)
details={"idnos":[10,20,30],
         "name":["pooja","priya","preethi"],
         "status":["p","a","p"]}
final(**details)
final(*data,**details)'''

#max(),min(),sum()
print(max(5,7,9,10,20,40))
print(min(6,7,8,9,10,23,6))
a=5,6,7,8
print(sum(a))





        


