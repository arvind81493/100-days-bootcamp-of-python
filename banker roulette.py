import random
names=input("give your names which should be separated by commas ")
name=names.split(",")
# a=len(name)
# random_choice=random.randint(0,a-1)
# whopaysbill=name[random_choice]      1sr method
# print(f"{whopaysbill} is the person who pays bill")
a=random.choice(name)
print(f"{a} will we paying the bill of meal today") #2nd method
