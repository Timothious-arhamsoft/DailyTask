

# List comprehension

numbers=[1,2,3,4,5]
result = list(item*item for item in numbers if item%2==0)
print(result)

# Iterable
it = iter(numbers)
while True:
    try:
        print(next(it))
    except StopIteration:
        break



# Exception

class Ageerror(Exception):
    def __init__(self,age):
        self.age = age
        super().__init__(f"The person is a minor: {age}")

def vote(age):
    if age<18:
        raise Ageerror(age)
    else:
        print("The Person is eligible")
    

age = 14
try:
    vote(age)
except Ageerror as e:
    print(e)

# Decorator
import time
from functools  import wraps
def time_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start=time.time()
        result = func(*args, **kwargs)
        end=time.time()
        print(end - start)
        return result
    return wrapper

# import pytest

# def test_withdraw():

#     with pytest.raises(InsufficientFundsError):
#         withdraw(100,200)
