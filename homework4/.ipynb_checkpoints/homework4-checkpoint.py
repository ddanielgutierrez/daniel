# File: homework4.py

# 3.1 - List Operations
favorite_foods = ["Pozole", "Cheeseburger", "Tamales", "Mole", "Ramen"]

print(favorite_foods[1])
print(favorite_foods[-1])

favorite_foods.append("Artichokes")

favorite_foods.insert(0, "Apple")

del(favorite_foods[2])

print(len(favorite_foods))

for food in favorite_foods:
    print(food.upper())

first_and_last = [favorite_foods[0], favorite_foods[-1]]

print (first_and_last)

if "potato" in favorite_foods:
    print("A potato!")
else:
    print("No potato!")

# 3.2 - Slicing and Striding
numbers = list(range(0, 21))

print(numbers)

def get_first_15(numbers):
    return(numbers[:16])
    
def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]


step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print("Original numbers:", numbers)
print("First 15:", step1)
print("Every 5th:", step2)
print("Reversed and every 3rd:", step3)

# 3.3 - Nested Lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]


numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(numbers[2])
print(numbers[1][1])

numbers.append([10, 11, 12])
print(numbers)

def sum_nested(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total

print(sum_nested(numbers))

# 3.4 - Create a 5x5 List
def create_list():
    matrix = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        matrix.append(row)
    return matrix
numbers_5x5 = create_list()
print (numbers_5x5)

def replace_mutltiples_of_3(matrix):
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
        new_matrix.append(new_row)
    return new_matrix

updated = replace_mutltiples_of_3(numbers_5x5)
print(updated)

def sum_not_question(matrix):
    total = 0
    for row in matrix:
        for item in row:
            if item != "?":
                total += item
    return total

result = sum_not_question(updated)
print(result)

# 4.0 - Dictionaries

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Sofia": 25,
    "Mira": 48
}
print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 52

del ages["Mariam"]

for name,age in ages.items():
    print(f"{name} is {age} years old")

