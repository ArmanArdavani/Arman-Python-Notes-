try:
    age = int(input("age: "))
except ValueError:
    print(" You didn't enter a valid age")
else:
    print("No exceptions were thrown")


''' with this you are saying for my exucution, when we have the exception for ValueError, print my statment
if we have no exceptions the exception will not be executed'''
