import sys

def second(a, b, c):
    d = (b ** 2) - 4 * a * c

    if (a, b, c) == ( 0, 0, 0):
        print("R")
    elif (a, b) == (0, 0):
        print("0")
    elif a == 0:
        print(- c / b)
    elif d == 0:
        print(- b / (2 * a))
    elif d > 0:
        print(- b + (d ** (1 / 2)) / (2 * a))
        print(- b - (d ** (1 / 2)) / (2 * a))
    else:
        print("Complexe")

second(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))

