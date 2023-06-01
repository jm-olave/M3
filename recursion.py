
# La capacidad que tiene una funcion de llamarse a si misma


def conteo(n):
    while n > 0:
        print(n)
        n -=1

# conteo(10)

#recursion
def recconteo(n):
    if n <= 0:
        return 0
    print(n)
    recconteo(n-1)
# recconteo(10)

# 0,1,2,3,4,5,6,7,8,9,10
# fibonacchi sequence

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fib(n-2)+ fib(n-1)

print(fib(20))