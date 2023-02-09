# print("hello" + input("what is your name"))

# name="arvind kumar"
# print(name)
# from unicodedata import name


# name=input("what is your name?")
# print(name)

# a=input("enter a numer 1")
# b=input("enter a numer 2")
# c=a
# a=b
# b=c
# print(a)
# print(b)
# print("hello world \n hello world \n hello world \n hello world")///
# print("hell0" + " " "arvind")
# print("hello world")
# length=len("asrrsf")
# print(length)
# input("what is your name")
# input("IN WHICH CLASS DO YOU STUDY \n")
# print("hello" + input("what is your name ") )
# print("what is your good name")
# print(len(input("what is yor name")))
# input("what is your name")
# name="arvind"
# print(len(name))
# from calendar import c


# a=input("enter the  no.")
# b=input("enter the no." )
# c=a
# a=b
# b=c
# print(a)
# print(b)
# print("welcome to the band name generator")
# city=input("what is the name of your city")
# pet=input("what is your pet name")
# print("ypur band name could be " +city + " " +pet)
# print("hello"[5])
# print(123+234)
# print(123456789+122344567)
# print(3.14+3.14)
# print(type(input("what is your name")))
# a=int(123)
# print(type(a))
# print(70 +int(12.3))
# print(str(20)+str(40))
# 3+5
# 7-5
# 6/3

# print(2**3)
# print(6/3)
# print(3*3/3)
# print(round(2/3,3))
# print(round(2.555,1))
# print(2//3)
# from ast import Not
# from operator import truediv
# from optparse import Values
# from winreg import KEY_ENUMERATE_SUB_KEYS


# score=0
# height=12
# iswinning=True
# #f-string
# # print(f"your score is {score},your height is {height},your winningt chace is {iswinning}")
# print("yore score is" + str(score))
# print(round(22.19))
# lo="ANGELA".lower()
# print(lo)
# a="angela".upper()
# print(a)
# a="angela".count("a")
# import random
# randominteger=random.randint(1,10)
# print(randominteger)
# import ccc
# print(ccc.a)
# import random
# intinteger=random.randint(1,30)
# print(intinteger)
# random_float=random.random()*5
# print(random_float)
#state_of_america=["Delaware","pennsylvania","maryland","south carolina","virgina","new jersey"]
# state_of_america[1]="maryland"
# state_of_america[2]="south carolina"
# state_of_america.append("arvind kingdom")   it only passes one argument
# state_of_america.extend(["a","b"])           it passes more than one argument
#ca)
# ****list  does not have upper and lower attributes
# total=0
# for arvind in range(1,101):
#     if arvind%2==0:
#         total+=arvind
#         print(total)
    
    
             #  day 8 

# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how do you do {name}")
    
# greet_with_name("Arvind kumar")

# def greet_with_name(name):
#     print(f"all hail to mighty king {name}")
# greet_with_name("arvind yadav")
# def greet_with(name,location,district):
#      print(f"hello {name}")
#      print(f"your location is {location}")
#      print(f"your district is {district}")
# # greet_with("arvind","babrala","sambhal")
# greet_with(location="babrala",district="sambhal",name="arvind")

                      #  day 9  dictionaries

# programming_dictionasries={
#  "bug": "an error in a program that prevents the program from running or excuting",
#  "function":"a piece of code that callls itself again and again",
#  123:"The action of doing something over and over again"
#  }
# #  Reterieving the items

# print(programming_dictionasries["bug"])
# print(programming_dictionasries["function"])
# print(programming_dictionasries[123])

# adding new items to dictionary.
# programming_dictionasries["loops"]="the action of doing something over and over again"
# programming_dictionasries["recursion"]="calling the function again and again"
# print(programming_dictionasries)


# Adding element in empty dictionaries

# empty_dictionaries={}
# empty_dictionaries["loops"]="The action of doing somethiong again and again"
# empty_dictionaries["function"]="A piece if codse thats call itself again"
# empty_dictionaries["Bug"]="A moth in your computer"
# print(empty_dictionaries)

# #n edit an element in a dictionaery
# key=False
# for key in empty_dictionaries:
#     print(key)
#     print(empty_dictionaries[key])


# # nesting of dictionaries

# capitals={
#     "france":"paris",
#     "Germany":"berlin", 
# }
# travel_log={
#         "france":{"cities_visited":["paris", "little","dijon"],"total_visiters":12},
#         "Germany":{"cities_visited": ["berlin","hamburg","stuttgart"],"total_visiter":5 }
# }
# print(travel_log)

# travel_log=[
# {
#     "country":"france",
#     "cities_visited":["paris","lille","dijon"],
#     "total_visited":12
# },
# {
#     "country":"germany",
#     "cities_visited":["berlin","hamburg","stuttgart"],
#     "tota_visiters":12

# },
# ] 

# day 10  functions with outputs

# def format_name(fname,l_name):
#     formatted_f_name=fname.title()
#     formatted_l_name=l_name.title()
#     print(f"{formatted_f_name} {formatted_l_name}")
# format_name("angela","ANGELA")


# def format_name(fname,l_name):
#     formatted_f_name=fname.title()
#     formatted_l_name=l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"
#     print("this got to be printed")  # this line has to be ignored
# print(format_name("angela","ANGELA"))

# def format_name(fname,lname):
#     """take the first and last name and return the title case
#      version of the name"""
#     if fname=="" or lname=="":
#         return f"you didn't provide a valid input"
#     format_f_name=fname.title()
#     format_l_name=lname.title()
#     return f"return :{format_f_name} {format_l_name}"

# print(format_name(input("what is your name? "),input("what is your last name? ")))


# day 12 scope and global variable
 #global scope
# enemies=1        
# def increase_enmies():
#   print(f"{enemies}")
# increase_enmies()
# print(enemies)

# #local scope
# drink=2
# def drink_portion():
#     drink=1
#     print(drink)
# drink_portion()
# print(drink)

# enemies=1
# def increase_enimies():
#       return enemies+1
# total_enemies=increase_enimies()
# print(total_enemies)


# fruits=["apple","strawberery","lichi"]
# fruits.append("mango")
# print(fruits)
# fruits.extend(["orange","guava"])
# print(fruits)
# fruits[0]="pomigranyt"
# # fruits["apple"]="pomigrante"
# fruits.remove("strawberery")

# print(fruits)
# import random
# names=input("give me the name who will pay the bill")
# name_list=names.split(",")
# print(name_list)
# random_choice=random.randint(0,len(name_list)-1)
# print(f"the person who pays the bill {name_list[random_choice]}")
import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game=[rock,paper,scissors]
# userchoice=int(input("type 0,1,2 for rock, paper,scissors"))
# print("your userchoice : ")
# print(game[userchoice])
# computer_choice=random.randint(0,2)
# print("computer choice : ")
# print(game[computer_choice])
# if userchoice==0 and computer_choice==2:
#       print("you win")
# elif computer_choice==0 and userchoice==2:
#       print("computer win")
# elif computer_choice > userchoice:
#       print("you lose")
# elif  userchoice>computer_choice:
#       print("you win")
# elif computer_choice==userchoice:
#       print("draw")
# else:
#       print("`invalid input")

# fruits=["apple","peach","pear"]
# for char in fruits:
#       print(char)
#       print(char+"pie")
# students_heights=[23,34,45,56,54,43,45,76,98]
# for height in students_heights:
#       total_height+=height
# print(total_height)
# height=0
# for students in students_heights:
#       height+=1
# print(f"the total no of students will be {height}")
# print(max(students_heights))
# print(min(students_heights))
# height=0
# for char in students_heights:
#       if char >height:
#             height=char
# print(height)
# sum=0
# for r in range(1,101):
#       if r%2==0:
#        sum+=r
# print(sum)

# for number in range(1,101):
#       if number%3==0 and number%5==0:
#             print("fizzbuzz")
#       elif number%3==0:
#             print("fizz")
#       elif number%5==0:
#             print("buzz")
#       else:
#             print(number)
# def my_function():
#       print("hello world")
#       print("goodbye beautiful")
# my_function()
# def ny_name(first_name,last_name):
#       print(f"My name is {first_name} {last_name}")
# ny_name()


# def greet_with(name,location):
#       print(f"hello {name}")
#       print(f"you are from {location}")
# greet_with("arvind","babrala")
# import math
# height=int(input("enter the height of wall:"))
# width=int(input("enter the width of wall:"))
# coverage =5
# def paint_calc(height,width,coverage):
#    area=height*width
#    no_of_cans=math.ceil(area/coverage)
#    print(f"the no of cans required for painting {no_of_cans}")
# paint_calc(height,width,coverage)
# def prime_number(number):
#       is_prime=True

#       for i in range(2,number):
#             if number%i==0:
#              is_prime=False
#       if is_prime:
#             print("It is prime no.")
#       else:
#             print("It is not a prime number")
      
                  
        
# n=int(input("Enter the no."))
# prime_number(number=n)


# caeser_cipher

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# programming_dictionaery={
#     "bug":"an error in a program that prevents the program from running as expected",
#     "function":"A piece of code that u can easily call over and over again",
#     "loop":"the action of something doing over and over again"

#     }
# print(programming_dictionaery["bug"])
# programming_dictionaery["progaram"]="a pice of code which is developed on the basis of algorithm"
# print(programming_dictionaery) 

# for thing in programming_dictionaery:
#     print(thing)
#     print(programming_dictionaery[thing])

# students_scores={
#     "harry":81,
#     "ron":78,
#      "hermione":99,
#      "Draco":74,
#      "neville":62
# }

# students_grade={}
# def students():
#     for score in students_scores:
#         a=students_scores[score]
#         if a>91 and a<100:
#             students_grade[score]="outstanding"
#         elif a>81 and a<90:
#                  students_grade[score]="exceeds expectation"
#         elif a>71 and a<80:
#                  students_grade[score]="Acceptable"
#         else:
#             students_grade[score]="good"
        
#     print(students_grade)
# students()

# travel_log={
#     "france":["paris","lille","dijon"],
#     "germany":["berlin"]
# }
# programming_dictionaery={
#     "bug":"AN error occured in program that  prevents the program from running as expected ",
#     "function":"a piece of  code that you can call over and over again",
#     "loop":"The action of doing something again and again"
# }

# print(programming_dictionaery["bug"])
# programming_dictionaery["bug"]="The bug is vulnerabilities that occur in program du which error occured in your program"
# print(programming_dictionaery)
# for thing in programming_dictionaery:
#     print(thing)
#     print(programming_dictionaery[thing]
#     )
# empty_dictionaery={}
# empty_dictionaery["function"]="a piece of code that calls itself again and again"

# print(empty_dictionaery)
# students_scores={
#     "harry":81,
#     "ron":78,
#     "hermione":99
# }
# students_grades={}
# for score in students_scores:
#     a=students_scores[score]
#     if a>91 and a<100:
#         students_grades[score]="outstanding "
#     elif a>80 and a<90:
#         students_grades[score]="exceeds expectation"
#     elif a>71 and a<80:
#         students_grades[score]="Acceptable"
# print(f"students_grades :{students_grades}")

# travel_log=[
# {
#     "country":"france",
#     "cities_visited":["paris","lille","dijon"],
#     "total_visited":12
# },
# {
#     "country":"germany",
#     "cities_visited":["berlin","hamburg","stuttgart"],
#     "total_visited":14
# },
# ]

# new_country={}
# def add_new_country(country,cities_visited,visits):
#     new_country["country"]=country
#     new_country["cities_visited"]=cities_visited
#     new_country["visits"]=visits
#     travel_log.append(new_country)
#     print(travel_log)

# add_new_country("russia",["moscow","saint petersburg"],11)
# black_jack capstone 
# import random

# def deal_cards():
#   card=[11,2,3,4,5,6,7,8,9,10,10,10]
#   cards=random.choice(card)
#   return cards


# def calculate_score(cards):

#     if sum(cards) == 21 and len(cards)==2:
#          return 0
#     if 11 in  cards and sum(cards)>21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards) 

# def compare(user_score,computer_score):
#     if user_score==computer_score:
#         return "draw"
#     elif computer_score==0:
#         return "apponent win with thw blackjack"
#     elif user_score==0:
#         return "win with the  blackjack "
#     elif  user_score>21:
#         return "u went over ,u loose"
#     elif computer_score>21:
#         return "opponent went over . You win"
#     elif user_score>computer_score:
#         return "you win"
#     else:
#         return "u loose"
# def play_game():
#     user_cards=[]
#     computer_cards=[]
#     is_gameover=False
#     for _ in range(2):
#         user_cards.append(deal_cards)
#         computer_cards.append(deal_cards)
#     while not is_gameover:    
#         user_score=calculate_score(user_cards)
#         computer_score=calculate_score(computer_cards)
#         print(f" your cards :{user_cards}, current score : {user_score}")
#         print(f" your cards :{computer_cards}, current score : {computer_score}")

#         if user_score==0 and computer_score==0 or user_score>21:
#             is_gameover=True
#         else:
#             user_should_deal=input("type 'y' to get another card,type ,type 'n' to pass : ")
#             if user_should_deal=="y":
#                 user_cards.append(deal_cards())
#             else:
#                 is_gameover=True
#     while computer_score!=0 and computer_score<17:
#         computer_cards.append(deal_cards())
#         computer_score=calculate_score(computer_cards)
#     print(f"tour final hand : {user_cards}, final score: {computer_score}")  
#     print(f"user final hand : {user_cards},your final score : {computer_score}")
#     print(compare(user_score,computer_score))
# while input("do u want play game ") =="y":
#         play_game()
# print(user_cards)
# print(computer_cards)

    
# user_cards=[]
# computer_cards=[]
# for _ in range(2):
#     new_cards=deal_cards()
#     user_cards.append(new_cards)
#     computer_cards.append(deal_cards)
# def calculate_scores(cards):
#     if sum(cards)==21 and len(cards)==2:
#         return 0
#     if 11 in cards and sum(cards)>21:
#         cards.remove(11)
#         cards.append(1)
#      return sum(cards)
# for i in range(5,0):
#     for j in range(0,5):
#       print(i)
#     print("\n")


# from turtle import Turtle, Screen
# ankit=Turtle()
# my_screen=Screen()
# print(my_screen.canvheight)
# ankit.shape("turtle")
# ankit.color("red")
# for char in range(4):
#     ankit.forward(100)
#     ankit.left(90)
# my_screen.exitonclick()

import aryan
print(aryan.brother)






























































































































