
from operator import add, mul, mod

def curry(operator):
    def keep1(x):
        def keep2(y):
            return operator(x, y)
        return keep2
    return keep1

curried_add = curry(add)
add_three = curried_add(3)
print(add_three(5))

 


    