# Day 8 - Caesar Cipher (STARTER CODE)

# TODO-1: Alphabet ro'yxatini yarating
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(text,shift,encode_or_decode):
    encrypted = ""
    if encode_or_decode =="decode":
                shift*=-1
    for letter in text:
        if letter not in alphabet:
            encrypted+=letter
        else:
            postion = alphabet.index(letter)
            new_position = postion+shift
            new_position %= len(alphabet)
            enc_let = alphabet[new_position]
            encrypted +=enc_let

    print(f"Here is your {encode_or_decode}d word: ")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text1= input("Type your message:\n").lower()
    shift1 = int(input("Type the shift number:\n"))
    ceaser(text=text1,shift=shift1,encode_or_decode=direction)

    choice = input("Type 'yes' to continue or 'no' to stop ")
    if choice=="yes":
        should_continue = True
    elif choice=="no":
        should_continue = False
    else:
        print("Wrong input")

