# we use escape sequences to be able to use notations in the double quotes with no problem, there are:
# \"
# \'
# \\
# \n

full_name = "Arman \"Ardavani"
print(full_name)

full_name2 = "Arman \'Ardavani"
print(full_name2)

full_name3 = "Arman \\ Ardavani"
print(full_name3)

full_name4 = " Arman \n Ardavani"
print(full_name4)
