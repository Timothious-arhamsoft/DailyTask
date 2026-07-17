
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

#---Task 3
# ------ @timer Decorator

#--Simple
import time
import functools
def simple_timer():
    time.sleep(2)
    print("Finished")

# Decorator

def time_deco(func):   
    def inside():
        start_time = time.time()
        print("Start: ", start_time)
        func()
        end_time = time.time()
        print("Function Name: ",func.__name__)
        print("Function Finished: ", end_time - start_time )
    return inside
@time_deco
def test():
    """This is my test function."""
    time.sleep(2)

test()
print(test.__name__)
print(test.__doc__)

# Decorator Version 2

def time_deco_v2(func):
    @functools.wraps(func)
    def inside():
        start_time = time.time()
        print("start: ", start_time )
        func()
        end_time = time.time()
        print("Function Name: ",func.__name__)
        print("Finsihed: ", end_time - start_time)
    return inside

@time_deco_v2
def greet(name="Tim"):
    """This is my Tuesday Function"""
    print(name) 

greet()
print(greet.__name__)
print(greet.__doc__)

# --- Task 5 
#----------Enumerate and Zip

planets_lst = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for key,name in enumerate(planets_lst):
    print(key,name)

example_zip = ["a", "b", "c"]
example_indes = [1,2,3]

for index,val in zip(example_indes, example_zip):
    print(index,val)
# --- Task 6

