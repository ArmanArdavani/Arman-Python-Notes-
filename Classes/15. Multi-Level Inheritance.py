class Animal:
    def eat(self):
        print("eat")

class bird(Animal):
    def fly(self):
        print("fly")

class chicken(bird):
    pass 

#in here chicken is a bird but it can't fly, but the chicken class is still inheriting the fly method from bird class. 
#this is why you should avoid multi-level Inheritance in your code by all cost.