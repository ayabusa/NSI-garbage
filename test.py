def ma_fonction(entre: str):
    chaine = entre.split()
    dico = {}
    for i in chaine:
        if i in dico:
            dico[i] += 1
        else:
            dico[i] = 1
    return dico

def liste_mots(entre: str):
    dico = ma_fonction(entre)
    ma_liste = []
    for cle in dico:
        ma_liste.append(cle)
    return ma_liste

print(liste_mots("et de un et de deux et de trois"))