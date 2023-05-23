def isPrime(n):
    def checker(i):
        if i < n and n % i == 0:
            return False
        elif i >= n:
            return True
        else:
            return checker(i+1)

    i = 2
    if n < 2:
        return False
    elif n == 2: 
        return True
    else:
        return checker(i)
        
    
print(isPrime(521))