class Animal:
    def __init__(self):
        self.age = 5
    
    def eat(self):
         print("eat")

# Animal: parent, base calss 
# Mammal and fish: child, sub class 

class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
         print("swim")

m = Mammal()
m.eat()
print(m.age)

