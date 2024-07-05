print("Name age and experience of software engineer.\n")
class programmer():
    def __init__(self, name,age,experience):
        self.name=name
        self.age=age
        self.experience=experience
    def print(self):
        print(f"NAME = {self.name}\nAGE = {self.age}\nEXPERIENCE = {self.experience}\n")

data1 = programmer("shyam",23,3)
data2 = programmer("kishan",21,1)
data3 = programmer("rohit",29,6)
data1.print()
data2.print()
data3.print()