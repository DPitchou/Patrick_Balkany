import random

class Point:
    total = 0

    def __init__(self, x=0, y=0, id=0):
        self.x = x
        self.y = y
        self.id = id
        Point.total = Point.total + 1

    def display(self):
        print(self.x, self.y)

    def get_id(self):
        print(self.id)

    def __del__(self):
        Point.total -= 1

    @classmethod
    def get_total(cls):
        print(Point.total)

#p1 = Point()
#p1.display()

if __name__ == "__main__":
    liste_point = []
    for n in range(10):
        liste_point.append(Point(random.randint(0, 100), random.randint(0, 100), n))

print("Point 1-------------------")
print("id:")
liste_point[0].get_id()
print("Total:")
liste_point[0].get_total()
print("Point 2-------------------")
print("id:")
liste_point[9].get_id()
print("Total:")
liste_point[9].get_total()

print("Suppression d'un point:")
del liste_point[1]
print("Nouveau total")
Point.get_total()

print("Information du dernier point:")
print("id:")
liste_point[-1].get_id()
print("total")
liste_point[-1].get_total()

