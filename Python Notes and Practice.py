# Variable and Variable Types

counter = 100  # An integer
miles = 1000.0  # This is a float naumber.
name = ("Matthew")  # A string.

print(counter)
print(miles)
print(name)

# TheStandardDataTypes
# Numbers
# Strings
# List
# Tuple
# Dictionary

# Types of Numbers
Integer = 10
Float = 0.0
Complex = 3.14j

print(Integer)
print(Float)
print(Complex)

# PythonStrings
str = "Hello World!"
print(str)  # Prints complete string
print(str[0])  # Prints first character of the string
print(str[1])  # Prints second character of the string
# Prints Characters string starting from the 3rd to 5th character
print(str[2:5])
print(str[2])  # Prints string starting from the 3rd character
print(str * 2)  # Prints string two times
print(str + " TEST ")  # Prints concenated string

# PythonLists
list = ['abcd', 786, 2.23, 'john', 70.20000000000003]
tinylist = [123, 'john']
print(list)  # Prints the complete list
print(list[0])  # Prints the 1st element in the list
print(list[1:3])  # Prints elements from 2nd until the 3rd
print(list[2:])  # Prints elements starting from the 3rd element
print(tinylist * 2)  # Prints the lists 2 times
print(list + tinylist)  # prints concentated lists

# PythonTuples
tuple = ('chrono',  456, 4.11, 'SadBoi', 61.3)
tinytuple = (789, 'Yelants')
print(tuple)  # Prints complete tuple
print(tuple[0])  # Prints first element of the tuple
print(tuple[1:3])  # Prints elements in tuples 2nd to 3rd
print(tuple[2:])  # Prints elements starting from the 3rd element
print(tinytuple * 2)  # Prints the tuple 2 times
print(tuple + tinytuple)  # Prints concentated tuples


# PythonDictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'SadBoi', 'code': 2012, 'dept': 'sales'}
print(dict['one'])  # Prints value for 'one' key
print(dict[2])  # Prints value 2 key
print(tinydict)  # Prints complete dicitionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values

# Dictionaries Pop
FullStackDeveloper = {'Name': 'DeAnthony', 'Age': 24, 'Languages': ['Python', 'Django', 'Flask']}
print(FullStackDeveloper['Name'])
FullStackDeveloper.pop('Age')

# Dictionaries Update
d = {1: 'HTML', 2: 'CSS3'}
d1 = {3: 'JavaScript'}

# Updates the value of 2
d.update(d1)
print(d)

d1 = {3: 'JavaScript'}

# adds element with key 3
d.update(d1)
print(d)


# TypesOfOperators
# MathematicalOperators
# ComparisonOperators
# AssignmentOperators
# LogicalOperators
# BitwiseOperators
# IdentityOperators

# Mathematical Operators

# Addition(+)
A = 10
B = 5
print(A+B)

# Multiplication(*)
C = 20
D = 15
print(C*D)

# Subtraction(-)
E = 100
F = 25
print(E-F)

# Division(/)
G = 200
H = 50
print(G/H)

# Modulus(%)
I = 75
J = 4
print(I % J)

# Exponents(**)
K = 2
L = 2
print(K**L)

# FloorDivision(//)
N = 1000
O = 11
print(N//O)

# ComparisonOperators

P = 23
Q = 23
P == Q  # If the 2 opperands are equal, then this condition is true

R = 61
S = 62

R != S  # If the 2 opperands aren't equal, then this condition is true

T = 63
U = 64

T > U  # If the left opperand is greater than the right opperand,This condition becomes true

V = 456
W = 789

# If the right opperand is greater than the left opperand,this condition becomes true.
V < W

X = 290
Y = 291

# If the left opperand is greater than or equal to the right operand, this condition becomes true.
X >= Y

New = 295
Old = 300

# If the right opperand is less than or equal to the left opperand, This condition becomes true.
New <= Old

# Functions


def function1():
    print("This is just my first function")
    print("I coded all damn night")
    print("I gotta find a better job")
    print("God knows we need more than enough in this life")


# Conditionals/If-Else Statements and Booleans
Z = 20021
z = 2001

if (Z < z):
    print("Z is greater than z")
elif(Z == z):
    print("Z is equal to z")
else:
    print("Z is less than z")
    print("is true")
    isTrue = True


# For loops
languages = ["HTML", "CSS3", "PYTHON", "DJANGO", "JAVASCRIPT"]
for x in languages:
    print(x)

# For Loops work for strings as well
for x in "HTML5":
    print(x)

# Wargs and Kwargs
#Args = Arguments Single Asterik
#Kwargs = Keyword Arguments  Double Asterik
#Kwargs = Key,Value Syntax


