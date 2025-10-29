# First case 
def save_user(**user):  # we use double star to call out keywords with their value in our funtion
    print(user)


save_user(id=32, name="Arman", age=16)
print("1st Case done")

# 2nd case
def save_user(**user):
    print(user["name"]) # we can call out the keyword like this, and then it will print it's value
    
save_user(id=32, name="Arman", age=16)
print("2nd Case done")
