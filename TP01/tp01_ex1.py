notes1 = [12, 14, 8.6, 12.3]
notes2 = [14, 12.5, 11, 14.5]

def moyenne(note):

    somme = 0

    for i in note:
        somme += i
    print(somme)
    moyenne = somme / len(note)
    print(moyenne)

    if moyenne < 10:
        print("Recalé")
    elif 14 > moyenne >= 10:
        print("Bien")
    elif moyenne >= 14:
        print("Très Bien")

moyenne(notes2)
