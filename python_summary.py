x,y=3,5
print(x)#new line  """ multi line comment """"
x=[1,2,3] #list []
x.append("hi")
print(x)
name = input("Enter your name: \n") #input return string to read int: x=int(input("Enter age: ")) if input not int error
print("hello", name)#same line sep by " "
y = int(input("Enter num1: "))#if intxx error when arrive to this line as he search for func with this name but if syntax error program will not run
#print(10, 20, sep=' - ', 30) #Syntaxerror Positional arguments 30 cannot appear after keyword arguments sep
y=3
l=[1,2,3,4,5,y]
print(l)
y=99
print(l)#l=[1,2,3,4,5,3] bya5od el kema bta3et y lma deftha ll list elly 3mlha lama 3mlt l=[1,2,3,4,5,y] w y=3
L=[1,2,3,4]
#print(l,L)#different

import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)#file=open('Testfile.txt', 'w')

#input().split(separator, maxsplit)
x, y = input("Enter two values sep by space: ").split()#default separator is space
print("First num {} and sec {}".format(x, y),end=".")# ..num 54 and sec 78
x, y = [int(x) for x in input("Enter two values: ").split()]
x = list(map(int, input("Enter multiple values: ").split()))
print
#-----------------if else-----------------
num = 34
if(num>12):
    print("Num1 is good")
elif(num>35):
    pass#do nothing
else:
    print("Num2 is great")
#-----------------for loop-----------------
#for step in range(5):
#    print(step)#0-4
#-----------------while loop-----------------

#-----------------function-----------------
def hello():
    print("hello")
hello()
#------
#if __name__=="__main__":
#    Main()
#--------------
import math#math module
#print( math.fabs(num) )#absolute value float 34.0      type(num)

#
"""
POWER **
// floor division
% REMAINDER
/ FLOAT DIVISION 5/1=5.0  we can overload the division operator to div true/false msln
!= NOT EQUAL
not x , X AND OR Y
Bitwise AND	x & y  NOT ~x   right shift	x>>3  OUTPUT IS INT 3ADE
a+=b
print (-5//2)  -3  (-5.0//2) -3.0
----
dentity Operators:
is zay == kda         True if the operands are identical  , is not
Membership Operators:
in            True if value is found in the sequenc , not in
----
Ternary operators " conditional expressions"
min = a if a < b else b
-------------
print( (b, a) [a < b] )  (if_test_false,if_test_true)[test]
print({True: a, False: b} [a < b])
------
# concatenate two strings
print("Geeks"+"For")

# Repeat the String
print("Geeks"*4)

operator overloading
    class A:
    def __init__(self, a):
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")
 
print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2))
print(A.__add__(ob3,ob4))
#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))
-------------
# second item (True) and will return True.
print (any([False, True, False, False])) zay or
all -> and

print (operator.add(a, b)) # a + b import operator

for i in range(0,10): 0-9

dict1={1:'Geeks',2:'For',3:'Geeks'}
"""
a,b=3,3
#print(a is b)#true same id

"""
Strings are immutable,
s='''This is a string''' or 'dfs' or "sds"
# Creating String with triple Quotes allows multiple lines
String1 = '''Geeks
            For
            Life'''


list mutable t2der t8yr feha

# Declaring a list
l=list() #or l=[]
L = [1, "a" , "string" , 1+2] ->1+2=3
print L
#Adding an element in the list
L.append(6)    
print L
#Deleting last element from a list
L.pop()
print L
#Displaying Second element of the list
print L[1]

tuple immutable
tup = (1, "a", "string", 1+2)  #tup[1]="a" 



i = 1
while (i < 10):
    print(i)
    i += 1

s = "Hello World"
for i in s:
	print(i)

"""
# tup = (1, "a", "string", 1+2)
# tup=(1,2,3,4,5,6,7,8,9,10)
# print(tup[1])#3adee
# tup[1]=3#TypeError: 'tuple' object does not support item assignment

# String1 = "Hello, I'm a Geek"
# print("Initial String: ")
# print(String1)
 
# # Updating a String
# #String1[3]= 'p' #error
# String1 = "Welcome to the Geek World"#3adee
# print("\nUpdated String: ")
# print(String1)
#del String1 delete string
s="hi \"Geek\" bro"#hi "Geek" bro
String1 = "{0:.2f}".format(1/6) #0.17
"""
Unlike Sets, the list(and tuple) may contain mutable elements.
len(List2) 3dd el elements
List.insert(0, 'Geeks') 0 index append fl a5er bs
List.extend([8, 'Geeks', 'Always']) add multiple elements to end zy append bs kza wa7ed

List Comprehension
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]  [ expression(element) for element in oldList if condition ]

tup = tuple(list1)
error  if a list and a tuple are combined.
Tuple3 = Tuple1 + Tuple2
Tuple3 = Tuple1 * 3
Tuple1[0] = 4 #TypeError: 'tuple' object does not support item assignment
del Tuple1
Tuple1[::-1] reverse
"""
x=3
tup=(x,3)
x=4
print(tup)#(3, 3)

"""
Set is unordered different data types ,iterable, mutable, has no duplicate.
var = {"Geeks", "for", "Geeks"}#set
Sets are implemented using a dictionary and hash table. sets are unordered, we cannot access items using indexes.
search in set o(1)
"""

# typecasting list to set
myset = set(["a", "b", "c"])
print(myset)

# Adding element to the set
x=6
myset.add(x)
print(myset)
x=7
print(myset)#6

myset = {"Geeks", "for", "Geeks"}#{"Geeks", "for"}
myset = {"Geeks", "for", 10, 52.7, True}
# values of a set cannot be changed
#myset[1] = "Hello"#error We can only add or delete items in the set.
print(myset)
#frozen_set = frozenset(["e", "f", "g"]) you cannot add or remove elements from a frozenset.
#set3 = s1.union(s2) or s1|s2/////////set1.intersection(set2) or set1 & set2  set1.difference(set2) or set1 - set2
#set1.clear()#remove all elements
list1=[1]
#s1={list1,2} error unhashable type: 'list' 3shan list mutable w el set bta5od 7agat immutable bs 3shan el hash table
#x in s	O(1) avg
#-------------
#Dictionary
"""
Dictionary keys values zy el map..O(1) access
keys can't be repeated and must be immutable.
"""
#d=dict({1:'a', 2:'b'}) or d=dict([ or '{' (1,'a'), (2,'b')] or'}') both: {1: 'a', 2: 'b'}
Dict = {2: 99, 1: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}#nested dictionary msh byrtbhom hya zy ma t7otha
Dict[2] = 'hi'#update
Dict['Name'] = 'For'#add
Dict['Value_set'] = 2, 3, 4#add set 3ade mn8er (2, 3, 4)
print(Dict)
del(Dict[1]) 
print(Dict[3]['A'])#Welcome
print(Dict.get(3))#{'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}
print(Dict.keys())#dict_keys([2, 3, 'Name', 'Value_set'])
dict2 = Dict.copy()
#Dict.clear()#remove all elements
#Dict.pop(2) remove specific element
#--------
l=[54]
x=4

l2=l #same id
y=x

l2[0]=5
y=88
print(l,x)#5

#-----array
#n array same tybe stored contiguous memory locations zy list
import array as arr
# creating an array with integer type
a = arr.array('i', [1, 6, 6])
a.insert(1, 4)#insert(index, value)
#print(a[7])#IndexError: array index out of range
#a[7]=3#IndexError: array assignment index out of range
#arr.remove(6)#remove first occurance of 6 in array error if not found
b=a.pop(2)#remove element at index 2
#indexx=a.index(8)#return index of first element with value 8 error if not found
#count = my_array.count(2)

print(a,*a)#rray('i', [6, 4, 1])       1 4 6

a.extend([6,7,8,9,10])

#--------funs
"""
once we have a default argument, all the arguments to its right must also have default values.
"""
def add(num1: int, num2: int) -> int:
    """ doc stringAdd two numbers"""
    num3 = num1 + num2
    return num3
num1,num2=1,2
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
print(add.__doc__)

#! *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#! *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(first='Geeks', mid='for', last='Geeks')

# !variables of nested functions
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
    f2()
f1()#I love GeeksforGeeks

#!-------
def myFun(arg1, *argv):
	print("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#!-------
def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)#kwargs['key'] its dictinary
# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

#!Anonymous Functions lambda
def cube(x): return x*x*x
cube_v2 = lambda x : x*x*x
print(cube_v2(2))#8
#fun name = lambda arguments : expression"return value ya3ne"
#return of lambda is a function object
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(20))

y=44
def fun(z):#if passed is list or dict the passed list will be changed
    z=3#z[0]=4 this change the passed list,,, 
    #z=[3,4] this create a new list so passed list will not change,,,same like vaiables z=3 is new variable.0
fun(y)
print(y)#44




d=4
j=d
print(id(d),id(j))#same
j=5
print(id(d),id(j))#different
j=4
print(id(d),id(j))#same

#-----------------
# closures
def outerFunction(text):
 
    def innerFunction():
        print(text)
 
    # Note we are returning function
    # WITHOUT parenthesis
    return innerFunction 
 
if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()#Hey!

    
# Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Nikhil')
p.say_hi()


# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):
	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber
        # d is private instance variable child can't access it
        #self.__d = 42
        #self._d = 42#protected only child can access it

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)#or super().__init__(name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
