"""
Python Basics: Variables, Operators, Conditional Statements,
 Loops, Jump Statements, and Functions
"""

# 1. Variable Declaration (All Data Types)
# Variables store data values of different types.
num_int = 10             # Integer
num_float = 10.5         # Float
num_complex = 3 + 4j     # Complex Number
is_valid = True          # Boolean
greeting = "Hello, Python" # String
numbers_list = [1, 2, 3, 4]  # List
numbers_tuple = (5, 6, 7, 8) # Tuple
unique_numbers = {1, 2, 3, 4} # Set
person_info = {"name": "Deekshitha", "age": 21}  # Dictionary
empty_value = None       # NoneType

#Indentation in Python
# Indentation refers to spaces or tabs used at the beginning of code lines to define code blocks.
# Python strictly enforces indentation, and improper indentation results in an error.

# Correct Indentation Example:
if True:
    print("This is properly indented.")
    if True:
        print("Nested indentation is also required.")

# Incorrect Indentation Example (This will cause an error)
# if True:
# print("This will cause an indentation error.")

# Indentation in Loops and Functions
for i in range(3):
    print("Iteration:", i)  # Correctly indented

# Function indentation example
def sample_function():
    print("Inside function")  # Properly indented
sample_function()

# 2. Operators in Python
# Operators are used to perform operations on variables and values.

# Arithmetic Operators
sum_result = 5 + 3  # Addition
diff_result = 5 - 3  # Subtraction
prod_result = 5 * 3  # Multiplication
div_result = 5 / 3  # Division
mod_result = 5 % 3  # Modulus
exp_result = 5 ** 3 # Exponentiation
floor_div_result = 5 // 3  # Floor Division

# Comparison Operators
is_equal = (5 == 3)  # False
is_not_equal = (5 != 3)  # True
is_greater = (5 > 3)  # True
is_less = (5 < 3)  # False

# Logical Operators
logical_and = (5 > 3 and 3 > 1)  # True
logical_or = (5 > 3 or 3 < 1)  # True
logical_not = not (5 > 3)  # False

# Bitwise Operators
bitwise_and = 5 & 3  # 1 (101 & 011)
bitwise_or = 5 | 3   # 7 (101 | 011)
bitwise_xor = 5 ^ 3  # 6 (101 ^ 011)
bitwise_not = ~5     # -6

# Assignment Operators
num_x = 5
num_y = 3
num_x += num_y  # num_x = num_x + num_y
num_x -= num_y  # num_x = num_x - num_y

# 3. Conditional Statements
# Conditional statements are used to execute a block of code based on conditions.
num = 10
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")

# 4. Loops in Python
# Loops are used to execute a block of code multiple times.

# For Loop - Iterates over a sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# For Loop with range
for number in range(1, 6):
    print("Number:", number)

# For Loop to print square of numbers from 1 to 5
for num in range(1, 6):
    print(f"Square of {num} is {num ** 2}")

# For Loop to iterate over dictionary
person = {"name": "Deekshitha", "age": 21, "city": "Hyderabad"}
for key, value in person.items():
    print(f"{key}: {value}")

# While Loop to find sum of first n natural numbers
n = 5
sum_n = 0
current = 1
while current <= n:
    sum_n += current
    current += 1
print("Sum of first 5 natural numbers:", sum_n)

# Additional While Loop Examples

# Countdown from 10 to 1
count = 10
while count > 0:
    print("Countdown:", count)
    count -= 1

# Print even numbers up to 20
even_num = 2
while even_num <= 20:
    print("Even Number:", even_num)
    even_num += 2

# Reverse string using while loop
string = "Python"
reversed_string = ""
i = len(string) - 1
while i >= 0:
    reversed_string += string[i]
    i -= 1
print("Reversed String:", reversed_string)

# While Loop to find factorial of a number
num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial of 5:", factorial)

# 5. Jump Statements
# Jump statements alter the flow of execution.

# Break Example - Exits loop when condition is met
for index in range(10):
    if index == 5:
        break
    print("Break Loop Value:", index)

# Continue Example - Skips the current iteration
for index in range(10):
    if index % 2 == 0:
        continue
    print("Odd Number:", index)

# 6. Functions in Python
# A function is a block of reusable code that performs a specific task.

def greet_user(username):
    """This function takes a name and returns a greeting message."""
    return "Hello, " + username

# Function Calling - Invoking the function
print(greet_user("Deekshitha"))  # Output: Hello, Deekshitha

# Function with Parameters and Arguments
def add_numbers(num1, num2):
    """This function adds two numbers and returns the result."""
    return num1 + num2

print(add_numbers(5, 3))  # Output: 8

# Function with Default Parameters
def power(base, exponent=2):
    """This function raises base to the power of exponent (default is 2)."""
    return base ** exponent

print(power(3))    # Output: 9 (3^2)
print(power(3, 3)) # Output: 27 (3^3)

# Function Returning Multiple Values
def get_user_info():
    """Returns multiple values as a tuple."""
    return "Deekshitha", 21, "Hyderabad"

name, age, city = get_user_info()
print(name, age, city)  # Output: Deekshitha 21 Hyderabad

# Lambda Function - Anonymous function
square = lambda num: num * num
print(square(5))  # Output: 25

# The 'return' Statement
# The return statement is used in a function to send the result back to the caller.
# If no return statement is used, the function returns None by default.

def multiply(num1, num2):
    return num1 * num2  # Returns the product of two numbers

result = multiply(4, 5)
print(result)  # Output: 20
