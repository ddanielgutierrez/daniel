#File: homework1. py
# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) #a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) #b is a Float, a number with decimals

c = 3j
print (c)
print (type(c)) #c is a complex number

d = "hello"
print(d)
print(type(d)) #d is a string, words or text

e = [1, 2, 3]
print(e)
print(type(e)) #e is a list, an ordered collection of data

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) #f is a dictionary, a collection of data values

g = (1, 2)
print(g)
print(type(g)) #g is a tuple, an ordered collection of data. The difference between a tuple and a list is that tuples are immutable (Cannot be modified after it is created)

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) #h is a list

i = True
print(i)
print(type(i)) #i is a boolean (True), one of two built in values

j = None
print(j)
print(type(j)) #j is NoneType, represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) #k is a list

l = str(14)
print(l)
print(type(l)) #l is a string

m = 1e4
print(m)
print(type(m)) #m is a float

'''
1) I found 9 different datatypes
2) Integer, Float, Complex Number, String, List, Dictionary, Tuple, Boolean, and Nonetype
3) d & l, h & k, b & m
4) l is a string and not an integer because we used the string function on 14, converting 14 from an integer to a string
'''
#5)

n = set("Danieliscool")
print(n)
print(type(n)) #n is a set, an unordered collection of data types that is iterable, mutable, and has no duplicate elements.

print(10 > 9) #True, 10 is greater than 9

print(10 == 9) #False, 10 is not equal to 9

print(10 <= 9) #False, 10 is not less than or equal to 9

print(bool("abc")) #True, any non-empty string is considered "Truthy"

print(bool(123)) #True, 123 is an integer

print(bool(["apple", "cherry", "banana"])) #True, any non-empty list is considered "Truthy"

print(bool(True)) #True, boolean function converts a value to its boolean representation, True is already Truthy.

print(bool(False)) #False, Reason above

print(bool(0)) #False, 0 is considered a "Falsey" value

print(bool("")) #False, empty string equates to "Falsey" value

print(bool(" ")) #True, nonempty string

print(bool(())) #False, empty tuple is considered "Falsey"

print(bool([])) #False, empty list is considered "Falsey"

print(bool({})) #False, empty dictionary is considered "Falsey"

print(bool(True and False)) #False, the "and" operations indicates both values must be true.

print(bool(True and True)) #True, same reason as above

print(bool(False and False)) #False, both statements are false

print(bool(True or False)) #True, the "or" statements allows one or the other, making it true

print(bool(True or True)) #True, both options are true

print(bool(False or False)) #False, both are false

print(bool(not(False))) #True, the "not" makes it the opposite of the boolean value, so opposite of false is true

print(bool(not(True))) #False, Opposite of true is false

"""
1) I've noticed that a lot of the values that are false are when the function has Nothing, Nonetype values in the function.
2) 
"""
