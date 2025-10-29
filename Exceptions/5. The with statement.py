try:
    with open("The with statement.py") as file:
        print("File opened")
    age = int(input("age: "))
    xfactor = 1 / age
except (ValueError, ZeroDivisionError):
    print(" You didn't enter a valid age")
else:
    print("No exceptions were thrown")
finally:
    file.close()