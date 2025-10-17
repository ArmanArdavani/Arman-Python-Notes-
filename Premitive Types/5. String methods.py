course = "python programming"
print(course.upper())           # we use upper method to convert characters to upper cases
print(course.lower())           # we use lower method to convert characters to lower cases
print(course.title())           # it will capitalize the first character of each string
print(course.find("pro"))       # it gives the index value of the string that you asked for it ti find from your variable 
print(course.replace("p", "j")) # replaces the character you want in the string
print("pro" in course )         # this gives the boolean value of the existance of the string in our string
print("pro" not in course)      # this gives the boolean value of the string not existing in our string

course2 = "   python programming"
print(course.strip())  # it will remove white spaces from both beginning and the end of a string


