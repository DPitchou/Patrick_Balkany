class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
         return f'x = {self.x}, y = {self.y}'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        self.x += other.x
        self.y += other.y


p = Point(1, 3)
q = Point(2, 6)

print(p)
print(q==p)
p.__add__(q)
print(q)
print(p==q)
q.__add__(p)
print('Après addition des points ')
print(p)
print(q)

