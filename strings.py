Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#len
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
e=" i am in vijayawada"
len(e)
19
# number of repaeted words nd character in given string is called COUNT
#COUNT
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
#so we use
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(" ")
3
a.count("")
28
#find a string
a="python"
a[1]
'y'
b="hello"
b.find("l")
2
b[2:4]
'll'
a.find("k")
-1
# it is opp to slicing in slicing you get number here you get character
#ESCAPE SEQUENCES
#\n-> new line
#\t-> tab space
a="name\nmailid\tmobileno\ncollege\tbranch"
a
'name\nmailid\tmobileno\ncollege\tbranch'
print(a)
name
mailid	mobileno
college	branch
b="name=Geethika\nmailid:geethikamunikoti369@gmail.com\tmobileno:8233773328\ncollege:vrsec\tbranch:CSE"
print(b)
name=Geethika
mailid:geethikamunikoti369@gmail.com	mobileno:8233773328
college:vrsec	branch:CSE
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python java"
b.replace("p","c")
'cython java'
c="wait until you succeed"
c.replace("wait","work",1)
'work until you succeed'
c.replace("wait","work",1)
'work until you succeed'
#upper()
a="code"
a.upper()
'CODE'
#lower()
b="HELLO"
b.lower()
'hello'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c[0] .upper()
'P'
c . capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.title()
'I Am In Class'
'I Am In Class'
'I Am In Class'
e.capitalize()
'I am in class'
a="code"
a.isupper()
False
a.islower()
True
a.isdigiti
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a.isdigiti
AttributeError: 'str' object has no attribute 'isdigiti'. Did you mean: 'isdigit'?
a.isdigit()
False
a.isalpha()
True
b="code course"
b.isalpha()
False
c="codecourse"
c.isalpha
<built-in method isalpha of str object at 0x000001CFAE678AF0>
c.isalpha()
True
d="1245"
d.isdigit()
True
d="1,2,3,4"
d.isdigit()
False
#allnum
a="geethika@123"
a.isalnum()
False
a="geethika123"
a.isalnum()
True
b="geethika.123"
b.isalnum()
False
a="data science"
a.startswith("d")
True
a.endswith("e")
True
#strip()
#leftstrip(),rstrip()
a="      pooja   "
a.strip()
'pooja'
a.lstrip()
'pooja   '
a.rstrip()
'      pooja'
#no middle spaces applies
#split()
a="python java c++"
a.split()
['python', 'java', 'c++']
b="i love python"
b.split()
['i', 'love', 'python']
b.spliti()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    b.spliti()
AttributeError: 'str' object has no attribute 'spliti'. Did you mean: 'split'?
b.split(i)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    b.split(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
b="html","css","js"
#join()
"'.join(b)
SyntaxError: unterminated string literal (detected at line 1)
"".join(b)
'htmlcssjs'
" ".join(b)
'html css js'
"k" .join(b)
'htmlkcsskjs'
c="python"
"k".join(c)
'pkyktkhkokn'
#cancatination or joining two strings
a="code"
b="gnan"
print(a+b)
codegnan
print(a+" "+b)
code gnan
c="geethika
SyntaxError: unterminated string literal (detected at line 1)
a="geethika"
b="munikoti"
print(a.title()+" "+b.title())
Geethika Munikoti
print((a+" "+b).title())
Geethika Munikoti
#formating
a=5
b=6
print(a+b)
11
>>> print("the sum is",a+b)
the sum is 11
>>> city="vijaya"
>>> print("city is",city)
city is vijaya
>>> print("the sum is ,a+b")
the sum is ,a+b
>>> #format()
>>> a="motu"
>>> b="pathulu"
>>> print("hy {}{}" .format(a,b))
hy motupathulu
>>> print("hello {} {}" .format(a,b))
hello motu pathulu
>>> print("hello {}\n{}" .format(a,b))
hello motu
pathulu
>>> pathulu
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    pathulu
NameError: name 'pathulu' is not defined
>>> print("hello {}\nhello{}" .format(a,b))
hello motu
hellopathulu
>>> a="sita
SyntaxError: unterminated string literal (detected at line 1)
>>> a='sita"
SyntaxError: unterminated string literal (detected at line 1)
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {b}")
hello sita ram
>>> print(f"hello {a} hello {b}")
hello sita hello ram
>>> print(f"hello {a}\nhello {b}")
hello sita
hello ram
a="1234"
a.isnumber()
a
