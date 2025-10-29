#First case
won = True
for number in range(5):
    print("competition")
    if won:
        print("won")
        break
print("1st case done")

#2nd case
won = False
for number in range(5):
    print("competition")
    if won:
        print("won")
        break
else:
    print("Competed 5 times and lossed")
    
print("2nd case done")
