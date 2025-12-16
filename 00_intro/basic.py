"""
REFERENCE GUIDE FOR BASIC PYTHON SYNTAX AND CONCEPTS
This file provides a concise overview of Python fundamentals.
It includes examples of core data types, control flow, data 
structures, strings, functions, and built-in utilities.
"""


# ------------------------------------------------------------
# 1. BASIC DATA TYPES
# ------------------------------------------------------------

# Boolean
is_active = True
is_complete = False

# Integer
count = 42

# Float
temperature = 98.6

# String
message = "Hello, Python!"


# ------------------------------------------------------------
# 2. BASIC OPERATIONS
# ------------------------------------------------------------

# Arithmetic: +, -, *, /, //, %, **
a = 10
b = 3
sum_val = a + b       # 13
quotient = a / b      # 3.333...
floor_div = a // b    # 3
modulus = a % b       # 1
power = a ** b        # 1000

# Boolean logic
greater_than = a > b         # True
greater_than_equal = a >= b  # True
equal_to = a == b            # False

# Type Conversion
num_str = "123"
num = int(num_str)    # Convert string to integer


# ------------------------------------------------------------
# 3. CONTROL FLOW (if/elif/else)
# ------------------------------------------------------------

x = 15

if x > 20:
    result = "Large"
elif x > 10:
    result = "Medium"
else:
    result = "Small"

# ------------------------------------------------------------
# 4. DATA STRUCTURES
# ------------------------------------------------------------

# List (mutable, ordered)
fruits = ["apple", "banana", "cherry"]
fruits.append("date")            # Add an item
first_fruit = fruits[0]          # Indexing

# Tuple (immutable, ordered)
coordinates = (10, 20)
x_coord = coordinates[0]

# Dictionary (key-value pairs)
person = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
}
person["age"] = 31               # Update value
person["city"] = "Austin"        # Add new key-value pair

# List in dictionary
person = {
    "name": "Alice",
    "age": 30,
    "places_lived": ["Hong Kong", "Paris", "Washington DC"] 
}

# Dictionaries in List
people = [
    {"name": "Bob", "age": 42},
    {"name": "Jack", "age": 23},
    {"name": "John", "age": 12},
    {"name": "George", "age": 61}
]

# ------------------------------------------------------------
# 5. LOOPS (for, while)
# ------------------------------------------------------------

# For loop (iterate over list)
for n in [1, 2, 3]:
    print("Number:", n)

# Range example
for i in range(5):  # 0, 1, 2, 3, 4
    print("i =", i)

# While loop
counter = 0
while counter < 3:
    print("Counter is", counter)
    counter += 1

# Enumerate example
for i, ch in enumerate(['a', 'b', 'c', 'd']):
    print("Result: ", i, ch)

# Dictionary iteration
for key, value in person.items():
    print(key, "->", value)

# Skipping iterations in a loop with continue
for ch in ['A', 'B', 'c', 'd', 'e']:
    if ch in ('A', 'C'):
        continue
    print(ch)

# ------------------------------------------------------------
# 6. STRINGS
# ------------------------------------------------------------

# Text can be single or double quoted
text = "python programming"

# Three quotes for multi-line string
multi_line_string = """This is a string
that spans multiple lines.
It's very useful for long blocks of text."""

# Slicing works like a list
first_word = text[:6]            # "python"
last_word = text[7:]             # "programming"

# Creating list
my_string = "abc,def,vtx,stz,dau"
my_list1 = my_string.split(",")  # ['abc', 'def', 'vtx', 'stz', 'dau']
my_list2 = list(my_string)       # ['a', 'b', 'c', ',', ....., 'u']

# General Methods
length = len(text)               # 18
contains_py = "py" in text       # True


# Cleaning
upper_text = text.upper()          # "PYTHON PROGRAMMING"
title_text = text.title()          # "Python Programming"
lower_text = upper_text.lower()    # "python programming"
"  some text  ".strip()            # "some text"
"  some text  ".lstrip()           # "some text  "
"  some text  ".rstrip()           # "  some text"
"apple pie".replace("pie", "cake") # "apple cake"

# Using f-strings
name = "Bob"
greeting = f"Hello, {name}!"     # f-string


# ------------------------------------------------------------
# 7. SLICING SYNTAX (LISTS, TUPLES, AND STRINGS)
# ------------------------------------------------------------

# Slicing syntax: sequence[start:stop:step]
# - start: index to begin (inclusive)
# - stop: index to end (exclusive)
# - step: interval between items

# LIST SLICING
numbers = [10, 20, 30, 40, 50, 60]

first_three = numbers[:3]        # [10, 20, 30]
middle_slice = numbers[2:5]      # [30, 40, 50]
last_two = numbers[-2:]          # [50, 60]
every_other = numbers[::2]       # [10, 30, 50]
reversed_list = numbers[::-1]    # [60, 50, 40, 30, 20, 10]

# TUPLE SLICING (same syntax as lists)
coords = (1, 2, 3, 4, 5)
coords_slice = coords[1:4]       # (2, 3, 4)

# STRING SLICING
text = "Python"

first_two = text[:2]             # "Py"
last_three = text[-3:]           # "hon"
skip_letters = text[::2]         # "Pto"
reversed_text = text[::-1]       # "nohtyP"


# ------------------------------------------------------------
# 8. LIST AND DICTIONARY COMPREHENSIONS
# ------------------------------------------------------------

# Think of "concise for loop"

# LIST COMPREHENSION
# Syntax: [expression for item in iterable if condition]

# Square each number
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]                      # [1, 4, 9, 16, 25]

# Filter even numbers
evens = [n for n in nums if n % 2 == 0]              # [2, 4]

# Create tuples (number, square)
paired = [(n, n * n) for n in nums]                  # [(1,1), (2,4), ...]

# DICTIONARY COMPREHENSION
# Syntax: {key_expr: value_expr for item in iterable if condition}

# Map numbers to their squares
square_map = {n: n * n for n in nums}                # {1:1, 2:4, ..., 5:25}

# Filter and transform keys/values
filtered_map = {n: n * 2 for n in nums if n > 2}     # {3:6, 4:8, 5:10}

# Build dictionary from list of tuples
pairs = [("apple", 3), ("banana", 2), ("cherry", 5)]
fruit_map = {fruit: qty for fruit, qty in pairs}     # {"apple":3, ...}

# Reverse key/value (only safe if values are unique)
reversed_map = {qty: fruit for fruit, qty in pairs}  # {3:"apple", ...}

# ------------------------------------------------------------
# 9. FUNCTIONS
# ------------------------------------------------------------

def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

def add(x, y):
    """Add two numbers."""
    return x + y

def factorial(n):
    """Compute factorial using a loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ------------------------------------------------------------
# 10. BUILT-IN FUNCTIONS (common examples)
# ------------------------------------------------------------

# Printing
print("a message for Bob")         # "a message for Matthew"
name = "Bob"
print(f"a message for {name}")     # f-strings
print(f"a message for {name=}")    # optionally, give the variable name and value

age = 33                           # Multi-line string (one option)
workplace = "University of Austin"
message = f"""
Hello, my name is {name}.
I am {age} years old.
I work at {workplace}.
"""
print(message)

# Numbers
numbers = [3, 7, 1, 9]

minimum = min(numbers)           # 1
maximum = max(numbers)           # 9
total = sum(numbers)             # 20
length = len(numbers)            # 4
sorted_list = sorted(numbers)    # [1, 3, 7, 9]
data_type = type(numbers)        # <class 'list'>

# Random
random_int = random.randint(1, 10)          # random integer between 1 and 10 (inclusive)
random_float = random.random()              # random float between 0 and 1
random_uniform = random.uniform(10.5, 20.5) # random float between 10.5 and 20.5

# ------------------------------------------------------------
# 11. MAIN EXAMPLE (for demonstration)
# ------------------------------------------------------------

def main():
    print("Basic Python Reference")
    print("----------------------")
    print("Greeting:", greet("Alice"))
    print("Add 2 + 3 =", add(2, 3))
    print("Factorial of 5 =", factorial(5))
    print("Sorted numbers:", sorted_list)

if __name__ == "__main__":
    main()
