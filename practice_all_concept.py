items = ["A", "B", "C", "D"]
dict_items = {1:"E", 2:"F", 3:"G", 4:"H"}

it = iter(items)

# Iter
while True:
    try:
        item = next(it)
        print("Item: ", item)
    except StopIteration:
        break
# Enumerate
for key,item in enumerate(items):
    print(f"Key {key}: {item}")

# Using Items
for key,item in dict_items.items():
    print(f"Key {key}: {item}")

