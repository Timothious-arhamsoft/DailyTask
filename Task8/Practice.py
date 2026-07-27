# Types of Formating

# 1) Dynamic Typing
'''
This means that the Python interpreter does type checking only as code runs,
and that the type of a variable is allowed to change over its lifetime.
'''
if False:
    1 + "Two" # This line never runs, so no TypeError is raised
else:
    1+2
thing = "Hello"
print(type(thing))

thing = 28.1
print(type(thing))

# 2) Static Typing
'''
The opposite of dynamic typing is static typing. Static type checks are performed 
without running the program. In most statically typed languages, for instance C and Java,
this is done as your program is compiled.
'''

# 3) Duck Typing
'''
Another term that is often used when talking about Python is duck typing. 
This moniker comes from the phrase “if it walks like a duck and it quacks like a duck,
then it must be a duck”

'''
class TheHobbit:
    def __len__(self):
        return 95022

the_hobbit = TheHobbit()
print(len(the_hobbit))