
class Note:
    def __init__(self, valeur, coef):
        self.valeur = valeur
        self.coef = coef

    def affiche(self):
        return {"note": self.valeur,
         "coef": self.coef}

