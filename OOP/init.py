class Computer:

    def __init__(self,cpu,ram):
        print("Init Started.....")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("CPU:", self.cpu, "RAM:" , self.ram)


comp1 = Computer("i5", 16)
comp2 = Computer("Ryzen-5", 32)

comp1.config()
comp2.config()