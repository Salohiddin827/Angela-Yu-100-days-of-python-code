print("   Welcome to Treasure Island.\nYpur mission is to find the treasure")
direction = input("Which direction you will choose to go through? ").lower()
if direction =="Right":
    print("Game Over!")
elif direction =="left":
    wait_or_swim = input("You are now in front of river\n do you wait the boat or swim to pass? ").lower()
    if wait_or_swim =="swim":
        print("Game Over!")
    elif wait_or_swim == "wait":
        door = input("Which door do you choose? Red or Blue or Yellow ").lower()
        if door=="bed" or door =="blue":
            print("Game Over!")
        elif door =="yellow":
            print("Wow! You win! ")
        else:
            print("Wrong input")
    else:
        print("Wrong input")
else:
    print("Wrong input")



    