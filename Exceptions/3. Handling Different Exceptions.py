try:
    age = int(input("age: "))
    xfactor = 1 / age
except ValueError:
    print(" You didn't enter a valid age")
except ZeroDivisionError:
    print("age cannot be 0.")
else:
    print("No exceptions were thrown")

''' we can do that same thing above like this as well'''

try:
    age = int(input("age: "))
    xfactor = 1 / age
except (ValueError, ZeroDivisionError):
    print(" You didn't enter a valid age")
else:
    print("No exceptions were thrown")

