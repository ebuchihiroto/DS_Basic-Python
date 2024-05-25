a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

import random


def euclid(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def calc(a, b):
    euclid(a, b)
    if euclid(a ,b) == 1:
        return True
    else:
        return False

print(euclid(int(a), int(b)))
calc(int(a), int(b))
x ,y = 0 ,0
for i in range(100000):
    a ,b = random.randint(1, 10000), random.randint(1, 10000)
    if calc(a, b) == True:
        x += 1
    y += 1

print(x / y)    
