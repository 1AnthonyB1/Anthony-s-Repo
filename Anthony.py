#Introduction
print()
x = input("Hello There, I'm ... What's your name? ")
print()
print("Hello",x,"nice to meet you...")

#The adventure begins
while True:
    y = input("Are you ready to begin now? \nYes or No... ")
    y = str.upper(y)
    if y == "NO":
        True
        print("\nOk then... I guess you'll never witness this epic story...\n")
    elif y == "YES":
        False
        break

while True:
    z = input("\nGreat! The adventure begins... \n")