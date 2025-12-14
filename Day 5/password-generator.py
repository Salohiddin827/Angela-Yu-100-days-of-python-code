letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}',
    ';', ':', "'", '"',
    ',', '.', '<', '>', '/',
    '?', '\\', '|', '`', '~'
]
import random
print("Welcome to the safest Password generator")
letter = int(input("How many letters do you want? "))
number = int(input("How many numbers do you want? "))
symbol = int(input("How many symbols do you want? "))
password = []
for let in range(0,letter):
    random.choice(letters)
    password  +=random.choice(letters)
for num in range(0,number):
    password  +=random.choice(numbers)
for sym in range(0,letter):
    password  +=random.choice(symbols)

random.shuffle(password)

str_password = ""
for p in password:
    str_password+=p
print("Your password is: ", str_password)
