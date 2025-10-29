#First case
number = 100
while number > 0:
    print(number)
    number //= 2   #this is the same as number = number // 2
print("first case done")








# in this code we are trying to be able to give inputs as a user and get answer printed witn format arman + our command, but while our command which is the input is not quit. 
# therefor if we type quit as a command it will end the programm.
# its important to note that quit should be in a double quote.
command = ""
while command.lower() != "quit":
    command = input(">")
    print("Arman", command)
print("2nd case done")
    