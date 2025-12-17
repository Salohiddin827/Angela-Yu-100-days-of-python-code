import random
words = ["Salohiddin","jamie","Jacky","John","Arthur"]
random_word = random.choice(words).lower()
placeholder = ""
print(random_word)
placeholder = ""
for position in range(1,len(random_word)+1):
    placeholder+="_"
print(placeholder)
Game_over  = False
correct_list = []
while not Game_over:
    guess = input("Guess a letter \n") 
    display = ""
    for letter in random_word:
        if guess ==letter:
            display+=letter
            correct_list.append(letter)
        elif letter in correct_list:
            display+=letter

        else:
            display+="_"


    print(display)

    if "_" not in display:
        Game_over = True
        print("You win")