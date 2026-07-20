
# Day-4 Tasks

#---Task 1
#-----Convert to a dataclass
# Example Simple Class

class Car:
    def __init__(self,model, color):
        self.model = model
        self.color = color
    
    def __repr__(self):
        return f"The name of the car is {self.model} with {self.color} color!"
    
    def __eq__(self, value):
        return self.model == value.model and self.color == value.color
 
        
car1 = Car("Toyota", "Red")
car2 = Car("Toyota", "Red")
car3 = Car("Honda", "Blue")

# Test __repr__
print(car1)
print(repr(car3))

# Test __eq__
print(car1 == car2)   # True
print(car1 == car3)   # False

# print(car1 == "Toyota")   
# --> Error:
'''
  File "/home/as/Downloads/Repos/DailyTask/Task4/Task4.py", line 31, in <module>
    print(car1 == "Toyota")
          ^^^^^^^^^^^^^^^^
  File "/home/as/Downloads/Repos/DailyTask/Task4/Task4.py", line 17, in __eq__
    return self.model == value.model and self.color == value.color
                         ^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'model'

'''

# ---> DataClass
from dataclasses import dataclass, field

@dataclass
class Car_v2:
    model: str
    color: str


car1_v2 = Car_v2("BMW", "Black")
car2_v2 = Car_v2("BMW", "Black")
print("--Details--")
print(f"-> {car1_v2.model}")
print(f"-> {car1_v2.color}")
print(car1_v2)
print(car1_v2 == car2_v2)



#---Task 2
# ----- Mutable default field
from dataclasses import dataclass
from typing import List
# ---> Error, Becuase every object would share the same list. 

# @dataclass
# class Car_Shop:
#     name: str
#     models: list = []

# -----Error
'''
ValueError: mutable default <class 'list'> for field models is not allowed: use default_factory

'''

# --Using Default Factory(We need Field to use this)
models = ["BMW", "Hyundi", "Honda", "MG", "Audi"]
colors = ["red", "blue", "black", "green"]

def gen_shop():
    return [Car_v2(m,c) for c in colors for m in models]

# print(gen_shop())
@dataclass
class Car_Shop_v2:
    cars: List[Car_v2] = field(default_factory=gen_shop)


shop1 = Car_Shop_v2()
shop2 = Car_Shop_v2()

print(len(shop1.cars))
print(len(shop2.cars))

# Modeified
print("Original:\n", shop1)
shop1.cars.append(Car_v2("Tesla", "Black"))
print("Updated: \n",shop1)


# --- Another Example
@dataclass
class Students:
    name: str
    subjects: list= field(default_factory=list)

s1 = Students("Tim")
s2 = Students("Tim2")

s1.subjects.append("Python")
print("Student 1: ",s1)
print("Student 2: ",s2)
'''
Output: 
Student 1:  Students(name='Tim', subjects=['Python'])
Student 2:  Students(name='Tim2', subjects=[])
'''
#---Task 3
# -----  Testing fundamentals 

def add(a,b):
    return a+b

# --- Test
def test_add():
    assert add(3,6) == 9


test_add()

