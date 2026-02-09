#2 types of variable
    
class Car:
    # Class(Static) variable
    wheel = 4
    # Instance variable
    def __init__(self):
        self.mil = 10
        self.com = "BMW"



c1 = Car()
c1.mil = 8
c2 = Car()

Car.wheel = 6

print(c1.mil, c1.com, c1.wheel)
print(c2.mil, c2.com, c2.wheel)
    