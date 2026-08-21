Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=["python","c","c++"]
a.append("java")

a.append("java")

a
['python', 'c', 'c++', 'java', 'java']
a.append("html","css")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.append("html","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["html","css"])
a
['python', 'c', 'c++', 'java', 'java', ['html', 'css']]
#extend()
a=["html","css","js"]
a.extend(["python","java"])
a
['html', 'css', 'js', 'python', 'java']
#insert
b=["vij","hyd","vzg"]
b.insert(l,"chennai")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b.insert(l,"chennai")
NameError: name 'l' is not defined
b.insert(l,"chennai")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b.insert(l,"chennai")
NameError: name 'l' is not defined
b.insert(1,"chennai")
b
['vij', 'chennai', 'hyd', 'vzg']
a=["apple","banana","grapes"]
a.index("grapes")
2
a.copy()
['apple', 'banana', 'grapes']
b=a.copy()
b
['apple', 'banana', 'grapes']
a.count("apple")
1
len(a)
3
d="apple"
len(d)
5
e=["apple"]
len(e)
1
a=["mango","kiwi","dragon","berry"]
a.sort()
a
['berry', 'dragon', 'kiwi', 'mango']
b=[1,4,9,7,8]
b.sort()
b
[1, 4, 7, 8, 9]
#sort means order.
#reverse
a=["ds","ai","ml"]
a.reverse()
a
['ml', 'ai', 'ds']
b=[3,6,7,4,9]
b.reverse()
b
[9, 4, 7, 6, 3]
#pop
a=["black","white","red"]
a.pop()
'red'
a
['black', 'white']
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.pop(2)
IndexError: pop index out of range
a.pop(1)
'white'
a
['black']
a.pop("black")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.pop("black")
TypeError: 'str' object cannot be interpreted as an integer
a.remove("black")
a
[]
#HERE POP IS DELETED ONLY when number given remove only takes away the character
a=["ap","ts","ka"]
a.clear()
a
[]
b=[]
b.append("geethu","vij","ts")
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    b.append("geethu","vij","ts")
TypeError: list.append() takes exactly one argument (3 given)
b.append["geethu","vij","ts"]
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    b.append["geethu","vij","ts"]
TypeError: 'builtin_function_or_method' object is not subscriptable
b.append("pooja")

b.append("pooja")
b
['pooja', 'pooja']
['pooja', 'pooja']
['pooja', 'pooja']
b.append("harini")
b
['pooja', 'pooja', 'harini']
a=[10,20,30,40,"code"]
a.extend("code")
a
[10, 20, 30, 40, 'code', 'c', 'o', 'd', 'e']
a.extend(["code"])
a
[10, 20, 30, 40, 'code', 'c', 'o', 'd', 'e', 'code']
#TUPLE
#TUPLE
#TUPLE
a=(4,6,7,"python",8+9j,True,False)
print(a)
(4, 6, 7, 'python', (8+9j), True, False)
type(a)
<class 'tuple'>
a.index(8+9j)
4
len(a)
7
a.count(True)
1
#tuples are immutable cannot be changed nd list are mutable
#list[]
#list[]
#################SETS()
a={4,7.8,"POOJA",5+9j,True,False}
print(a)
{False, True, (5+9j), 4, 'POOJA', 7.8}
type(a)
<class 'set'>
b={7,9,4,8,9,2}
print(b)
{2, 4, 7, 8, 9}
#add()
a={4,5,6,7,8}
a.ad(15)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.ad(15)
AttributeError: 'set' object has no attribute 'ad'. Did you mean: 'add'?
a.add(15)
a
{4, 5, 6, 7, 8, 15}
#issubset()
a={3,4,5,6,7,8,9}
b={6,7,8,9}
b.issubset(a)
True
a.issubset(b)
False
#b is part of a so b is subset
a={5,6,7,8,9,10}
b={6,7,8}
b.issuperset(a)
False
a.issuperset(b)
True
#here a is superset
#union two sets merged into single set is CALLED UNION
a={3,4,5,6,7}
b={1,2,3,4,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
#intersection
a={3,4,5,6,7}
b={1,2,3,4,7}
a.intersection(b)
{3, 4, 7}
b.intersection(a)
{3, 4, 7}
#gives the common values in a&b
#difference
a={7,8,9,10,11,12}
b={8,9,10,11,12,13,14,15}
a.difference(b)
{7}
b.difference(a)
{13, 14, 15}
#pluck out different value in a nd pluck out  different value in b
#update
a={2,3,4,5,6}
b={1,4,5,6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#symmetric difference
a={2,3,4,5,6,7,8}
b={1,4,6,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 3, 5, 7, 9, 10, 11}
b.symmetric_difference(a)
{1, 2, 3, 5, 7, 9, 10, 11}
#it deletes similar values
a={4,5,6,7,8,9}
b={1,2,3,4,5,6,10}
a.difference_update(b)
a
{7, 8, 9}
a
{7, 8, 9}
b.difference_update(a)

b.difference_update(a)

b
{1, 2, 3, 4, 5, 6, 10}
b
{1, 2, 3, 4, 5, 6, 10}
a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.interesction_update(b)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a.interesction_update(b)
AttributeError: 'set' object has no attribute 'interesction_update'. Did you mean: 'intersection_update'?
a.intersection_update(b)
a
{8, 5, 6, 7}
a
{8, 5, 6, 7}
b.intersection_update(a)
b
{8, 5, 6, 7}
b
{8, 5, 6, 7}
a={11,12,13,14,15,16}
b={13,14,15,16,17,18,}
a.symmetric_difference_update(b)

b
{16, 17, 18, 13, 14, 15}
a
{17, 18, 11, 12}
a
{17, 18, 11, 12}
b.symmetric_difference_update(a)
b
{16, 11, 12, 13, 14, 15}
>>> a.remove(6)
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    a.remove(6)
KeyError: 6
>>> a={3,4,5,6,7,8}
>>> a.pop()
3
>>> a
{4, 5, 6, 7, 8}
>>> a.remove(6)
>>> a
{4, 5, 7, 8}
>>> a
{4, 5, 7, 8}
>>> a={10,20,30,40}
>>> a.copy()
{40, 10, 20, 30}
>>> b
{16, 11, 12, 13, 14, 15}
>>> b=a.copy()
>>> b
{40, 10, 20, 30}
>>> a.discard(20)
>>> a
{40, 10, 30}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(100)
>>> b
{100}
>>> a={2,3,4,5,6}
>>> b={6,7,8,9,10}
>>> a.isdisjoint(b)
False
>>> c={10,20,30,40}
>>> d={50,60,70,80}
>>> c.isdisjoint(d)
True
