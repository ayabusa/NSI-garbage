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
""")
a = input("Voullez vous une vitesse instantanée ? (Y/N) \n(N par défaut) : ")
b = input("Combien de battiment voullez vous ? \n(5 par défaut) : ")

if (a.capitalize() != "Y" and  a.capitalize() != "N" and  a != ""):
    print("Merci d'entrer une valeur valide >_<")
elif a == "Y":
    instant_speed = True
if b != "":
    try:
        nb_batiment = int(b)
    except:
        print("Merci d'entrer une valeur valide >_<")

# invite l'utilisateur à personnaliser la fenêtre


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

def toit():
    t.begin_fill()
    ''' Fonction qui trace le toit '''
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
    ''' Fonction qui trace le toit rond '''
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
    t.begin_fill()
    ''' Fonction qui trace le rez de chaussez '''
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

def bas_fene():
    ''' Fonction qui trace le rez de chaussez '''
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

def étage():
    ''' Fonction qui trace l'étage '''
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

def étage_deux_fene():
    ''' Fonction qui trace l'étage '''
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
    ''' Change la couleur du pinceau aléatoirement'''
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.fillcolor(r,g,b)

def faire_batiment():
    t.pendown()
    # déssine le bas
    couleur_random()
    match random.randint(0,1):
        case 0:
            bas()
        case 1:
            bas_fene()
    # déssine les étages intermédiaires
    for i in range(random.randint(0,5)):
        couleur_random()
        match random.randint(0,1):
            case 0:
                étage()
            case 1:
                étage_deux_fene()
    # déssine le toit
    couleur_random()
    match random.randint(0,1):
        case 0:
            toit()
        case 1:
            toit_rond()

    # reviens en bas
    t.setposition(t.position()[0], -370)
    t.forward(150)

def batiments():
    ''' Fonction qui trace un batiment '''
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

print(t.position())

batiments()
#pour la vitesse instant
if instant_speed == True:
    t.update()
# garde la fenêtre allumé
t.mainloop()