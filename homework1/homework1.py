#File: homework1.py
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
5) 
'''
#5) 

n = set("Danieliscool")
print(n)
print(type(n)) #n is a set, an unordered collection of data types that is iterable, mutable, and has no duplicate elements.

# --- Booleans ---

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

print(bool(1+1))

print(bool(type(1)==type(0.1)))

"""
1) I've noticed that a lot of the values that are false are when the function has Nothing, Nonetype values in the function.
2) I think something that shocked me somewhat was print(bool(True or False)) because I wasn't sure whether it preferred one or the other.
3) print(bool(1+1). This returned true because it is not an 
4) print(bool(type(1)==type(0.1))) returns False because 1 is an integer and is not the same as a float
"""

# --- Operators ---

print(10 + 5) # 15, + performs addition

print(10 - 5) # 5, performs subtraction

print(2 * 4) # 8, performs multiplication

print(6 / 3) # 2.0, performs division

print (5 % 2) #1, Divides and outputs the remainder

print(3 ** 2) #9, expondent multiplication

print(15 // 2) #7, performs floor division (division and round the result down to the nearest whole number)

print(5 == 2) #False, performs comparison

print(10 != 10) #False, comparison using "not equal to"

print(2 < 5) #True, comparison using "less than"

print (12 > 5) #True, comparison using "greater than"

print (5<= 6) #True, comparison using "less than or equal to"

print(1 >= 10) #False, comparison using "greater than or equal to"

# --- Assignment Operators ---

x = 5

x += 5 

print(x)

x -= 4

print(x)

x *= 3

print(x)

'''
1) The "and" operation multiple boolean conditions. It returns true if every condition it connects is true An expression that results in True can be "print(True and True)". An expression that results in False can be "print(True and False)
2) The "or" operation evaluates two expressions and returns a result based on their truthiness. An expression that results in true can be "print(True or False)". An expression that results in False can be "print(False or False")
3) The "not" operator in python performs boolean negation. It inverts the truth value of a boolean expression. An expression that results in True can be "print(not(False))". An expression that results in False can be "print(not(True))
'''

"""
1) / is true division, where it results in a floating number, even if the operands are integers and their results are whole numbers. // is floor division, meaning it rounds the largerst integer less than or equal to the actual quotient. 
2) % is modulo, which returns the remainder of a division. // is floor division, so it gives you a rounded quotient less than or equal to the true quotient.
3) You would use the modulo operator, %, since it gives you the remainder of a quotient. For example, 5 % 2 would give you 1, since 2 goes into 5 2 times with a remainder of 1
4) Assignment operators are used to assign values to variables. Arithmetic assignment operators allow you to update a variable in your code.
"""

# --- Strings ---

my_string = "hello"

my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) #Prints: h
print(my_string[1]) #Prints: e
print(my_string[2]) #Prints: l
print(my_string[3]) #Prints: l
print(my_string[4]) #Prints: o
print(my_string[-1]) #Prints: o
print(my_string[1:3]) #Prints: el
print(my_string[0:5:2]) #Prints: hlo
print(len(my_string)) #Prints the amount of characters in my_string

my_string += "goodbye"
print(my_string)

my_string *= 7
print(my_string)

'''
1) Slicing is used to extract a subsequence or a portion of a sequence (String, list, tuple). We sliced by doing [1:3] & [0:5:2]

4) The difference between the two is that the second one is an f string. what this does is that the {name} inside the strings gets replaced with the value of the name variable, which results in a single string.
'''
name = "Oski"
print("Hello, my name is", name) #Prints: Hello, my name is Oski

name = "Oski"
print(f"Hello, my name is {name}") #Prints: Hello, my name is Oski

# --- Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# list directory contents
# Example: ls

# ls -a
# list all files, including hidden files
# Example: ls -a

# mkdir
# Make new directories (folders) in the file system
# mkdir python_decal_fall25

# cat
# Prints out all the contents of a file
# cat datatypes.py

# pwd
# Print the current working directory
# pwd

# cd ..
# Moves up to a parent directory
# cd ..

# cd .
# Means "change directory to the current directory.", so it essentially does nothing
# cd .

# cd ~
# Changes the current working directory to the user's home directory. 
# cd ~

# cp
# creates a duplicate of a specified source file or directory at a designated destination.
# cp <source_file destination_file>

# mv 
# Used to move or rename files, directories, or symlinks within a Git repository.
# mv file.txt path/to/new/location/

# rm
# Used to remove files from a Git repository
# rm old_notes.txt

# Clear
# Used to remove untracked files from your working directory
# clear -df

# grep
# Allows searching for patterns within files tracked by a Git repository
# grep "search-term"

# --- Questions ---

# whoami
# Displays the username of the current logged-in user.
# whoami

# echo
# Prints text or variables to the terminal.
# echo "Hello World"

# head
# Prints the first 10 lines of a file by default.
# head datatypes.py

#2) ls list all visible files, ls -a list all files, including hidden ones (such as .. and .)
#3) A hidden file is a file or folder on your computer that is not displayed by default in a file explorer
#4)
'''
ls -1
Displays a detailed "long list" of attributes, including permissions, owner, group, size, and modification date.

ls -t
Sorts the listed files by modification time, showing the most recently modified first.

ls -r
Reverses the sorting order. For example, when used with -t, it shows the oldest files first.

'''
