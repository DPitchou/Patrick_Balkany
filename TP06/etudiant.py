from note import *
class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        self.note = []

    def ajoute_note(self, note):
        self.note.append(Note(note[0], note[1]))

    def moyenne(self):
        l = []
        c = []
        for i in self.note:
            l.append(i.affiche()["note"] * i.affiche()["coef"])
            c.append(i.affiche()["coef"])
        return sum(l)/sum(c)


    def affiche(self):
        z = str(self.nom)+" # "+str(self.moyenne())+" # "
        for i in self.note:
            z = z+str(i.affiche()["note"])+"("+str(i.affiche()["coef"])+") "

        print(z)




