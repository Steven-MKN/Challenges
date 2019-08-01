#Ask the user for a number and determine whether the number is prime or not. 
#(For those who have forgotten, a prime number is a number that has no divisors).

#I adjusted this to check for prime numbers with a given range, just for fun!

def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

for a in range(1,100):
    print(str(a) + ' is prime = '+str(is_prime(a)))
