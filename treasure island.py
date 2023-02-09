from this import d


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("welcome to the treasure island")
print("your mission to find the treasure.")
go=input("where want you go? right or left").lower()
if go=="left":
    b=input("there is lake between you and treasure ,you want to wait for boat or you want to swim ?").lower()
    if b=="wait":
        d=input("congrats!you successfully crossed lake. There is door you have to open if you want treasure. which door you want to go? red ,blue or yellow? ").lower()
    if d=="red":
            print("sorry you chossed wrong door . Now you will burned by fire.Game over")
    elif d=="blue":
                print("sorry! you choose wrong door you will be Eaten by beasts . game over")
    elif d=="yellow":
                    print("CONGRUTULARTION YOU WoN all treaure")
    else:
            print("you fall into a hole.game over")
else:
     print("you will be attacked by trout.GAME OVER")
            


    
