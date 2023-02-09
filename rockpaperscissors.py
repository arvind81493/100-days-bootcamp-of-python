import random
from traceback import print_tb

rock='''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
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
game_images=[rock,paper,scissors]
userchoice=int(input("what is your choice? type 0 for rock,type1 for paper,2 for scissors"))
print(game_images[userchoice])
computerchoice=random.randint(0,2)
print("computer choice :")
print(game_images[computerchoice])
# if userchoice>=3 or userchoice<0:
                # print("u type invalid input")
# else:
#         print(game_images[computerchoice])
        
if userchoice==0 and computerchoice==2:
                                    print("user win")
elif computerchoice>userchoice:
                                print("you lose")
elif userchoice>computerchoice:
                            print("you win")
elif computerchoice==userchoice:
                                print("its draw")
else:
          print("u type invalid input")
                                        



