# we use the input function to get input from the user
# as an argument we pass a string, this will be a label that will be displayed in the terminal
x = input("x: ")
print(type(x))
y = int(x) + 3
print(f"x: {x}, y: {y}")

# we use this funtions for type conversion 
int(x)
float(x)
bool(x)
str(x)


# we have some Falsy vaulues which are always False in a boolean contxt, they are:
# ""
# 0
# None
print(bool(0))
print(bool(1))
print(bool(5))

print(bool("arman"))
print(bool("False"))
print(bool(""))



