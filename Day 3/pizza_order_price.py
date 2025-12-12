print("Welcome to the Python Pizza Deliveries")
size = input("What size do you want? S, M or L ")
pepperoni  = input("Do you want pepperoni in your pizza? Y or N ")
extra_cheese = input("Do you want extra cheese? ")
total_bill = 0
if size == "S":
    total_bill+=15
    if pepperoni =="Y":
        total_bill+=2
    if extra_cheese =="Y":
        total_bill+=1
elif size == "S":
    total_bill+=20
    if pepperoni =="Y":
        total_bill+=3
    if extra_cheese =="Y":
        total_bill+=1
elif size == "S":
    total_bill+=25
    if pepperoni =="Y":
        total_bill+=3
    if extra_cheese =="Y":
        total_bill+=1
else:
    print("You have wrong inputs")
print(f"You have to pay {total_bill}")
