Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#vairable
print(5+5)
10
a=5
b=7
print(a+b)
12
a=8
print(a)
8
@=7
SyntaxError: invalid syntax
$=8
SyntaxError: invalid syntax
_d=7
print(_d)
7
-=7
SyntaxError: invalid syntax
print(_)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(_)
NameError: name '_' is not defined. Did you mean: '_d'?
_=8
print(_)
8
if=60
SyntaxError: invalid syntax
first name="pooja"
SyntaxError: invalid syntax
first_name="pooja"
print(first_name)
pooja
firstname="geethika"
print(firstname)
geethika
a=2,8,6,7,8,
print(a)
(2, 8, 6, 7, 8)
a,b,c=1,2,3
print(a,b,c)
1 2 3
a,b,c=1,2,3,4,7
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a,b,c=1,2,3,4,7
ValueError: too many values to unpack (expected 3, got 5)
>>> unpacking
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    unpacking
NameError: name 'unpacking' is not defined
>>> #unpacking and packing
>>> a,b,c=(6,7,8)
>>> print(a,b,c)
6 7 8
>>> #delete keyword
>>> a=7
>>> print(a)
7
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> #usecase
>>> fname="pooja"
>>> lname="ch"
>>> print(fname+lname)
poojach
>>> print(fname+ lname)
poojach
>>> print(fname+" "+lname)
pooja ch
>>> print(fname,lname)
pooja ch
>>> #Case Sensitive
>>> name="geeth"
>>> print(name)
geeth
>>> NAME="geeth"
>>> print(NAME)
geeth
>>> Name="geeth"
>>> print(Name)
geeth
