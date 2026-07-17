
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
