year=int(input("which year do you want check "))
if year%4==0:
 if year%100==0:
  if year%400==0:
    print("leap year")
  else:
     print("not leap year")
 else:
    print("its a leap year")
else:
        print("its not a leap year")
