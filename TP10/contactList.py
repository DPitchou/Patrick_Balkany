class Adresse:
    def __init__(self, rue, ville):
        self.rue = rue
        self.ville = ville

    def __str__(self):
        return f'La rue est:{self.rue} dans la ville: {self.ville}'

class Personne:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"Le nom est:{self.nom} et l'adresse email est:{self.email}"

class Contact(Adresse, Personne):
    def __init__(self, rue, ville, nom, email):
        Adresse.__init__(self, rue, ville)
        Personne.__init__(self, nom, email)

    def __str__(self):
        return f'Rue: {self.rue}\nVille: {self.ville}\nNom: {self.nom}\nEmail: {self.email}'

class Carnet:
    def __init__(self, personne=[]):
        self.personne = personne

    def addContact(self, rue, ville, nom, email):
        self.personne.append(Contact(rue, ville, nom, email))

    def findContact(self, nom):
        for i in self.personne:
            if i.nom == nom:
                print(i)

C=Carnet()
C.addContact('Chaussure', 'pontault', 'louan', 'email')
C.findContact('louan')
