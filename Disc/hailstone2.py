def hailstone(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        print(n)
        n//=2
        return hailstone(n)
    else:
        print(n)
        return hailstone((3*n)+1)
    

print(hailstone(10))