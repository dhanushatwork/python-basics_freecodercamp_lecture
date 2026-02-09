class Computer:

    def config(self):
        print("This is i5, 16GB RAM and 1TB storage")

comp1 = Computer()

Computer.config(comp1)

comp2 = Computer()

Computer.config(comp2)

comp1.config()
comp2.config()