Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a**b)
16
print(a//b)
0
print(a/b)
0.5
print(a%b)
2


#ASSIGNMENT OPERATORS
a=
SyntaxError: invalid syntax
a=3
b=5
a+=b

b+=a
#comparision
a=6
b=8
a<b
True
b>a
True
a<=b
True
b<=a
False
a>b
False
b<a
False
#logical
a=4
b=8
a<b and b>a
True
a!=b or a==b
True
a!=b or a==b
True
True
True
a!=b and a==b
False
not true
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not false
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    not false
NameError: name 'false' is not defined. Did you mean: 'False'?
not True
False
not False
True
#identify
a=6
type(a) is int
True
type(a) is not int
False
b=2.4
type(b) is float
True
type(b) is string
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    type(b) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(b) is str
False
type(b) is bool
False
type(b) is complex
False
type(b) is not str
True
type(b) is not complex
True
type(b) is not bool
True
#membership
a=1,2,4,7,8,5
5 in a
True
5 not in a
False
9 in a
False
9 not in a
True
7 not in a
False
7 in a
True
2 not in a
False
2 in a
True
4 in a
True
1 in a
True
8 in a
True
#membership
b="python","c"
c in b
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    c in b
NameError: name 'c' is not defined
>>>  "c" in b
...  
SyntaxError: unexpected indent
>>> "c" in b
True
>>> "python" in b
True
>>> "c" "python" in b
False
>>> "python","c" in b
('python', True)
>>> #so thats why 2 values are not checked at a time
>>> #bitwise
>>> a=5
>>> b=9
>>> a|b
13
>>> a=4
>>> b=2
>>> a&b
0
>>> a=6
>>> -(a+1)
-7
>>> b=-9
>>> ~b
8
>>> -(-9+1)
8
>>> #xor
>>> a=8
>>> b=10
>>> a^b
2
>>> #right shift left shift
>>> a=3
>>> a>>3
0
>>> a=6
>>> a<<3
48
