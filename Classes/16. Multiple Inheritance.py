class Employee:
    def greet(self):
        print("Employee Greet")

class Person:
    def greet(self):
        print("Person Greet")
    
class Manager(Employee, Person):
    pass 

'''here because the two classes Employee and Person have the same method greet, we you inherit them together in a new 
class called Manager Lets say, the first class you inherited is going to be executed first. 
that's why if you are writing a program that includes classes with common methods, you should avoid multiple inhertance'''

#in a case where the classes have no method or attribute in common, you can use multiple inheritance 
#like the example below:

class Flyer:
    def fly(self):
        print("Fly")

class Swimmer:
    def swim(self):
        print("Swim")
    
class flyfish(Flyer, Swimmer):
    pass
    
