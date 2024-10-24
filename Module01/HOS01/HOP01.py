#Variables, Data Types, and User Input
#variable

name = input("Please inter your name: ")
print("Hello " + name)

x = 5
y = "Nam-oy"
print(x)
print(y)

x = 4
x = "Sally"
print(x)

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

x = "Jone"
x = 'Jone'

a = 4
A = "Sally"
print(a)
print(A)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

x,y,z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple","banana","cherry"]
z, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"

print(x, y, z)
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"
def myfunc():
    x =  "fantastic"
    print("Python is" + x ) 

    myfunc()

print("Python is "+ x)   

def myfunc():
    global x
    x = "fantastic"

    myfunc()

print("Python is "+ x)   

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

    myfunc()

print("Python is " + x)   

x = 5
print(type(x))


#datatype

x = "Hello World"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

x = ["apple","banana","cherry"]
print(type(x))

x = ("apple","banana","cherry")
print(type(x))

x = range(6)
print(type(x))

x = {"name":"Jonh","age" : 36}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))



#specific Data Type

x = str("Hello World")
print(x)
print(type(x))

x = int(20)
print(x)
print(type(x))

x = float(20.5)
print(x)
print(type(x))

x = complex(1j)
print(x)
print(type(x))

x = list(("apple","banana","cherry"))
print(x)
print(type(x))

x = tuple(("apple","banana","cherry"))
print(x)
print(type(x))

x = range(6)
print(x)
print(type(x))

x = dict(name = "John" , age = 36)
print(x)
print(type(x))

x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))

x = bool(5)
print(x)
print(type(x))

x = bytes(5)
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)
print(type(x))

x = None
print(x)
print(type(x))

#User Input

username = input("Enter username:")
print("Username is: " + username)

#Multiple assignments

print("\nMultiple assignments\n")
a, b, c = 5, 3.2 , "Hello"
print("a = ",a)
print("b = ",b)
print("c = ",c)

x = y = z = "Python"
print("x = "+x)
print("y = "+y)
print("z = "+z)

#String Functions and Concatenation: 

print("This is your name all caps: " + name.upper())
print("This is your name all caps: " + name.lower())

first_message = "Hi !"
second_message = "How are you?"
full_message = f"{first_message} {second_message}"
print(full_message)

#Numbers and operators

a = 21
b = 10 
c = 0

c = a + b
print("a: {} b: {} a+b: {}".format(a,b,c))

c = a - b
print("a: {} b: {} a-b: {}".format(a,b,c))

c = a * b
print("a: {} b: {} a*b: {}".format(a,b,c))

c = a / b
print("a: {} b: {} a/b: {}".format(a,b,c))

c = a % b
print("a: {} b: {} a%b: {}".format(a,b,c))

a = 2
b = 3
c = a**b
print("a: {} b: {} a**b:{}".format(a,b,c))

a = 10 
b = 5
c = a//b
print("a: {} b: {} a//b:{}".format(a,b,c))

a = 21
b = 10 
if (a == b):
    print("Line 1 - a is equal to b")
else:
    print("Line 1 - a is not equar to b")

if ( a != b):
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")

if ( a < b):
    print("Line 3 - a is less than b")
else:
    print("Line 3 - a is not less than b")

if ( a > b):
    print("Line 4 - a is greater than b")
else:
    print("Line 4 - a is not greater b")

a,b = b,a 

if( a <= b):
    print("Line 5 - a is either less than or equal to b")
else:
    print("Line 5 - a is neither less than nor equal to b")

if ( b >= a):
    print("Line 6 - b is either qreater than or equar to b")
else:
    print("Line 6 - b is neither greater than nor equar to b")


a = 21
b = 10 
c = 0
print("a: {} b: {} c: {}".format(a,b,c))

c = a + b
print("a: {} c = a + b: {}".format(a,c))

c += a 
print("a: {} c += a: {}".format(a,c))

c *= a 
print("a: {} c *= a: {}".format(a,c))

c /= a 
print("a: {} c /= a: {}".format(a,c))

c = 2 
print("a: {} b: {} c: {}".format(a,b,c))

c %= a
print("a: {} c %= a: {}".format(a,c))

c **= a
print("a: {} c **= a: {}".format(a,c))

c //= a
print("a: {} c //= a: {}".format(a,c))


a = 20
b = 10
print('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;
print ("result of AND is ", c,':',bin(c))

c = a | b;
print ("result of OR is ", c,':',bin(c))

c = a ^ b;
print ("result of EXOR is ", c,':',bin(c))

c = ~a;
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;
print ("result of RIGHT SHIFT is ", c,':',bin(c))


var = 5

print(var > 3 and var < 10)
print(var > 3 or var < 4)
print(not(var > 3 and var < 10))

a =10 
b = 20
list = [1, 2, 3, 4, 5]

print("a:", a, "b:", b, "list:",list)

if ( a in list):
    print("a is present in the given list")
else:
    print("a is not present in the given list")

if ( b not in list):
    print("b is not present in the given list")
else:
    print("b is present in the given list")

c=b/a
print("c:", c, "list:", list)
if ( c in list):
    print("c is available in the given list")
else:
    print("c is not avilable in the given list")

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

print(a is c)
print(a is b)

print(a is not c)
print(a is not b)

#While loop
attempts = 0
randomNumber = 5

while attempts <= 2:
    guess = int(input("Please guess a interger between 1 and 6: "))
    
    if (guess == randomNumber):
        print("Congrats, you got it! ")
    else:
        print("Oops, goodluck next time!")
    attempts += 1


