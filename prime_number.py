a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO


def calc(x):
    if x < 2:
        print("素数ではありません")
        return
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            print("素数ではありません")
            break
    else:
        print("素数です")

calc(int(a))
calc(int(b))