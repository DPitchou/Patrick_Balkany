class A:
    def __init__(self, a1=0.0, a2=''):
        self.a1 = a1
        self.a2 = a2

    def isEmpty(self):
        if self.a2 == '':
            return True
        else:
            return False

    def __str__(self):
        return f'a1 = {self.a1} \na2 =  {self.a2}'

#a = A()
#print(a.isEmpty())
#print(a)

class B(A):
    def __init__(self, a1=0.0, a2='', b1=0.0):
        super().__init__(a1, a2)
        if 0 <= b1 <= 180:
            self.__b1 = b1
        else:
            self.__b1 = 0.0

    def get_b1(self):
        return self.__b1

    def __str__(self):
        return f'a1 = {self.a1} \na2 =  {self.a2}\nb1 = {self.get_b1()}'

    b1 = property(get_b1)

b = B(1, 'louan', 190)
print(b)


