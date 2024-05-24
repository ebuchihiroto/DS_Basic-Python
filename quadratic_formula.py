a = 1
b = -6
c = 9

# TODO
def calc(a, b, c):
    x1 = ( -b + (b ** 2 - 4 * a * c) ** 0.5 ) / (2 * a)
    x2 = ( -b - (b ** 2 - 4 * a * c) ** 0.5 ) / (2 * a)
    print(x1, x2)

calc( 1, -6, 9 )
calc( 1, 2, -8 )
calc( 8, -6, -35 )
calc(1, 0 , 1)