
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
from dataclasses import dataclass

@dataclass
class Car_v2:
    model: str
    color: str


car1_v2 = Car_v2("BMW", "Black")
car2_v2 = Car_v2("BMW", "Black")
print(car1_v2)
print(car1_v2 == car2_v2)

