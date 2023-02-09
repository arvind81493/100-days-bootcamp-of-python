from msilib.schema import Billboard
from re import L


print("welcome to the pizza deliveries!")
size=input("what is the size of pizza ? s,M,or l")
addpeperroni=input("Do u want to add peperroni")
extrachesse=input("do you want extra chesse")
bill=0
if size=="s":
    bill+=15
   
elif size =="M":
    bill+=20
   
elif size=="l":
    bill+=25
    
if addpeperroni=="y":
    if size=="s":
        bill+=2
    else:
            bill+=3
if extrachesse=="y":
    bill+=1
    print(f"your final bill is ${bill}")

