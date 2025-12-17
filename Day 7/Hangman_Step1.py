import random
import hangman
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

random_word = random.choice(hangman.word_list).lower()
placeholder = ""
lives = 5
print(random_word)
placeholder = ""
for position in range(1,len(random_word)+1):
    placeholder+="_"
print(placeholder)
Game_over  = False
correct_list = []
while not Game_over:
    print(f"You have total {lives} lives")
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
    if guess not in random_word:
        print(f"You have already guessed {guess}")
        lives-=0

    if "_" not in display:
        Game_over = True
        print("You win")
    if guess not in random_word:
        lives-=1
        print(f"Now You have {lives} lives left")

        if lives ==0:
            print(f"You lost!\n The correct word was {random_word}" 
            )
            Game_over = True
        elif lives ==1:
            print(f"Now You have {lives} live left")

    print(stages[lives])