a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO


def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(euclid(int(a), int(b)))
