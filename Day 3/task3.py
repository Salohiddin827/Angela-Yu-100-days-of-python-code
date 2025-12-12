height = int(input("What's your height? "))
bill = 0
if height <120:
    print("Sorry,You can't ride rollercoaster")
else:
    print("You can ride rollercoaster")
    age = int(input("How old are you? "))
    if age <=12:
        print("You have to pay $7")
        bill+=5
    elif age <=18:
        print("You have to pay $7")
        bill+=7
    elif age=>45 and age=<55:
        bill+=0

    else:
        print("You have to pay $12")
        bill+=12

    want_photo = input("Do you want photo ")
    if want_photo =="Y":
        bill+=3
    print(f"Your final bill is {bill}")