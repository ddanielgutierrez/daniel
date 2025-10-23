# Homework5.py

# 3.1: Vocabulary Review


#1: Git vs. GitHub
# Git is a distributed version control system that allows developers to track changes in their codebase
# Git Hub is a web-based platform that provides hosting and collaboration features on top of Git

#2: Terminal vs. Command Line
# The command line is where you enter commands.
# The terminal provides access to the command line and see the output of your commands.

#3: Local vs. Remote Repository
# Local repository is what is on an indivuals device.
# Remote repository is hosted on a server

#4: Version Control
# Version Control helps keep a complete history of a code by tracking changes.

#5: Staging Area
# a place to make last-minute changes before committing files to your saved history

#6: git add
# Allows you to add changes in your working directory to the staging area

#7: git commit
# Saves the changes from the staging area into your local repository's history

#8: git push
# Uploads your local commits to a remote repository

#9: git status
# Displays the current state of your repository and staging area

#10: git pull
# Integrates changes from a remote repository into your current local branch.

#11: pwd
# Shows your current path to the directory you are currently in

#12: ls
# list the contents of the directory you are in

#13: cd
# cd stands for "Change Directory" which allows you to move in our out of a directory

#14: nano
# Command line text editor

#15: touch
# Creates a file

#16: mv
# Moves file that you choose

#17: rm
# Removes a file that you choose

#18: cat
# "Concatenate": Displays the entire content of a file

# 3.2: A Directory Tree 

#1) pwd
#2) ls
#3) cd ~/python_decal/brianna_repo | git pull origin main
#4) mv homework.py ~/python_decal/judy_decal/homework/
#5) cd ~/python_decal/judy_decal/homework
#6) cat homework.py
#7) git add . | git commit -m "Finished Homework" | git push
#8) Judy’s local branch was behind the remote version. To resolve: git pull origin main --rebase
#9) /Users/judy/Recents

# 4.1: Data Types

def checkDataType(value):
    return type(value)

print(checkDataType(3.14))
print(checkDataType(True))

# 4.2: Conditionals

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(7))
print(even_or_odd(10))

# 5: Loops

numbers = [1, 2, 3, 4, 5]

def sum_With_Loop(nums):
    total = 0
    for i in nums:
        total += i
    return total

print(sum_With_Loop(numbers))

#6: Homework 4 Review

#6.1: List

def duplicate_List(lst):
    new_list = []
    for item in lst:
        new_list.extend([item, item])
    return new_list

duplicate_List(["a", "b", "c"])

#6.2: Debugging

def square(num):  #The error was forgetting to put the colon after defining your function\
    return num * num

print(square(5))