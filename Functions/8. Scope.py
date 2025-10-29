message = "a"     # this is a global variable, which means it's outside of a function and it can be used globally across our file

def greet(name):
    message = "b"  # this is a local varibale which is dedicated only to this function

greet("Arman") 
print(message)    # but now when we try to print the variable message here, it prints the global message, and it can mess with our file
                  # therefore its recommended to not use global varibales.