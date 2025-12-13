import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome to the game")

choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper and 2 for Scissors: "))

if choice < 0 or choice > 2:
    print("Invalid input")
else:
    print(game_images[choice])

    computer = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer])

    if choice == computer:
        print("Draw")
    elif choice == 0 and computer == 2:
        print("You win")
    elif choice == 2 and computer == 0:
        print("You lose")
    elif choice > computer:
        print("You win")
    else:
        print("You lose")