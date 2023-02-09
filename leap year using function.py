def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
              return False
        else:
             return True
    else:
        return False


def days_of_month(year,month):
    if month>12 or month<1:
        return f"invalid input "
    months_days=[31,28,31,30,31,30]
    if is_leap(year) and month==2:
        return 29
    return months_days[month-1]

year=input("enter the year :")
month=input("enter the month")
days=days_of_month(year,month)
print(days)