


#*args and **kwargs

def func1(*args):
    print(args)

func1(1, 2, 3)

def func2(**kwargs):
    print(kwargs)


func2(name="check", age=23)


def student(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")


# Positional arguments
student("Ali", 22, "Lahore")

print()

# Keyword arguments
student(name="Sara", age=20, city="Karachi")

print()

# Different order
student(city="Islamabad", name="Ahmed", age=25)

# check for testing
def greet(name):
    print(name) 

# Testing Calls
#greet() #TypeError: greet() missing 1 required positional argument: 'name'
# greet(name="Ali")
#greet(student="Ali") #TypeError: greet() got an unexpected keyword argument 'student'

#--- File Handling
with open("file.txt", "r") as file:
    content = file.read()
    print(content)