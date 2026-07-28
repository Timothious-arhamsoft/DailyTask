import logging
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
import json
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


# Loging:
# Warning
logging.warning("Remain Calm!")
# Debug
logging.debug("This is a debug Message!")
# Info
logging.info("This is an info Message")
# Error
logging.error("This is an Error Message")
# Critical
logging.critical("This is an critical Message")
# Basic Config
logging.basicConfig(level=logging.DEBUG)
logging.debug("This will get logged.")

logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")
logging.warning("Hello, Warning!")


print(Path.cwd())
print(Path.home())

base = Path(__file__).parent
print("Base: ", base)
source = base / Path("practice.c")
destination = base / Path("practice.txt")
print(source)
print(source.exists())
if source.exists() and not destination.exists():
    source.replace(destination)

# Counter
sample = ["A", "B", "C", "D", "E", "A", "C"]
print(Counter(sample))

# Defaultdict
d = defaultdict(list)
d["Fruit"].append("Apple")
print(d)

# PathLib
path = Path("data") / "test.txt"
print(path)

# Datetime
today = datetime.now()
print(today)
print(type(today))

# Logging Info
logging.basicConfig(
    level=logging.INFO,
    force=True
)
logging.info("User Logged In")

# Path
base = Path(__file__).parent
print(base)

data = [
    {"name": "Ali", "age": 20},
    {"name": "Sara", "age": 22}
]

# Created File
path = base / Path("students.json")
path.write_text(json.dumps(data, indent=4))

# Load File
load_file = base / Path("students.json")
students = json.loads(load_file.read_text())
print(students)