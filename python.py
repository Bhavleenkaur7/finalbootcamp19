def CheckPrime(num):
    if num > 1:
        for i in range[2,num]:
            if (num%i) == 0:
                return false
                break
            else:
                return True







def print_prime_number():
    list = []
    for n in range[1,100]:
        if CheckPrime(n) == True:
            list.append(n)
    print (list)
print_prime_number()
