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
# 4. LOOPS (for, while)
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


# ------------------------------------------------------------
# 5. DATA STRUCTURES
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
    "is_student": False
}
person["age"] = 31               # Update value
person["city"] = "Austin"        # Add new key-value pair

# Dictionary iteration
for key, value in person.items():
    print(key, "->", value)


# ------------------------------------------------------------
# 6. STRINGS
# ------------------------------------------------------------

text = "python programming"

# Slicing
first_word = text[:6]            # "python"
last_word = text[7:]             # "programming"

# Methods
length = len(text)               # 18
upper_text = text.upper()        # "PYTHON PROGRAMMING"
contains_py = "py" in text       # True

# String formatting
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

numbers = [3, 7, 1, 9]

minimum = min(numbers)           # 1
maximum = max(numbers)           # 9
total = sum(numbers)             # 20
length = len(numbers)            # 4
sorted_list = sorted(numbers)    # [1, 3, 7, 9]
data_type = type(numbers)        # <class 'list'>


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
