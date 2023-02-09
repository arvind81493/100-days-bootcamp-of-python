height=int(input("enter your height in cm "))
bill=0
if height>120:
    print("you can ride on rollar coaster ")
    age=int(input("enter your age"))
    if age<12:
        bill=3
        print("you have to pay $3")
    elif age<=18:
          bill=7
          print("please pay $7") 
    elif age<22:
        bill=30
        print("u have to pay $30")
    elif age>=45 and age<=50:
              print("you have free ride.you do not need to pay.")

    photo= input("want photo ? yes or no.")
    if photo=="yes":
            bill+=3
            
    print(f"your final bill is {bill}")

        
else:
     print("you cannot ride on rollar coaster") 
