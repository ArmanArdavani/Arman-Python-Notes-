class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1 

    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        super().__init__()  #we do this so the method __init__ here doesn't overrride the __init__ method of the base class (Animal)
        self.weight = 2

    def walk(self):
        print("walk")
        

m = Mammal()
print(m.weight)
print(m.age)