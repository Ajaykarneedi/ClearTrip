

class Student:                                     # Outer Class
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name , self.roll)
        self.lap.show()

    class Laptop:                                   # Inner Class
        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = '8GB'

        def show(self):
            print(self.brand, self.cpu, self.ram)
s1 = Student('Ajay',2)
s2 = Student('Kiran',3)

#print(s1.name , s2.roll)

s1.show()

#lap1 = s1.lap
#lap2 = s2.lap

#print(id(lap1))
#print(id(lap2))