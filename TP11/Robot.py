class Robot:
    def __init__(self, nom, x=0, y=0, direction='Est'):
        self.nom = nom
        self.x = x
        self.y = y
        self.direction = direction

    def avance(self):
        if self.direction == 'Nord':
            self.y +=1

        elif self.direction == 'Sud':
            self.y -=1

        elif self.direction == 'Est':
            self.x += 1

        elif self.direction == 'Ouest':
            self.x -= 1

    def droite(self):
        if self.direction == 'Nord':
            self.direction = 'Est'

        elif self.direction == 'Est':
            self.direction = 'Sud'

        elif self.direction == 'Sud':
            self.direction = 'Ouest'

        elif self.direction == 'Ouest':
            self.direction = 'Nord'

    def affiche(self):
        print(f'nom:{self.nom}\nx:{self.x}\ny:{self.y}\ndirction:{self.direction}')


class RobotNG(Robot):
    def __init__(self, nom, x=0, y=0, direction='Est', turbo=1):
        super().__init__(nom, x, y, direction)
        self.turbo = turbo


    def avance(self, pas):
        if self.direction == 'Nord':
            self.y += pas*self.turbo

        elif self.direction == 'Sud':
            self.y -= pas*self.turbo

        elif self.direction == 'Est':
            self.x += pas*self.turbo

        elif self.direction == 'Ouest':
            self.x -= pas*self.turbo

    def gauche(self):
        if self.direction == 'Nord':
            self.direction = 'Ouest'

        elif self.direction == 'Ouest':
            self.direction = 'Sud'

        elif self.direction == 'Sud':
            self.direction = 'Est'

        elif self.direction == 'Est':
            self.direction = 'Nord'

    def demiTour(self):
        if self.direction == 'Nord':
            self.direction = 'Sud'

        elif self.direction == 'Sud':
            self.direcrtion = 'Nord'

        elif self.direction == 'Est':
            self.direction = 'Ouest'

        elif self.direction == 'Ouest':
            self.direction = 'Est'

    def Turbo(self):
        if self.turbo == 1:
            self.turbo = 3

        elif self.turbo == 3:
            self.turbo = 1

    def affiche(self):
        z = False
        if self.turbo == 1:
            z = False
        else:
            z = True
        print(f'nom:{self.nom}\nx:{self.x}\ny:{self.y}\ndirction:{self.direction}\nTurbo:{z}')


A = Robot('Charle')
A.affiche()
A.avance()
A.affiche()
A.droite()
A.affiche()

B = RobotNG('NG')
B.affiche()
B.avance(3)
B.affiche()
B.gauche()
B.affiche()
B.Turbo()
B.avance(3)
B.affiche()



