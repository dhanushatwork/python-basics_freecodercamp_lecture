# This code demonstrates BASIC OBJECT-ORIENTED PROGRAMMING (OOP) concepts in Python
# Concepts learned here:
# 1. Class and object
# 2. __init__ constructor
# 3. Instance variables
# 4. self keyword
# 5. Comparing data between two objects
class Students:
    # __init__ is a constructor
    # It runs automatically when an object of this class is created
    # It is used to initialize (assign initial values to) object variables
    def __init__(self):
        # Instance variables
        # These variables belong to EACH object separately
        self.section = "A"
        self.age = 14
    # This is a method used to compare two student objects
    # 'self' refers to the current object
    # 'others' refers to another object passed for comparison
    def compare(self,others):
        # Compare age of current object with age of another object
        if self.age == others.age:
            return True
        else:
            return False
        
# Creating first object of Students class
s1 = Students()     # __init__ is automatically called
s1.age = 15         # Updating age only for s1 object

# Creating second object of Students class
s2 = Students()     # __init__ is automatically called
# s2.age remains 14 (default value from constructor)

# Comparing ages of two objects directly using their instance variables

if s1.age == s2.age:
    print("They are of the same age")
else:
    print("Age is different")