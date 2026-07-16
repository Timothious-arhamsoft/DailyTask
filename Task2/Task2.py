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


#---List Cmprehension
#----------------- Methods of List
# Append
temp_list = [1, 2, 3, 4, 5]
temp_list.append(6)

# extend
temp_list.extend([7, 8, 9])

# Diiference between append and extend:
# - append() adds its argument as a single element to the end of a list. The length of the list itself will increase by one.
# - extend() iterates over its argument adding each element

# insert
temp_list.insert(0, 0)  # Insert 0 at index 0
print(temp_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# remove
temp_list.remove(3)  # Remove the first occurrence of 3
print(temp_list)  # Output: [0, 1, 2, 4, 5, 6, 7, 8, 9]

# pop
popped_item = temp_list.pop()  # Remove and return the last item
print(popped_item)  # Output: 9
print(temp_list)  # Output: [0, 1, 2, 4, 5, 6, 7, 8]

# index
index_of_5 = temp_list.index(5)  # Get the index of the first occurrence of 5
print(index_of_5)  # Output: 4

# count
count_of_2 = temp_list.count(2)  # Count the occurrences of 2
print(count_of_2)  # Output: 1

# sort 
unodered_list = [5, 2, 8, 1, 4, 7, 6, 0]
unodered_list.sort()  # Sort the list in ascending order
print(unodered_list)  

# reverse
unodered_list.reverse()  # Reverse the list
print(unodered_list)  # Output: [8, 7, 6, 5, 4, 2, 1, 0]

# Copy
copied_list = unodered_list.copy()  # Create a shallow copy of the list
copied_list.append(9)  # Modify the copied list
print(unodered_list)  # Output: [8, 7, 6, 5, 4, 2, 1, 0]
print(copied_list)  # Output: [8, 7, 6, 5, 4, 2, 1, 0, 9]

