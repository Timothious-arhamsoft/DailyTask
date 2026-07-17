
# Day-3 Tasks

#---Task 1
# -----Lazy Counting Generator

def count_generator(n):
    for i in range(1, n+1):
        yield i

counter = count_generator(4)
print(counter)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#---Task 2
# ----- Convert a List Function into a Generator
def simple_lst(lst):
    empty = []
    for item in lst:
        empty.append(item**2)
    return empty

simple_lst_example = simple_lst
print(simple_lst_example(([1,2,3,4])))
def list_generator(lst):
    for num in lst:
        yield num ** 2


gen_lst = list_generator([1, 2, 3, 4])
print(gen_lst)
for value in gen_lst:
    print(value)
