import turtle as t
import random as random

# variables de lancement
instant_speed = False
nb_batiment = 5

# mini interface
print("""
__________         __  .__                       __                
\______   \_____ _/  |_|__| _____   ____   _____/  |_  ___________ 
 |    |  _/\__  \\\\   __\  |/     \_/ __ \ /    \   __\/  _ \_  __ \\
 |    |   \ / __ \|  | |  |  Y Y  \  ___/|   |  \  | (  <_> )  | \/
 |______  /(____  /__| |__|__|_|  /\___  >___|  /__|  \____/|__|   
        \/      \/              \/     \/     \/                   
                                        ~ par Maxime S. et Léon R.
""")
a = input("Voullez vous une vitesse instantanée ? (Y/N) \n(N par défaut) : ")
b = input("Combien de battiments voullez vous ? \n(5 par défaut) : ")
### Faut qu'on ajoute d'autres options ###

if (a.capitalize() != "Y" and  a.capitalize() != "N" and  a != ""):
    print("Merci d'entrer une valeur valide pour la vitesse >_<")
elif a == "Y":
    instant_speed = True
if b != "":
    try:
        nb_batiment = int(b)
    except:
        print("Merci d'entrer une valeur valide pour le nb de battiments >_<")

# met en plein écran
screen = t.Screen()
screen.setup(width = 1.0, height = 1.0)

# met les couleurs en mode rgb
t.colormode(255)
t.speed("fastest")
screen.bgcolor(46,35,74)

# pour la vitesse instant
if instant_speed == True:
    t.tracer(0, 0)

def toit_pointu():
    ''' Fonction qui trace un toit pointu '''
    t.begin_fill()
    # met la tortue au bon endroit (100 vers le haut)
    t.penup()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()
    # trace le triangle
    for i in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()
    t.penup()

def toit_rond():
    ''' Fonction qui trace un toit rond '''
    # met la tortue au bon endroit (100 vers le haut)
    t.penup()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()
    t.begin_fill()
    # trace le triangle
    t.forward(100)
    t.left(90)
    t.circle(50, 180)
    t.left(90)

    t.end_fill()
    t.penup()

def bas():
    ''' Fonction qui trace le rez de chaussez sans fenêtre '''
    t.begin_fill()
    # fait le carré principal
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

    couleur_random()

    t.begin_fill()
    # fait la porte
    t.forward(75)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(180)

    t.end_fill()
    t.penup()

def bas_fenetre():
    ''' Fonction qui trace le rez de chaussez avec une fenêtre '''
    t.begin_fill()
    # fait le carré principal
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

    couleur_random()

    t.begin_fill()
    # fait la porte
    t.forward(75)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(180)

    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)

    couleur_random()

    t.begin_fill()

    t.pd()
    for i in range(4):
          t.forward(20)
          t.left(90)
    
    t.end_fill()
    t.pu()
    t.left(180)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.right(90)
 
    t.penup()

def etage():
    ''' Fonction qui trace un étage avec une seule fenêtre '''
    t.begin_fill()

    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()
    for i in range(4):
            t.forward(100)
            t.left(90)

    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)

    couleur_random()
    t.begin_fill()

    t.pd()
    for i in range(4):
          t.forward(20)
          t.left(90)
    t.pu()

    t.end_fill()

    t.left(180)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.right(90)

def etage_deux_fenetre():
    ''' Fonction qui trace un étage avec 2 fenêtres '''
    t.begin_fill()

    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()
    for i in range(4):
            t.forward(100)
            t.left(90)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.pd()
    couleur_random()
    t.begin_fill()
    for i in range(4):
          t.forward(20)
          t.left(90)
    t.end_fill()
    t.penup()
    t.forward(50)
    t.pd()
    couleur_random()
    t.begin_fill()
    for i in range(4):
          t.forward(20)
          t.left(90)
    t.end_fill()
    t.pu()
    t.left(180)
    t.forward(70)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.right(90)

def couleur_random():
    ''' Change la couleur du remplissage aléatoirement'''
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.fillcolor(r,g,b)

def faire_batiment():
    ''' Dessine un batiment à la position de la tortue '''
    t.pendown()
    # déssine le bas
    couleur_random()
    match random.randint(0,1):
        case 0:
            bas()
        case 1:
            bas_fenetre()
    # déssine les étages intermédiaires
    for i in range(random.randint(0,5)):
        couleur_random()
        match random.randint(0,1):
            case 0:
                etage()
            case 1:
                etage_deux_fenetre()
    # déssine le toit
    couleur_random()
    match random.randint(0,1):
        case 0:
            toit_pointu()
        case 1:
            toit_rond()

    # reviens en bas
    t.setposition(t.position()[0], -370)
    t.forward(150)

def batiments():
    ''' Fonction qui trace une rue de batiments '''
    for i in range(nb_batiment):
        faire_batiment()

# va au début
t.penup()
t.right(180)
t.forward(670)
t.left(90)
t.forward(370)
t.left(90)
t.pendown()

# lance la construction de la rue
batiments()

#pour la vitesse instantanée
if instant_speed == True:
    t.update()

# garde la fenêtre allumé
t.mainloop()