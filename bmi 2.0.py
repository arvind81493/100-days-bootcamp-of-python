weight=float(input("enter the weight"))
height=float(input("enter the weight"))
bmi=round(weight/height**2)
if bmi<18.5:
    print("they are underweight")
elif bmi<25:
        print("they have normal weight")
elif bmi<30:
            print("they are overweight")
elif bmi<35:
                print("they are obese")
else:
                    print("They are clinically obese")

