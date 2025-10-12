#File: homework3.py

# 3.1: Say goodbye
def say_hello(name):
    print("Hello,", name)
say_hello("Daniel")

def say_goodbye(name):
    print("Goodbye,", name)
say_goodbye("Daniel")

# 3.2: Area of a circle

def area_of_a_circle(radius):
    area = (3.14 * (radius ** 2))
    print("Area of a circle of radius,", radius, "is", area)
    return area

area_of_a_circle(5)

#4.1: Subtract, Multiply and Divide

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(divide(6, 2))

# 5.1: What should I wear

readings = [72, 57, 67, 59, 67, 60, 69, 62, 68, 61, 65, 60, 68, 57, 69, 57]
def min_max_temps(readings):
    return (min(readings), max(readings))

result = min_max_temps(readings)
print(result)

# 5.2: Check if its the Weekend

def is_weekend(day):
    return day == 6 or day == 7

print(is_weekend(4))
print(is_weekend(7))

# 5.3: Fuel Efficiency Calculator

def fuel_efficiency(distance, fuel):
    return distance / fuel

print(fuel_efficiency(50, 10), "Miles per Gallon")

# 5.4: Secret Code

def data_encryption(num):
    last_digit = num % 10
    rest = num // 10
    digits = len(str(rest))
    return last_digit * (10 ** digits) + rest

print(data_encryption(12345))
    
# 6.1: Oski stole your power
def power (a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

# 6.2: Min & Max with Loops!

print(power(2, 5))

def min_max_loops(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return(smallest, largest)

print(min_max_loops(readings))

# 6.2.1: For Loops

def min_for(nums):
    smallest = nums[0]
    for i in nums:
        if i < smallest:
            smallest = i
    return smallest

def max_for(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest

print(max_for(readings))
print(min_for(readings))

# 6.2.2: While Loops

def min_while(nums):
    smallest = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < smallest:
            smallest = nums[i]
        i += 1
    return smallest

def max_while(nums):
    largest = nums[0]
    i = 1
    while i > len(nums):
        if nums[i] < smallest:
            smallest = nums[i]
        i += 1
    return largest

print(max_while(readings))
print(min_while(readings))

# 6.3 Calculate the Sum

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

print(sum_of_digits(2468))


def area_of_a_circle(radius):
    area = (3.14 * (radius ** 2))
    print("Area of a circle of radius,", radius, ", is", area)
    return area

area_of_a_circle(5)