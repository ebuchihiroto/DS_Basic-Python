a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO


def calc(x):
    try:
        x = int(x)
        if x < 0:
            raise ValueError
        elif x < 2:

            print("素数ではありません")
            return
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                print("素数ではありません")
                break
        else:
            print("素数です")

    except ValueError:
        print("正の整数を入力してください")


calc(a)
calc(b)