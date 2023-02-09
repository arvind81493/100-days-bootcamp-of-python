# import turtle
# from turtle import Turtle,Screen
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# my_screen=Screen()
# my_screen.exitonclick()

# from prettytable   import PrettyTable
# table=PrettyTable()
# table.add_column("fruits Name",["apple", "banana","orange"])
# table.add_column("price",[30.24,50,34])
# print(table)

# from prettytable import PrettyTable
# table= PrettyTable()
# table.add_column("arvind",[20])
# import random
# letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
# nr_letters=int(input("how many letters do u want in your password"))
# nr_numbers=int(input("how many numbers do u want in your password"))
# nr_symbols=int(input("how many symbols do u want in your password"))
# password=""
# for char in range(0,nr_letters):
#     password+=random.choice(letters)
# for char in range(0,nr_numbers):
#     password+=random.choice(numbers)
# for char in range(0,nr_symbols):
#     password+=random.choice(symbols)
# print(password)
import random

random_side=random.randint(0,1)
if random_side==1:
    print("heads")
else:
    print("tails")