from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi , exp

def f(x):
    return sin(x)

def f2(x):
    return 4 / (1 + x ** 2)

def f3(x):
    return (x ** 0.5) * exp( - (x ** 2 ))

def integral(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(n):
       result += h * (f(a + i * h) + f(a + (i + 1) * h)) / 2
    return result

print(integral(f,0,(pi/2),50))
print(integral(f2,0,1,100))
print(integral(f3,-100,100,1000))