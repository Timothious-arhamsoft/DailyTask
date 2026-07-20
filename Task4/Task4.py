
# Day-4 Tasks

#---Task 1
#-----Convert to a dataclass
# Example Simple Class

class Car:
    def __init__(self,model, color):
        self.model = model
        self.color = color
    
    def __repr__(self):
        return f"TThe name of the car is {self.model} with {self.color} color!"
    
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