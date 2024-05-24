from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
from math import pi
a = 0
b = pi/2
n=100
h=(b-a)/n
x=0
for i in range(n):
    a1=a+i*h
    a2=a+(i+1)*h
    s=(a2-a1)*(sin(a1)+sin(a2))/2
    x+=s

print(x)