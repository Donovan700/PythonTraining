# Introduction
print("Please enter an integer(0-9)\nPress -1 to quit")

# Procedures
Working=True
while Working:
    number=int(input(">>>"))
    if number == -1:
        Working=False
        print("Exiting...")
    elif number == 0:
        print("Zero\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 1:
        print("One\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 2:
        print("Two\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 3:
        print("Three\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 4:
        print("Four\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 5:
        print("Five\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 6:
        print("Six\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 7:
        print("Seven\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 8:
        print("Eight\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    elif number == 9:
        print("Nine\nWant to continue?")
        answer=input()
        if answer == "no" or answer == "No" or answer == "n" or answer == "N" or answer == "NO" or answer == "nO":
            Working=False
    else:
        print("Number not between 0 to 9")
