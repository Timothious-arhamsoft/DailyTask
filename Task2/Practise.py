
# ------------------ List in Python

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

# -----------List as Queue
from collections import deque
queue = deque([1,2,3])

queue.append(4)  # Enqueue
print(queue)  # Output: deque([1, 2, 3, 4])

#--Tuples and Sequences
# Tuple are immutable sequences, typically used to store collections of heterogeneous data. Tuples are defined by enclosing the elements in parentheses ().
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

empty = ()
singleton = 'hello',  # <-- note trailing comma
print(singleton)  # Output: ('hello',)

singleton = singleton + ('bye',)  # <-- note trailing comma
print(singleton)  # Output: ('hello', 'bye')


# ----------Dictionary Comprehension

