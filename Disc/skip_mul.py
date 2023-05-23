def skip_mul(n):

    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n-2)
    
print(skip_mul(5))