# states_of_america=["pennsylvania","taxes","california"]
# states_of_america.append("arizona")
# states_of_america.extend(["Nevada","North carloina"])
# states_of_america[0]="alaska"
# print(states_of_america)
# import random
# name=[]
# for char in range(2):
#     name.append(input("enter your name"))
# print(name)
# a=random.choice(name)
# print(f"the person who pays the bill will be ={a}")
# fruits=["guava"]
# vegetables=["ladyfinger"]
# dirty_dozen=[fruits,vegetables]
# print(dirty_dozen)
# from tkinter import N


# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# mao=[row1,row2,row3]
# choice=input("enter where u want to put your no. ")
# horizontal=int(choice[0])
# vertical=int(choice[1])
# map[vertical-1][horizontal-1]="X"
# print(f"{row1}\n {row2}\n {row3}")

# height=int(input("enter your height : "))
# age=int(input("enter your age : "))
# amount=0
# if height>120:
#     print("you can ride")
#     if age<12:
#       amount+=5
#     elif age>12 and age < 18:
#         amount+=7
#     elif age>18:
#         amount+=12

# else:
#     print("you cant ride")
# if input("u want photos")=="yes":
#     amount+=3
    
# print(f"The total bill will be ${amount}")
# year=int(input("enter the year you want to check : "))
# if year %4==0:
#    if year %100==0:
#        if year%400==0:
#            print("leap year ")
#        else:
#            print("not leap year : ")
#    else:
#         print(" leap year")
# else:
#     print("not leap year")
# name=input("enter yor name : ").lower()
# n_name=input("enter there name ").lower()
# l=name.count("l")
# fruits = ["apple","mango","gauva"]
# for c in fruits:
#     print(c)
# def prime_checker(number):
#     is_prime=True
#     for i in range(2,number):
#         if number%i==0:
#             is_prime=False
#     if is_prime:
#         print("It is a prime number ")
#     else:
#         print("it is not a prime number ")

# n=int(input("enter the number : "))
# prime_checker(n)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# text=input("enter the text : ")
# amount=int(input("enter the number : "))
# direction=input(" what do you want encode or decode :").lower()
# def ceaser(end_text,shift_amount,direction):
#     start_text=""
#     if direction=="decode":
#         shift_amount*=-1
#     for char in  end_text:
#        position=alphabet.index(char)
#        new_position=position+shift_amount
#        letter=alphabet[new_position]
#        start_text+=letter
#     print(f"The text with {direction} direction is : {start_text}")
    
# ceaser(text,amount,direct
# from turtle import Turtle , Screen
# screen = Screen()
# screen.setup(height=600, width=600)
# screen.bgcolor("black")
# screen.title("My snake Game")

# segmen_1=Turtle("square")
# segment_1.color("white")
# screen.exitonclick()
# programming_dictionaery={
#     "bug":"an error in a program  that prevents the program from running as expected",
#     "function" : "A piece of code that you can easily call over again"
# }
# programming_dictionaery["loop"]="The action of doing something over and over again"
# print(programming_dictionaery)
# student_score={
#     "harry":81,
#     "ron":78,
#     "hermione":99,
    
# }
# students_grades={}
# def students(student_score):
#     for char in student_score:
#         score=student_score[char]
#         if score >91 and score<100:
#              students_grades[char]="outstaning"
#         elif score>81 and score <90:
#             students_grades[char]="exceeds Expectations"
#         elif score>70:
#             students_grades[char]="accepectable"
#         else:
#             print("fail ")

# students(student_score)
# print(students_grades)
# travel_log=[
#     {"france":{"cities_visited":["paris","little","Dijon"],"total_visited":12},
#     "germany":{"cities_visited":["Berlin","hamsburg","stuttgart"],"total_visited":10},
    
# ]
# def highest_bid(bids):
#     highest=0
#     for char in bids:
#         score=bids[char]
#         if highest<score:
#             highest=score
#         print(f"The winner of secret auction with {highest} bid is {char} ")

# bids={}
# not_finished=True
# while not_finished:
#     name=input("what is your name : ")
#     bid=int(input("what is your bid : "))
#     bids[name]=bid
#     if input("are there are any bis ? : ")=="no":
#         highest_bid(bids)
        
#         not_finished=False

# def format_name(f_name,l_name):
#       f_name=f_name.title()
#       l_name=l_name.title()     
#       return f"{f_name} {l_name} "
  
# a=format_name("arvind","kumar")
# print(a)

# def leap(year):
#     if year%4==0:
#         if year%100:
#             if year%400:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# def days_in_months(year,month):
#     month_days=[31,28,31,30,31,31,31,30,31]
#     if leap(year):
#         return 29
#     return month_days[month -1]
    
    
    
    
    
    
# year=int(input("Enter a year : "))
# month=int(input("Enter the month : "))
# days=days_in_months(year,month)
# print(days)
  

# def add(n1,n2):
#     return n1+n2
# def sub(n1,n2):
#     return n1-n2
# def  div(n1,n2):
#     return n1/n2
# def mul(n1,n2):
#     return n1*n2


# operations={
#     "+":add,
#     "-":sub,
#     "*":mul,
#     "/":div
# }

# n1=int(input("enter the first number"))
# is_continue=True
# while is_continue:
#     print("choose the  operations : ")
#     for char in operations:
#         print(char)
#     symbol=input("choose your symbol : ")
#     n2=int(input("enter your next number : "))
#     calculations=operations[symbol]
#     answer=calculations(n1,n2)
#     print(f"{n1}{symbol}{n2}={answer}")
#     if input("do you want to continue: ")=="yes":
#        n1=answer
#     else:
#         is_continue=False
        
# print(len("hello" +input("what's your name")))
# from re import A




# print(f"a={a}")
# print(f"b={b}")
# name=input("what is your name")
# pet=input("what is your pet name")
# print("your band name will be : ",
#       name+pet)

# print("Welcome to the rollercoaster. ")
# height=int(input("What is your height in cm  "))

# if height>120:
#     print("You can ride the rollercoaster ")
# else:
#     print("you can not ride the rollercoaster")
    
# height=int(input("enter the height :  "))
# age=int(input("enter your age : "))
# amount=0
# if height>120:
#     print("you can ride rollercoaster")
#     if age >18:
#         amount+=12
#         print(amount)
#     elif age==18 or age<18:
#         amount+=7
#         print(amount)
# else:
#     print("you can'nt ride a rollercoaster ")       

# height=int(input("enter your height : ")) 
# weight=int(input("enter your weight : "))   
# bmi=round(weight/height**2,2)
# print(f"The bmi will be {bmi}")
# if bmi<18.5:
#     print("they are underweight")
# elif bmi>18.5 and bmi<25:
#     print("They have normal weight ")
# elif bmi>25 and bmi<30:
#     print("they are overweight ")
# elif bmi>30 and bmi<35:
#     print("they are obese ")
# else:
#     print("They are clinically obese")
  
# year=int(input("enter the year :"))  
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap year")
#         else:
#             print("Not a leap Yeap Year")
#     else:
#         print("leap Year")
# else:
#     print("Not a leap Year ")
    
      
# name1=input("enter your name : ")
# name2=input("enter your name : ")
# name=name1+name2
# t=name.lower().count("t")
# r=name.lower().count("r")
# u=name.lower().count("u")
# e=name.lower().count("e")
# true=t+r+u+e
# l=name.lower().count("l")
# o=name.lower().count("o")
# v=name.lower().count("v")
# e=name.lower().count("e")
# love=l+o+v+e
# love_score=str(true)+str(love)
# print(love_score)

# fruits=["cherry","apple","pear"]
# fruits[0]="mango"
# fruits.append("cherry")
# fruits.extend(["leach","pomegrante","banana"])
# fruits.remove("cherry")
# print(fruits)

# str="hello,from,arvind"
# a=str.split(",")
# print(a) 
# import random

# from blackjack capstone project import calculate_score
# name=input("enter your name separrated by commas: ")
# a=name.split(",")
# print(a)

# person_who_pays=random.randint(0,2)
# print(f"person who pays the bill : {a[person_who_pays]}")

# fruits=["strawberries","Apples","Grapes","peaches"]
# vegetables=["spinach","kale"]
# dirty_dozen=[fruits,vegetables]
# print(dirty_dozen)

# row1=["⬜","⬜","⬜"]
# row2=["⬜","⬜","⬜"]
# row3=["⬜","⬜","⬜"]
# map=[row1,row2,row3]
# vertical=int(input("enter the row: "))
# horizontal=int(input("Enter the column :  "))
# map[horizontal-1][vertical-1]="X"
# print(f"{row1}\n{row2}\n{row3}")
# print(len("hello"))
# print("HELLO"[-1])

# a=input("enter the no.")
# b=input("enter the second No. ")

# print(int(a)+int(b))
# weight=int(input("Enter the weight in kg: "))
# height=float(input("enter the height of person : "))
# bmi=weight/height**2
# print(int(bmi))
# 
# year=int(input("enter the year : "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("ints a leap year ")
#         else:
#             print("its not a leap year ")
#     else:
#         print("its a leap year ")
# else:
#     print("its not a leap year ")
# age=int(input("enter the age : "))
# height=int(input("enter the height : "))
# bill=0
# if height>120:
#     print("can ride")
#     if age <12:
#         bill+=5
#     elif age>12 and age<18:
#         bill+=7
#     else:
#         bill+=12
# want_photo=input("if you want photo yes or no : ").lower()
# if want_photo=="yes":
#     bill+=3
# print(f"The total bill will be ${bill}")
# import random
# a=random.randint(0,1)
# if a==0:
#     print("its tail")
# else:
#     print("its head")
# fruits=["cherry","mango","orange"]
# fruits.append("apple")
# print(fruits)
# fruits.extend(["pineapple","Date"])
# print(fruits)
# fruits[0]="pomegranate"
# fruits.remove("apple")
# print(fruits)
# import random
# name=input("enter thge name ,separated by commas : ")
# a=name.split(",")
# choice=random.randint(0,2)
# print(a[choice])
        
# row1=["⬜","⬜","⬜"]
# row2=["⬜","⬜","⬜"]
# row3=["⬜","⬜","⬜"]
# map=[row1,row2,row3]
# vertical=int(input)
# total=0
# for num in range(2,101,2):
   
#         total+=num
    
# print(total)

# for num in range(1,101):
#     if num%3==0:
#         print("fizz")
#     elif num%5==0:
#         print("buzz")
#     elif  num%3==0 and num%5==0:
#         print("fizzbuzz")
#     else:
# #         print(num)
# import random
# letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']  
# print("welcome to the password generator  ")
# nr_letters=int(input("any letters do u want in your password"))
# nr_numbers=int(input("any numbers do u want in yourt password "))
# nr_symbols=int(input("any symbols do you want in your password "))
# password=[]
# for char in range(0,nr_letters):
#     password.append(random.choice(letters))
    
# for char in range(0,nr_numbers):
#     password.append(random.choice(numbers))
    
# for char in range(0,nr_symbols):
#     password.append(random.choice(symbols))
    
# random.shuffle(password)
# passw=""
# for char in password:
#     passw+=char
# print(passw)
# print(f"{''.join(password)}")
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
# #   O   |
# #  /|\  |
# #       |
# #       |
# # =========
# # ''', '''
# #   +---+
# #   |   |
# #   O   |
# #  /|   |
# #       |
# #       |
# # =========''', '''
# #   +---+
# #   |   |
# #   O   |
# #   |   |
# #       |
# #       |
# # =========
# # ''', '''
# #   +---+
# # #   |   |
# # #   O   |
# # #       |
# # #       |
# # #       |
# # # =========
# # # ''', '''
# # #   +---+
# # #   |   |
# # #       |
# # #       |
# # #       |
# # #       |
# # # =========
# # # ''']
# word_list=["reaper","karan","apple","cat","man"]
# random_word=random.choice(word_list)
# print(f"the right chosen word is : {random_word}")
# lives=6
# blank=[]
# for letter in random_word:
#     blank+="_"
# print(blank)

# is_true=False
# while not is_true:
#     guess=input("guess the letter : ").lower()
#     for position in range(len(random_word)):
#         letter=random_word[position]
#         if guess==letter:
#             blank[position]=guess
            
#     if guess not in random_word:
#         lives-=1
#         if lives==0:
#             is_true=True
#             print("you lose")
             
#     print(blank)   
#     if "_" not in blank:
#         is_true=True
#         print("you won")
#         print(f"{''.join(blank)}")

#     print(stages[lives])
    
# def greet(first_name,last_name):
#     print(f"hello {first_name} {last_name}")

# greet(last_name="Arvind",first_name ="kumar")
# import math
# def paint_area(height,width,coverage):
#     area=math.ceil((height*width)/coverage)
#     print(f"the canvas required for coverage will be : {area}")
    


# height=int(input("enter the height of wall : "))
# width=int(input("enter the width of wall : "))
# coverage=5
# paint_area(height,width,coverag


# def prime_checker(num):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#     if is_prime:
#         print("its a prime number ")
#     else:
#          print("Its not a prime no. ")
         
# num=int(input("enter the number do you want to check : "))
# prime_checker(num)


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def caeser(text,shift,direction):
#     direction=input("enter direction encypt/decrypt: ").lower()
#     text = input("enter the text:  ")
#     shift=int(input("enter the shift no : "))
#     start_text=''
#     if direction=="decode":
#             shift*=-1
#     for char in text:
#         position=alphabet.index(char)
       
#         new_position=position+shift
#         letter=alphabet[new_position]
#         start_text+=letter
#     print(f"The {direction} of text : {start_text}")
#     if input("want to continue : ")=="yes":
#         caeser(text,shift,direction)
        
        
# programming_dictionaery={
#     "bug":"An error in a program that prevents the program from running as expected",
#     "Function":"A piece of code that you can easily call over and over again",
#     "loop":"The action of doing something over and over again"
# }

# studenyts_scorers={
#     "Harry":81,
#     "ron":78,
#     "Hermonine":99,
#     "Draco":74,
#     "neville":62
# } 
# students_grades={}
# for students in studenyts_scorers:
#     score=studenyts_scorers[students]
#     if score>90:
#         students_grades[students]="outstanding"
#     elif score<90 and score>80:
#         students_grades[students]="exceeds expectation"
#     elif score<80 and score>70:
#         students_grades[students]="Acceptable"
#     else:
#         students_grades[students]="fail"
        
    
# print(students_grades)

# is_true=True
# bids={}
# while is_true:
#     name=input("enter your name : ")
#     bid=int(input("enter the bid : "))
#     bids[name]=bid
#     if input("any other users who want to bid : ")=="no":
#         highest_bid=0
#         for high in bids:
#             score=bids[high]
#             if score>highest_bid:
#                 highest_bid=score
#         print(f"the winner of highest bid {highest_bid} is {high}")
    
# def formatted_name(f_name,l_name):
#     formatted_fname=f_name.title()       
#     formatted_lname=l_name.title()
#     return f"{formatted_fname} {formatted_lname}"

# a=formatted_name("arvind","KUMAR")
# print(a)
  
# def leap_year(year):
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 return True
#         else:
#             return False
#     else:
#         return True

    
    
# def days_in_months(year,month):
#     month_days=[31,28,30,31,30,31,31,30,30,31]
#     if leap_year(year) and month==2:
#         return 29
#     return month_days[month-1]
        
        
    # year=int(input("enter the year : "))
# month=int(input("enter the month : "))
# days_in_months(year,month)
# print(days_in_months)

# def add(n1,n2):
#     return n1+n2

# def sub(n1,n2):
#     return n1-n2

# def div(n1,n2):
#     return n1/n2

# def mul(n1,n2):
#     return n1*n2

# operation={
#     "+":add,
#     "-":sub,
#     "/":div,
#     "*":mul
# }
# def cal():
#  num1=int(input("enter the first number  : "))
#  want_continue=True
#  while want_continue:
#     num2=int(input("enter the next number : "))
#     for symbol in operation:
#       print(symbol)
#     operational_symbol=input("pick any symbol")
#     calculation=operation[operational_symbol]
#     answer=calculation(num1,num2)
#     print(f"{num1}{operational_symbol}{num2}={answer}")
#     if input("do you want to continue")=="yes":
#         num1=answer



import random




# HARD_LEVELS=10
# EASY_LEVELS=5

# def set_difficulty():
#     choose=input("choose diffculty level : ")
#     if choose.lower()=="easy":
#         return EASY_LEVELS
#     else:
#        return HARD_LEVELS

# def calculate(guess,answer,turn):
#     if guess>answer:
#         print("its too high ")
#         return turn-1
#     elif guess<answer:
#         print("its too low")
#         print("guess again")
#         return turn-1
#     else:
#         print("you guesssed perfectly")
# def play_game():
#     print("welcome to the guessing game! ")
#     print("Think number between 1 to 100")
#     answer=random.randint(1,100)
#     print(f"{answer}")
#     turn=set_difficulty()
#     guess=0
#     while guess!=answer:
     
#      print(f"you have {turn} attempt remaining ")
#      guess=int(input("guess the number : "))
#      calculate(guess,answer,turn)
     
# logo = """
#     __  ___       __             
#    / / / (_)___ _/ /_  ___  _____
#   / /_/ / / __ `/ __ \/ _ \/ ___/
#  / __  / / /_/ / / / /  __/ /    
# /_/ ///_/\__, /_/ /_/\___/_/     
#    / /  /____/_      _____  _____
#   / /   / __ \ | /| / / _ \/ ___/
#  / /___/ /_/ / |/ |/ /  __/ /    
# /_____/\____/|__/|__/\___/_/     
# """

# vs = """
#  _    __    
# | |  / /____
# | | / / ___/
# | |/ (__  ) 
# |___/____(_)
# """

# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Ariana Grande',
#         'follower_count': 183,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 181,
#         'description': 'Actor and professional wrestler',
#         'country': 'United States'
#     },
#     {
#         'name': 'Selena Gomez',
#         'follower_count': 174,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kylie Jenner',
#         'follower_count': 172,
#         'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kim Kardashian',
#         'follower_count': 167,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Lionel Messi',
#         'follower_count': 149,
#         'description': 'Footballer',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Beyoncé',
#         'follower_count': 145,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Neymar',
#         'follower_count': 138,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'National Geographic',
#         'follower_count': 135,
#         'description': 'Magazine',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Bieber',
#         'follower_count': 133,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Taylor Swift',
#         'follower_count': 131,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kendall Jenner',
#         'follower_count': 127,
#         'description': 'Reality TV personality and Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Jennifer Lopez',
#         'follower_count': 119,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Nicki Minaj',
#         'follower_count': 113,
#         'description': 'Musician',
#         'country': 'Trinidad and Tobago'
#     },
#     {
#         'name': 'Nike',
#         'follower_count': 109,
#         'description': 'Sportswear multinational',
#         'country': 'United States'
#     },
#     {
#         'name': 'Khloé Kardashian',
#         'follower_count': 108,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Miley Cyrus',
#         'follower_count': 107,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Katy Perry',
#         'follower_count': 94,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kourtney Kardashian',
#         'follower_count': 90,
#         'description': 'Reality TV personality',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kevin Hart',
#         'follower_count': 89,
#         'description': 'Comedian and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Ellen DeGeneres',
#         'follower_count': 87,
#         'description': 'Comedian',
#         'country': 'United States'
#     },
#     {
#         'name': 'Real Madrid CF',
#         'follower_count': 86,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'FC Barcelona',
#         'follower_count': 85,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'Rihanna',
#         'follower_count': 81,
#         'description': 'Musician and businesswoman',
#         'country': 'Barbados'
#     },
#     {
#         'name': 'Demi Lovato',
#         'follower_count': 80,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': "Victoria's Secret",
#         'follower_count': 69,
#         'description': 'Lingerie brand',
#         'country': 'United States'
#     },
#     {
#         'name': 'Zendaya',
#         'follower_count': 68,
#         'description': 'Actress and musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Shakira',
#         'follower_count': 66,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Drake',
#         'follower_count': 65,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Chris Brown',
#         'follower_count': 64,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'LeBron James',
#         'follower_count': 63,
#         'description': 'Basketball player',
#         'country': 'United States'
#     },
#     {
#         'name': 'Vin Diesel',
#         'follower_count': 62,
#         'description': 'Actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cardi B',
#         'follower_count': 67,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'David Beckham',
#         'follower_count': 82,
#         'description': 'Footballer',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Billie Eilish',
#         'follower_count': 61,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Timberlake',
#         'follower_count': 59,
#         'description': 'Musician and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'UEFA Champions League',
#         'follower_count': 58,
#         'description': 'Club football competition',
#         'country': 'Europe'
#     },
#     {
#         'name': 'NASA',
#         'follower_count': 56,
#         'description': 'Space agency',
#         'country': 'United States'
#     },
#     {
#         'name': 'Emma Watson',
#         'follower_count': 56,
#         'description': 'Actress',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Shawn Mendes',
#         'follower_count': 57,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Virat Kohli',
#         'follower_count': 55,
#         'description': 'Cricketer',
#         'country': 'India'
#     },
#     {
#         'name': 'Gigi Hadid',
#         'follower_count': 54,
#        'description': 'Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Priyanka Chopra Jonas',
#         'follower_count': 53,
#         'description': 'Actress and musician',
#         'country': 'India'
#     },
#     {
#         'name': '9GAG',
#         'follower_count': 52,
#         'description': 'Social media platform',
#         'country': 'China'
#     },
#     {
#         'name': 'Ronaldinho',
#         'follower_count': 51,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'Maluma',
#         'follower_count': 50,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Camila Cabello',
#         'follower_count': 49,
#         'description': 'Musician',
#         'country': 'Cuba'
#     },
#     {
#         'name': 'NBA',
#         'follower_count': 47,
#         'description': 'Club Basketball Competition',
#         'country': 'United States'
#     }
# ]
# print(logo)
# def compare(guess,follower_a,follower_b):
#     if follower_a>follower_b:
#         return guess=="a"
#     else:
#         return guess=="b"
# is_gameover=False
# while not is_gameover:
#     account_a=random.choice(data)
#     account_b=random.choice(data)
#     if account_a==account_b:
#         accoun_b=random.choice(data)
#     name_a=account_a["name"]
#     description_a=account_a["description"]
#     country_a=account_a["country"]
#     print(f"NAME: {name_a},description: {description_a},country: {country_a}")
#     print(vs)
#     name_b=account_b["name"]
#     description_b=account_b["description"]
#     country_b=account_b["country"]     
#     print(f"Name: {name_b},description: {description_b},country:{country_b}")
#     guess=input(f"which celebrity/player have more no of instagram flower a/b: ").lower()
#     follower_a=account_a["follower_count"]
#r     follower_b=account_b["follower_count"]
#     answer=compare(guess,follower_a,follower_b)
#     if answer:
#         print("you have got it right ")
#     else:
#         print("you have got it wrong")
#     if input("you want to continue").lower()=="no":
#         is_gameover=True
# resources={
#     "water":300,
#     "milk":100,
#     "coffe":100,
#     "money":0
# }    
# profit=0

# for char in resources:
#        print(f"")

# from list import pi
# print(pi)

# revision2

# print("print('arvind')
# print("hello world")
# print("day-1 python print function")
# print("The function is decared like this : ")
# print("print('what to print')")
# print("hello"+" "+"angela")
# print(len(input("what is your name : ")))
# name="jack"
# print(name[0])
# print("Enter the number for swapping : ")
# a=int(input("enter first number :" ))
# b=int(input("enter the second number : "))
# c=a
# a=b
# b=c
# print(f"a={a}")
# print(f"b={b}")
# print("welcome to the band name genrator : ")
# name=input("enter your name : ")
# pet = input("enter your pet name : ")
# # print(" your band name genrator will be :" {name}{+}{pet}

# for i in range(5):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("\r")
# a=input("enter two digit number : ")
# print(int(a[0])+int(a[1]))
# weight=float(input("enter the weight in kg : "))
# height=int(input("enter the height in cm : "))
# bmi=weight/height**2
# print(round(bmi,2))
# age=int(input("what is your age : "))
# year_remaining=90-age
# days_remaining=year_remaining*365
# weeks_remaining=year_remaining*52
# months_remaining=year_remaining*12
# print(f'you have {year_remaining} years remaining ,{months_remaining} months remaining and {days_remaining} days remaining')
# height=int(input("enter the height in cm : "))
# if height>120:
#     print()
# print("Day 1 - Python print function ")
# print("The function is decalared like this : ")
# print('print("what to print")')
# print("hello"+" "+"arvind ")
# a=input("what is your name : ")
# print(a)
# print("hello"+input("what is your name : "))
# print(len(input("wnat is your name : ")))
# a=float(input("enter whatever u want to enter : "))
# print(type(a))
# a=input("a:")
# b=input("b:")
# c=a
# a=b
# b=c
# print(f"a: {a}")
# print(f"b:{b}")

# print("welcome to the band na me generator")
# city=input("enter the name of the city in which you grew up : ")
# pet=input("enter your pet name : ")
# print(f"your band name will be : {city+pet}")
# num=input("Enter the two digit no. : ")
# print(int(num[0])+int(num[1]))
# height=int(input("enter your height in cm : "))
# weight=int(input("enter your weight in kg : "))
# bmi=weight/height**2
# print(f"bmi={bmi}")






