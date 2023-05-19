def make_keeper(n):
    def f(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)
    return f


def is_even(x):
    return x%2 == 0

make_keeper(5)(is_even)