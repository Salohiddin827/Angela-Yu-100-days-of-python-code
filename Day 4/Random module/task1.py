import random
import my_module


random_int = random.randint(1,10)
print(random_int)

print(my_module.my_favourite_number)
random_0_1 = random.random()
print(random_0_1)
random_= random.uniform(1,10)
print(random_)
head_tail = random.randint(0,1)
if head_tail==0:
    print("Heads")
else:
    print("Tails")
