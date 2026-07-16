# Tomorrows Redo Task

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

# Task 1: Comprehension refactor
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
print("Dictionary from Comprehension: ", dict_comprehension)




