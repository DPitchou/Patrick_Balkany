#EX 1
'''def foo(tab, n):
    z = 0
    for i in tab:
        print(i)
        if n == len(i):
            print(n)
            z += 1
            return z


#EX 2
class A:
    def __init__(self, x, tab):
        self.x = x
        self.__tab = tab

    def foo(self):
        if len(self.__tab) <= self.x:
            return len(self.__tab)

a = A([1,2,3,4,5],5)
print(a.foo())'''

class MaClasse:
    x = 10
    y = x + 5
    print(x, y)
    def up(self):
        MaClasse.x += 10
        MaClasse.y = MaClasse.x + 5
        print(MaClasse.x, MaClasse.y)


a = MaClasse()
b = MaClasse()
b.up()
print(a.x, a.y)
