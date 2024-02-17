import math

####### TRUC BINAIRE/HEXA ########

def binaire(a):
    b=0
    d=a
    c=0
    e=[]
    f=""
    while d!=0 :
        c=d%2
        d=d//2
        e.append(c)
    for i in e :
        f=str(i)+f
    return [f,e]

def hexadécimal(a):
    b=0
    d=a
    c=0
    e=[]
    f=""
    while d!=0 :
        c=d%16
        d=d//16
        if c < 10 :
            e.append(c)
        elif c==10 :
            e.append("A")
        elif c==11 :
            e.append("B")
        elif c==12 :
            e.append("C")
        elif c==13 :
            e.append("D")
        elif c==14 :
            e.append("E")
        elif c==15 :
            e.append("F")
    for i in e :
        f=str(i)+f
    return [f,e]

def conversion_binaire(a):
    c=[]
    for b in a :
        c.append(binaire(b)[0])
    return(c)

def conversion_hexadécimal(a):
    c=[]
    for b in a :
        c.append(hexadécimal(b)[0])
    return(c)

####### NB PREMIER ########

def trouverpremier(taille): # prend en arg le seuil et retourne un tableau des nb premiers
    # cree le tableaux !
    tab=[p for p in range(2,taille+1)]
    # boucle pincipale
    for i in range(len(tab)):
        # nb est le nombre par lequel on va essayer de diviser tout les autres
        nb = tab[i]
        for t in range(len(tab)):
            # nb2 le nombre à diviser
            nb2 = tab[t]
            # test si nb2 est plus petit ou egal a nb
            # test si le reste de la division nb2/nb est bien 0
            # test si nb -1 (valeur quand le nombre n'est pas premier)
            if (not nb2 <= nb) and (nb2%nb == 0) and (nb != -1):
                # indique en le remplacant que le nombre n'est pas premier
                tab[t] = -1
    # enleve toutes les occurences de -1
    while tab.count(-1):
        tab.remove(-1)
    return tab

def testPremier(nb): # prend en arg le nombre et retourne un bool qui dit si il est premier ou pas
    print("nombre choisit :",nb)
    tab = trouverpremier(nb)
    if tab[len(tab)-1] == nb:
        return True
    else:
        return False

def décomposition_en_nombre_premier(obj):
    a=1
    b=obj
    c=[]
    for i in trouverpremier(obj):
        while b%i==0:
                b=b/i
                c.append(i)
    return(c)

####### NB DYADIQUES #######

def testDyadique(nb):
    # On trouve la fraction initiale (diviseur = dénominateur)
    numerateur = int(str(nb).replace(".", "")) # on enlève juste la virgule, ex: 6.42 -> 642
    diviseur = 10**len(recupNbDecimaux(nb)) # le diviseur est une puissance de 10 du nombre de chiffre après la virgule, ex: 6.42 -> 10² -> 100
    # On simplifie la fraction en décomposant les nb en nombres premier.
    numerateur = décomposition_en_nombre_premier(numerateur)
    diviseur = décomposition_en_nombre_premier(diviseur)
    # On trouve les premiers communs
    premierCommun = {}
    for i in range(len(numerateur)):
        nombre = numerateur[i]
        if (diviseur.count(nombre) != 0):
            if numerateur.count(nombre) >= diviseur.count(nombre):
                premierCommun[nombre] = diviseur.count(nombre)
            else:
                premierCommun[nombre] = numerateur.count(nombre)
    # On enlève les premiers communs
    for i in premierCommun:
        nbDeFois = premierCommun[i]
        for t in range(nbDeFois):
            diviseur.remove(i)
            numerateur.remove(i)
    # On calcule le diviseur final
    diviseurFinal = 1
    for i in diviseur:
        diviseurFinal = diviseurFinal*i
    # Test final
    while diviseurFinal % 2 == 0:
        diviseurFinal = diviseurFinal//2
    return diviseurFinal == 1

def recupNbDecimaux(nb):
    chaine = list(str(nb))
    for i in range(len(chaine)):
        if chaine[i] != ".":
            chaine[i] = False
        else:
            chaine[i] = False
            while chaine.count(False):
                chaine.remove(False)
            return chaine

####### INTERFACE DE LA HESS ########

print("    ____                      _                       __            \n   / __ \________  ____ ___  (_)__  _________  ____ _/ /_____  _____\n  / /_/ / ___/ _ \/ __ `__ \/ / _ \/ ___/ __ \/ __ `/ __/ __ \/ ___/\n / ____/ /  /  __/ / / / / / /  __/ /  / / / / /_/ / /_/ /_/ / /    \n/_/   /_/   \___/_/ /_/ /_/_/\___/_/  /_/ /_/\__,_/\__/\____/_/     ")
print("Par Léon R. et Alexandre L.")
reponse = input("Quel mode voullez vous ? \n [1] Obtenir une liste de nombres premier \n [2] Obtenir une liste de nombres premier en Binaire \n [3] Obtenir une liste de nombres premier en Hexadeciamal \n [4] Tester si un nombre est premier \n [5] Décomposition en nombre premier \n [6] Tester si un nombre est dyadique \nVotre choix :")

if reponse == "1":
    nb = int(input("Choisissez le seuil :"))
    resultat = trouverpremier(nb)
    print("Voici la liste des nombres premier jusqu'à", nb)
    print(resultat)

elif reponse == "2":
    nb = int(input("Choisissez le seuil :"))
    resultat = conversion_binaire(trouverpremier(nb))
    print("Voici la liste des nombres premier en Binaire jusqu'à", nb)
    print(resultat)

elif reponse == "3":
    nb = int(input("Choisissez le seuil :"))
    resultat = conversion_hexadécimal(trouverpremier(nb))
    print("Voici la liste des nombres premier en Hexadécimal jusqu'à", nb)
    print(resultat)

elif reponse == "4":
    nb = int(input("Choisissez le nombre à tester :"))
    resultat = testPremier(nb)
    if resultat == True:
        print("Le nombre", nb, "est premier")
    else:
        print("Le nombre", nb, "n'est pas premier")

elif reponse == "5":
    nb = int(input("Quel nombre voullez vous décomposer :"))
    resultat = décomposition_en_nombre_premier(nb)
    print("Voici le nombre", nb, "décomposé en nombres premier :", resultat)

elif reponse == "6":
    nb = float(input("Choisissez le nombre à tester (flottant) :"))
    resultat = testDyadique(nb)
    if resultat == True:
        print("Le nombre", nb, "est dyadique")
    else:
        print("Le nombre", nb, "n'est pas dyadique")

else:
    print("Merci de renter un mode valide (ex: 1, 2, etc...)")