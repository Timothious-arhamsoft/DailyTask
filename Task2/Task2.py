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
    except FileNotFoundError:
        print("File not found. Please check the file path.")

file_read("Task2/file.txt")
#------------------------------------------
#---------16-July-2026


