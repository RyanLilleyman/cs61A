def f1():
    return (lambda x: x)(3)

print(f1())

def f2():
    return lambda: 3

print(f2()())

def f3():
    return lambda x: x

print(f3()(3))


def f4():
    return lambda: lambda x: lambda: 3

print(f4()()(3)())