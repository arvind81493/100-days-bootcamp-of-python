import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to the password generator")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#                        *easy level password 
# password=""
# for char in range(1,nr_letters+1):
#     random_char=random.choice(letters)
#     password+=random_char
#     print(password)
# for char in range(1,nr_symbols+1):
#      password+=random.choice(symbols)
#      print(password)
# for char in range(1,nr_numbers+1):
#     password+=random.choice(numbers)
# print(password)

#         *hardlevel password


password=[]
for char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password.append(random_char)
    print(password)
for char in range(1,nr_symbols+1):
     password+=random.choice(symbols)
     print(password)
for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)
print(password)
random.shuffle(password)

print(f"{''.join(password)}")
# passwrd=""
# for char in password:
#     passwrd+=char

# print(f"your password is {passwrd}")

# password=""
# for char in range(1,nr_letters+1):
#     password+=random.choice(letters)

# for char in range(1,nr_symbols+1):
#     password+=random.choice(symbols)

# for char in range(1,nr_numbers):
#     password+=random.choice(numbers)


# print(f"your password will be {password}")

#    *strong password
