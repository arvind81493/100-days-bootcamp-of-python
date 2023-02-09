logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add (n1,n2):
   return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
    should_continue=True
    num1=int(input("what the first number?: "))
    # num2=int(input("what the aecond number?: "))
    for symbol in operations:
     print(symbol)
    while should_continue:
    # operation_symbol=input("pick an operation from the above line :")
    # function_cal=operations[operation_symbol]
    # answer_first=function_cal(num1,num2)
    # print(f"{num1}{operation_symbol}{num2}={answer_first}")

        operation_symbol=input("pick another operation")
        num3=int(input("what is your next number?: "))
        function_cal=operations[operation_symbol]
        answer=function_cal(num1,num3)
        print(f"{num1}{operation_symbol}{num3}={answer}")
        a=input("type 'yes' if u want to continue to calculate or 'no' if u dont want to calculate")
        if a=="yes":
            should_continue=True
        else:
            should_continue=False 
            calculator()

calculator()
            

