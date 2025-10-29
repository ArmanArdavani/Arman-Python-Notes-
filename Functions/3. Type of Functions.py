# we have 2 types of functions
# 1- performs a task
# 2- Return a value

#this is for the first type
def greet(name):
    print(f"Hi {name}")


greet("Arman")

#this is the 2nd type
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Arman")
print(message)

# in this 2nd way now we have a variable which is our greeting with input(name), and we can use it later in our programm as well