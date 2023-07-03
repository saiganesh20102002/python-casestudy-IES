import random
i=input("do yo want to roll the dice (y/n)")
while i=="y":
        min_value=1
        max_value=6
        n=random.randint(min_value,max_value)
        print(n)
        i=input("do yo want to roll the dice again (y/n)")
else:
    print("game over")
