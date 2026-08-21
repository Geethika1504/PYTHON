#exception handling
'''try-instructions from which we are expecting the exceptions
except-exception are raised in try block it will be handle
by this block
else-no exception(optional)
finally-always it will display '''
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exception")
    finally:
        print("programs ends")'''

#file handling
'''a=open("geeth.txt","w")
a.write("python full stack")
a.close()'''

#append()
'''a=open("geeth.txt","a")
a.write("\tgeeth")
a.close()'''

#runtime
'''a=open("geeth.txt","w")
b=input("data")
a.write(b)
a.close()'''

'''a=open("geeth.txt","w")
a.write(input("data"))
a.close()'''

#readlines()
'''a=open("geeth.txt")
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.readlines())#t will display in list with \n(new line)
print(a.read(13))#t will display n0.of characters'''

#writelines()-it makes every object side by side
'''a=open("priya.txt","w")
b=["hari","kesav","ketan","harsh"]
a.writelines(b)
a.close()'''

'''a=open("priya.txt","w")
b=["hari","kesav","ketan","harsh"]
a.writelines("\n".join(b))
a.close()'''


'''a=open("conditions.py")
print(a.read())'''

a=open("C:\\Users\\vasu\\Desktop\\python\\MODULE.py")
print(a.read())








       
        
        
        
    
