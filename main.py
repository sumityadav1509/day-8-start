def prime_number_check(n): 
 is_prime=True
 for i in range(2,n-1):
   if n%i==0:
    is_prime=False
 if is_prime:
    print("It's a Prime Number. ")
 else:
    print("It's not a Prime Number. ")      




prime_number_check(n=int(input("Please input a number: ")))
