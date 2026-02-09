class Students:

    school = "Telusko"

    def __init__(self,math,phy,cs):
        self.math = math
        self.phy = phy
        self.cs = cs

    def avg(self): #Instance method
        return (self.math + self.phy + self.cs)/3    
    
    def Get_math(self):
        return self.math
    
    def Get_phy(self):
        return self.phy
    
    def Get_cs(self):
        return self.cs

    @classmethod #Decorator
    def Get_school(cls): #Class method
        return cls.school

    @staticmethod
    def eval(avg):
        if avg >= 65:
            print("More than 65%")
        else:
            print("less than 65%")

s1 = Students(67,90,34)
s2 = Students(45,99,67)

print(s1.avg())
print(s2.avg())

print(s1.Get_math())
print(s2.Get_math())

print(s1.Get_phy())
print(s2.Get_phy())

print(s1.Get_cs())
print(s2.Get_cs())

print(Students.Get_school())

print(s1.eval(65))
print(s1.eval(35))

