logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction game")

my_dict = {}
highest_bid = 0
winner = ""

while True:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    other = input("Are there any bidders? yes/no: ").lower()

    my_dict[name] = bid  

    if other == "yes":
        print("\n" * 100)
    else:
        break


for name, bid in my_dict.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"Its sold to {winner} to the amount ${highest_bid}")
   