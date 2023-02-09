import random


logo="""

 _______  __   __  _______  _______  _______          _______        __    _  __   __  __   __  _______  _______  ______   
|       ||  | |  ||       ||       ||       |        |   _   |      |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  
|    ___||  | |  ||    ___||  _____||  _____|        |  |_|  |      |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  
|   | __ |  |_|  ||   |___ | |_____ | |_____         |       |      |       ||  |_|  ||       ||       ||   |___ |   |_||_ 
|   ||  ||       ||    ___||_____  ||_____  |        |       |      |  _    ||       ||       ||  _   | |    ___||    __  |
|   |_| ||       ||   |___  _____| | _____| |        |   _   |      | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |
|_______||_______||_______||_______||_______|        |__| |__|      |_|  |__||_______||_|   |_||_______||_______||___|  |_|

"""
print(logo)
HARD_LEVELS=10
EASY_LEVELS=5

def check_answer(guess,answer,turn):
    if guess>answer:
        print("to high")
        return turn-1
    elif guess<answer:
        print("to low")
        return turn-1
    else:
        print(f"you got it . your correct answer is {answer}")   
        
     
def set_difficulty():
    choose=input("choose Difficulty.Type 'easy' or hard")
    if choose=="easy":
        return EASY_LEVELS
    else:
        return HARD_LEVELS


def game():

    print("welcome to the number guessing game! ")
    print("Think of a number between 1 and 100 .")
    answer=random.randint(1,100)
    print(f"psst your answer will be {answer}")
    turn=set_difficulty()

    guess=0
    while guess!=answer:
        print(f"you have {turn} turns remaining")

        guess=int(input("make a guess"))
        turn=check_answer(guess,answer,turn)
        if turn==0:
            print(" you utilised you turn. No remaining turn left. you loose")
            return
        else:
            print("guess again")


game()
  


