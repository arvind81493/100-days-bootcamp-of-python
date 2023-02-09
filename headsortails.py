import random
print("welcome! call your chance for  head and tail")
call =input("call whether its head or tails ")
coin=random.randint(0,1)
if coin==0:
    print("Its heads")
else:
    print("its tails")