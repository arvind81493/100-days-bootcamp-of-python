print("welcome to the tip calculator.")
bill=float(input("what was your total bill? $"))
tip=int(input("how much tip you want to give ? 10,12,15 "))
people=int(input("how many people between bills should be distributed"))
tipwithbills=tip/100*bill+bill
bill_per_person=tipwithbills/people

print("{:.2f}".format(round(bill_per_person,2)))

