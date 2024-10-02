import math

def fun(x):
    return (1.7 * math.pow(x,5) - 3.2 * math.pow(x,4) - 9.6 * x - 27.3)

def fi(x):
    return ((3.2 * x ** 4 + 9.6 * x + 27.3) / 1.7) ** (1/5)

eps = 0.000001
x0 = -10
x1 = 100000

#changes

while True:
    if abs(fun(x0) - fun(x1)) < eps:
        print("корень =", x0)
        break
    else:
        tmp = x1
        x1 = fi(x0)
        x0 = tmp

print("значение функции в найденной точке", fun(x0))




