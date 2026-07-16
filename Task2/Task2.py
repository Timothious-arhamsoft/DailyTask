# Task 1: Tomorrows Redo Task

# A -> cache-bug fix 
def cache_bug(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(cache_bug(1))  # Output: [1]

# B -> bare-except fix 

def bare_except(value):
    try:
        result = value/0
        print(result)
    except ZeroDivisionError:
        print("Number cannot be divided by zero.")

bare_except(5)

# C -> file-read fix

def file_read(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            # Ilterative method to read file line by line and consume less RAM for large Files
            # for line in file:
            #     print(line.strip())
    except FileNotFoundError:
        print("File not found. Please check the file path.")

file_read("Task2/file.txt")
#------------------------------------------
#---------16-July-2026

# Task 2: Comprehension refactor
#---List Cmprehension
import random

# Simple Loop 
list_comprehension = []
for i in range(10):
    list_comprehension.append(random.randint(1,20))

print("Generated List: ", list_comprehension)

# Lambda Function
squared_list = list(map(lambda x: x**2, range(10)))
squared_list_random = list(map(lambda x: x**2, list_comprehension))
print("Squared List: ", squared_list)
print("Squared List from Random List: ", squared_list_random)

# Lsit inside List
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

# Transpose
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed.append([row[i] for row in matrix])
    return transposed

print("Transposed Matrix: ", transpose(matrix))


# Filtering Example

# Simeple Loop
print("Simple Loop Filter:")
for i in list_comprehension:
    if i % 2 == 0:
        print(i, "is even.")

# List Comprehension Filter
print("List Comprehension Filter:")
print([i for i in list_comprehension if i % 2 == 0])



# Making Dictionary from Two list
keys = [1,2,3,4]
values = ['a', 'b', 'c', 'd']

# Simple Loop
if (len(keys) == len(values)):
    combine_dict ={}
    for i in range(len(keys)):
        combine_dict[keys[i]] = values[i]
    print("Combined Dictionary: ", combine_dict)

# Dict Comprehension 
dict_comprehension = {keys[i]: values[i] for i in range (len(keys))}
dict_comprehension_v2 = {keys:values for keys, values in zip(keys, values)}
print("Dictionary from Comprehension: ", dict_comprehension)
print("Dictionary from Comprehension v2: ", dict_comprehension_v2)


# ----------Complex List Comprehension
# As its impossible to debug or scan quickly.
# As Below we have Wrror: AttributeError: 'list' object has no attribute 'is_active'   

# flattened_data = [str(val).upper() for block in matrix if block.is_active for row in block.rows if sum(row) > 10 for val in row if val != 0]

# Easy
matrix_v2 = [
    [[5, 6, 7, 8]],
    [[0, 0]]
]
flattened_data_simple = []
for block in matrix_v2:
    for row in block:
        if sum(row) > 10:
            for val in row:
                if val != 0:
                    flattened_data_simple.append(str(val).upper())


# print("Flattened Data: ", flattened_data)
print("Flattened Data Simple: ", flattened_data_simple)

#------------------------------
# Task 3: Custom exception:
# Link youtube: https://www.youtube.com/watch?v=CK0wc85inxk&t=100s
# Link Website: https://realpython.com/python-exceptions/#creating-custom-exceptions-in-python

#--> Method 1:
'''class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
                raise InsufficientFundsError(
            f"Insufficient funds: balance is ${balance}, attempted withdrawal is ${amount}."
        )

    return balance - amount

try: 
    new_balance = withdraw(100, 150)
    print(f"Withdrawal successful. New balance: {new_balance}")
except InsufficientFundsError as e:
    print(e)
'''

#--> Method 2:
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: balance is Rs{balance}, attempted withdrawal is Rs{amount}.")

def withdraw(balance, amount):
    if amount> balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

balance = 1000
amount = 10000
try:
    withdraw(balance, amount)
except InsufficientFundsError as e:
    print(f"Warning: {e}")

# More Example

class VowelsError(Exception):
    pass

def check_vowels(input_string):
    vowels = "aeiouAEIOU"
    for char in input_string:
        if char in vowels:
            raise VowelsError(f"Vowel '{char}' found in the input string.")

try:
    check_vowels("Hello")
except VowelsError as e:
    print(e)


#------------------------------
# Task 4: Context manager:

import time
from contextlib import contextmanager

#Method 1: Using Class (Enter and Exit Methods)
class TimerContextManager:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time: {self.elapsed_time} seconds")

# with TimerContextManager() as timer:
#     time.sleep(2)


# Method 2: Decorator (@contextmanager)
@contextmanager

def timer_context_manager():
    start_time = time.time()
    try:
        yield
    except Exception as e:
        print(f"An error occurred Inside: {e}")
        
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
# with timer_context_manager():
#     time.sleep(2)


# Task 5: Breake Points

def calculate_sum(a,b):
    final = a+b
    # breakpoint() 
    return final

print(calculate_sum(5, 10))