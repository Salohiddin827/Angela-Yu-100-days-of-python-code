import random
words = ["Salohiddin","jamie","Jacky","John","Arthur"]
random_word = random.choice(words).lower()
# for letter in random_word:
#     letter.replace(letter,"_")

print(random_word)
guess = input("Guess a letter")
for l in random_word:
    if guess ==l:
        print("Right")
    else:
        print("wrong")