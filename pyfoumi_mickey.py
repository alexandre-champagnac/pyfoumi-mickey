from random import randint
from PIL import Image

#Chargement et préparation des images

img_pierre = Image.open("pierrem.png")
img_feuille = Image.open("feuillem.png")
img_ciseaux = Image.open("ciseauxm.png")
img_win = Image.open("winm.png")
img_lose = Image.open("losem.png")
img_assemble = Image.new("RGB",(600,200))

#Bienvenue

#Initialisation des scores
score_ordi = 0
score_joueur = 0

#Premier choix du joueur
choix_joueur = input('Entrez P pour pierre, F pour feuille, C pour ciseaux ou Q pour quitter').upper()

while (choix_joueur!= "Q"):
    #choix de l'ordinateur
    choix_ordinateur = randint(1,3) #1 = papier 2 = feuille 3 = ciseaux

    #création de l'image assemblée des choix des deux joueurs
    #choix_joueur
    for y in range(200):
        for x in range(200):
            if choix_joueur == 'P':
                pixel = img_pierre.getpixel((x,y))
                img_assemble.putpixel((x,y),(pixel))
            elif choix_joueur == 'F' :
                pixel = img_feuille.getpixel((x,y))
                img_assemble.putpixel((x,y),(pixel))
            elif choix_joueur == 'C' :
                 pixel = img_ciseaux.getpixel((x,y))
                 img_assemble.putpixel((x,y),(pixel))
            else :
                img_assemble.putpixel((x,y),(0,0,0))
    #choix ordi
    for y in range(200):
        for x in range(200):
            if choix_ordinateur == 1:                   #1 = papier 2 = feuille 3 = ciseaux
                pixel = img_pierre.getpixel((x,y))
                img_assemble.putpixel((x + 200,y),(pixel))
            elif choix_ordinateur == 2 :
                pixel = img_feuille.getpixel((x,y))
                img_assemble.putpixel((x + 200,y),(pixel))
            elif choix_ordinateur == 3 :
                 pixel = img_ciseaux.getpixel((x,y))
                 img_assemble.putpixel((x + 200,y),(pixel))

    #Gagnant/Perdant/score

    print((choix_ordinateur))
    if choix_joueur == 'P' and choix_ordinateur == 1 :
        result = "égalité"
    elif choix_joueur == 'F' and choix_ordinateur == 1 :
        result = "gagné"
    elif choix_joueur == 'C' and choix_ordinateur == 1 :
        result = "perdu"
    elif choix_joueur == 'P' and choix_ordinateur == 2 :
        result = "perdu"
    elif choix_joueur == 'F' and choix_ordinateur == 2 :
        result = "égalité"
    elif choix_joueur == 'C' and choix_ordinateur == 2 :
        result = "gagné"
    elif choix_joueur == 'P' and choix_ordinateur == 3 :
        result = "gagné"
    elif choix_joueur == 'F' and choix_ordinateur == 3 :
        result = "perdu"
    elif choix_joueur == 'C' and choix_ordinateur == 3 :
        result = "égalité"
    else :
        result = "mauvaise saisie"

    for y in range(200):
        for x in range(200):
            if result == "gagné":
                pixel = img_win.getpixel((x,y))
                img_assemble.putpixel((x + 400,y),(pixel))
            elif result == "perdu" :
                pixel = img_lose.getpixel((x,y))
                img_assemble.putpixel((x + 400,y),(pixel))
            else :
                img_assemble.putpixel((x + 400,y),(0,0,0))

    if result == "gagné" :
        score_joueur = score_joueur + 1
    elif result == "perdu" :
        score_ordi = score_ordi + 1

    img_assemble.show()


     #saisie du choix du joueur
    choix_joueur = input('Entrez P pour pierre, F pour feuille, C pour ciseaux ou Q pour quitter').upper()

#Sortie du jeu
print('C\'est terminé')
print("Votre score est de " + str(score_joueur) + " contre " + str(score_ordi) + " pour l'ordinateur")



