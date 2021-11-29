class Polygone():
    def __init__(self, n):
        self.n = n
        self.sides = []

    def inputSides(self):
        for loop in range(self.n):
            self.sides.append(input('Donner une valeur de longueurs souhaitée'))

    def printSides(self):
        for e in range(self.n):
            a = self.sides[e]
            print(f'Longueur de coté {e} est {a}')

class Triangle(Polygone):
    def __init__(self):
        super().__init__(3)

    def is_valid_triangle(self):
        a, b, c = self.sides
        if (a + b) > c and (a + c) > b and (b + b) > a:
            print('Le triangle est valide')

    def findArea(self):
        a, b, c = self.sides
        p = (int(a) + int(b) + int(c) )/ 2
        return (p * (p - int(a)) * (p - int(b)) * (p - int(c))) * 0.5

T = Triangle()
T.inputSides()
T.printSides()
T.is_valid_triangle()
print(T.findArea())



