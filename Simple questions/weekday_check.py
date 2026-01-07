
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 

# function approach

# def findDay(num):
#     if(num < 1 or num > 7):
#         print("Invalid day number")
#         return
#     print(days[num - 1])

# findDay(7)

#if-else approach

# if(num < 1 or num > 7):
#         print("Invalid day number")
# else:   
#     print(days[num - 1])


# match-case approach

# num = int(input("Enter day number (1-7): "))
# match num:
#     case 1: print("Monday")
#     case 2: print("Tuesday")
#     case 3: print("Wednesday")
#     case 4: print("Thursday")
#     case 5: print("Friday")
#     case 6: print("Saturday")
#     case 7: print("Sunday")
#     case _: print("Invalid day number")


while(True):
    num = int(input("Enter day number (1-7): "))
    match num:
        case 1: print("Monday")
        case 2: print("Tuesday")
        case 3: print("Wednesday")
        case 4: print("Thursday")
        case 5: print("Friday")
        case 6: print("Saturday")
        case 7: print("Sunday")
        case _: 
            print("Invalid day number")
            break