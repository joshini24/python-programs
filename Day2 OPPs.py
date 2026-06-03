"""

#functions

def abc():
    print("hello world")
    print("123")

abc()

def calculator(a,b):
    print(a+b)

calculator(2,3)

#object oriented programming language

#classes, object

class First:
    a = 78

    def method1(self):
        print("Method1")

o1 = First()

print(o1.a)
o1.a=80
print(o1.a)
o1.method1()

#inheritance concept

class Second(First):
    b = 45

    def Method2(self):
        print("Method2")

s1 = Second()
print(s1.b)
print(s1.a)
"""

#modules

import calc

calc.add(11,3)

import calc as K

K.add(11,3)

from calc import add

add(11,3)

from calc import *

add(11,3)
sub(100,0)
mul(1,5)
div(1,1)



