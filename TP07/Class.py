import sys
class membre_ipsa:
    def __init__(self, nom, prenom, email, ID):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.ID = ID

    def __str__(self):
        print("nom:",self.nom, "prenom:", self.prenom, "email:", self.email, "ID:", self.ID)

class Etudiant(membre_ipsa):
    def __init__(self, nom, prenom, age, email, ID):
        super().__init__(nom, prenom, email, ID)
        self.age = age

    def majeur(self):
        if self.age < 18:
            print("Mineur")
        else:
            print("Majeur")

