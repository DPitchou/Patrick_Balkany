class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f'x = {self.x}, y = {self.y}')

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            print('Les deux point sont les mêmes ')
        else:
            print('Les points sont different')

    def __add__(self, other):
        self.x += other.x
        self.y += other.y


p = Point(1, 3)
q = Point(2, 6)

p.__str__()
p.__eq__(q)
p.__add__(q)
q.__str__()
q.__eq__(p)
q.__add__(p)
print('Après addition des points ')
q.__str__()
p.__str__()

