day = int(input("Enter the day of a week:"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednsay")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Satarday")
    case 7:
        print("Sunday")
    case _:
        print("The is no corresponding day to your input")
         