from src.test_affichage_map import affichage_map
from src.clavier_jeu import *
from src.person import Player
from src.import_map_csv import lire_map_depuis_doc
from src.verifie_mouvement import verifie_mouvement
#######################################################################
#PENSER A IMPORTER COLORAMA POUR METTRES CERTAIN CARACTERE EN COULEUR
#######################################################################

joueur=Player(106, 11, 3, 0)

map=lire_map_depuis_doc()

fin_du_jeu=0

while fin_du_jeu==0:
    
    texte=""

    if keyboard.is_pressed("LEFT"):
        handle_key_press("LEFT", "L")
        map, traversable, texte, fin_du_jeu=verifie_mouvement(map, joueur, 0)
        if(traversable==1):
            joueur.move(-1, 0)
        os.system('cls')
        affichage_map(map, joueur)
        print(texte)
        while keyboard.is_pressed("LEFT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("RIGHT"):
        handle_key_press("RIGHT", "R")
        map, traversable, texte, fin_du_jeu=verifie_mouvement(map, joueur, 1)
        if(traversable==1):
            joueur.move(+1, 0)
        os.system('cls')
        affichage_map(map, joueur)
        print(texte)
        while keyboard.is_pressed("RIGHT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("UP"):
        handle_key_press("UP", "U")
        map, traversable, texte, fin_du_jeu=verifie_mouvement(map, joueur, 3)
        if(traversable==1):
            joueur.move(0, -1)
        os.system('cls')
        affichage_map(map, joueur)
        print(texte)
        while keyboard.is_pressed("UP"):
            time.sleep(0.01)

    elif keyboard.is_pressed("DOWN"):
        handle_key_press("DOWN", "D")
        map, traversable, texte, fin_du_jeu=verifie_mouvement(map, joueur, 2)
        if(traversable==1):
            joueur.move(0, +1)
        os.system('cls')
        affichage_map(map, joueur)
        print(texte)
        while keyboard.is_pressed("DOWN"):
            time.sleep(0.01)

    if (joueur.get_health()<=0):
        fin_du_jeu=1

    time.sleep(0.1)

if (joueur.get_health()<=0):
    print("Fin du jeux. Vous êtes malheureusement mort dans un piege.")
else:
    print("Fin du jeux. Bien joué, vous avez atteint la fin du niveau !")