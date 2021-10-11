import math

def cercle(x, y, R):
    print("x=", x, "y=", y, "R=", R, "Aire=", math.pi * R ** 2, "distance par rapport au centre=", (x ** 2 + y ** 2) ** 0.5)


def carré(x, y, L):
    print("x=", x, "y=", y, "L=", L, "Périmètre=", 4 * L, "Aire=", L ** 2, "distance par rapport au centre=", ((x + L / 2) ** 2 + (y + L / 2) ** 2) ** 0.5)


if __name__ == "__main__":
    x = 0
    y = 0
    R = 1
    L = 1

    cercle(1, 2, 3)
    cercle(x, y, R=6)
    carré(1, 2, 3)
    carré(x, y=-2, L=13.5)






