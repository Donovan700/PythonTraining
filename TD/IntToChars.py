print("Enter number between 0-9: ")
try:
    number=int(input(">>>"))
    match(number):
        case 1:
            print(number,"s'ecrit un")
        case 2:
            print(number,"s'ecrit deux")
        case 3:
            print(number,"s'ecrit trois")
        case 4:
            print(number,"s'ecrit quatre")
        case 5:
            print(number,"s'ecrit cinq")
        case 6:
            print(number,"s'ecrit six")
        case 7:
            print(number,"s'ecrit sept")
        case 8:
            print(number,"s'ecrit huit")
        case 9:
            print(number,"s'ecrit neuf")
except:
    print("An error has occured")
