def prime_checker(number):
    is_prime=True
    for i in range(2,number):
     if number%i==0:
         is_prime=False
     if is_prime:
         print("its a prime no.")
     else:
         print("Its not a prime no.")

n=int(input("enter the no."))
prime_checker(number=n)