class Animal:
    def __init__(self):
        self.age = 5
    
    def eat(self):
         print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")

m = Mammal()
print(isinstance(m, Mammal)) #checks to see if the object is an instance of the specific class.
print(isinstance(m, Animal))
print(issubclass(Mammal, Animal)) #cheks to see if the class inherites from another class or not.