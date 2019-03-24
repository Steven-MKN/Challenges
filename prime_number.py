def is_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

for a in range(1,100):
    print(str(a) + ' is prime = '+str(is_prime(a)))