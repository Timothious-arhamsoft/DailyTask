
#-----Task 1: Iterables vs. iterators 


lst  = [10, 20, 30, 40, 50]

it = iter(lst)
print(next(it)) # 10
print(next(it)) # 20
print(next(it)) # 30


# --What happens inside a for loop?

# for num in lst:
#     print(num) 

# Inside Loop:

it = iter(lst)
while True:
    try:
        num = next(it)
        print(num)
    except StopIteration:
        break


numbers = [1,2,3]
a = iter(numbers)
b = iter(numbers)

print(next(a))
print(next(a))

print(next(b))

#-----Task 2: Generators

def count():
    yield 1
    yield 2
    yield 3

print(count())

check  = count()

'''
Did it print 1?

No.

Did it execute the function?

No.

Instead, Python created a generator object.
'''

# Now it will run
print(next(check)) # 1
print(next(check)) # 2
print(next(check)) # 3


# Generators work in for loops too


def count_gen():
    yield 1
    yield 2
    yield 3
print("----Generator----")
for num in count_gen():
    print(num)



# Task 3 ---Decorators
# Step 1: Functions can be assigned to variables
def greet():
    print("Hello!")

say_hello = greet

say_hello()

'''
We never wrote

say_hello = greet()
'''

#  Step 2: Functions can be passed as arguments

def execute(func):
    print("Function as argument:")
    func()

execute(greet)


# Step 3: Functions can return functions
def outer_func():
    print("Outer function")
    def inner_func():
        print("Inner function")
    return inner_func

outer = outer_func()
outer()


# Step 4: Combining both ideas

def combine_func(func):
    print("Combining both ideas:")
    def inner_func():
        print("Inner function Executing the function as argument:")
        return func()
    return inner_func

combine = combine_func(greet)
combine()

# Decorator Function
def decorate(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper

greet = decorate(greet)
greet()



# Task 4--- Decorators pattern

import time

def decorater_patter(func):
    def wrapper():
        print("Start")
        start_time = time.time()
        func()
        end_time = time.time()
        print("End")
        print("Time taken:", end_time - start_time)
    return wrapper


# Task 5: Idiomatic iteration 

# ---> enumerate
planets_lst = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
places = [0,1,2,3,4,5,6,7]

# Code Smell

for i in range(len(planets_lst)):
    print(i,planets_lst[i])
# Idiomatic

for index, name in enumerate(planets_lst):
    print(index, name)

# ---> zip


# Code Smell
if len(planets_lst) == len(places):
    for i in range(len(planets_lst)):
        print(planets_lst[i], places[i])

# Idiomatic
for name, id in zip(planets_lst, places):
    print(name, id)


# --> itertools
list1 = [1, 2, 3]

list2 = [4, 5, 6]


# Code Smell

'''
Python first created A brand-new list. Then iterated over it. For very large lists, this wastes memory.
'''
for i in list1 + list2:
    print(i)

# Idiomatic
'''
it simply walks through one iterable, then the next.

Read list1

↓

1
2
3

↓

Move to list2

↓

4
5
6

'''


from itertools import chain
for x in chain(list1, list2):
    print(x)


# functools.lru_cache
# Cashe

# ---> Basic Idea
cache = {}

def square(x):

    if x in cache:
        print("Using cache")
        return cache[x]

    print("Calculating")

    result = x * x
    cache[x] = result

    return result

print(square(5))
print(square(5))
print(square(5))

# --> Using lru_cache

from functools import lru_cache
@lru_cache
def square_v2(x):
    print("Calculating")
    return x*x
print(square_v2(5))
print(square_v2(5))
print(square_v2(5))



# Setting the cache size
from functools import lru_cache, partial

@lru_cache(maxsize=3)
def square(x):
    print("Calculating")
    return x * x

# Fibonacci with Cashe
@lru_cache
def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)

# functools.partial
# Using partial
def power(base, exponent):
    return base ** exponent

square_v3 = partial(power, exponent = 2)
print("Using partial")
print(square_v3(6))
print(square_v3(7))
print(square_v3(8))


        

    
