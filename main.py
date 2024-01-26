from src.test_affichage_map import affichage_map
from src.clavier_jeu import *
from src.person import Player
from src.import_map_csv import lire_map_depuis_doc
from src.verifie_mouvement import verifie_mouvement
#######################################################################
#PENSER A IMPORTER COLORAMA POUR METTRES CERTAIN CARACTERE EN COULEUR
#######################################################################

joueur=Player(3, 12, 3, 0)

map=lire_map_depuis_doc()


while True:
    if keyboard.is_pressed("LEFT"):
        handle_key_press("LEFT", "L")
        map, traversable=verifie_mouvement(map, joueur, 0)
        if(traversable==1):
            joueur.move(-1, 0)
        os.system('cls')
        affichage_map(map, joueur)
        while keyboard.is_pressed("LEFT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("RIGHT"):
        handle_key_press("RIGHT", "R")
        map, traversable=verifie_mouvement(map, joueur, 1)
        if(traversable==1):
            joueur.move(+1, 0)
        os.system('cls')
        affichage_map(map, joueur)
        while keyboard.is_pressed("RIGHT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("UP"):
        handle_key_press("UP", "U")
        map, traversable=verifie_mouvement(map, joueur, 2)
        if(traversable==1):
            joueur.move(0, -1)
        os.system('cls')
        affichage_map(map, joueur)
        while keyboard.is_pressed("UP"):
            time.sleep(0.01)

    elif keyboard.is_pressed("DOWN"):
        handle_key_press("DOWN", "D")
        map, traversable=verifie_mouvement(map, joueur, 3)
        if(traversable==1):
            joueur.move(0, +1)
        os.system('cls')
        affichage_map(map, joueur)
        while keyboard.is_pressed("DOWN"):
            time.sleep(0.01)

    elif keyboard.is_pressed("A"):
        handle_key_press("A", "Function A")
        #current_position = 0  # Reset the position
        while keyboard.is_pressed("A"):
            time.sleep(0.1)

    # Add a delay to avoid constant checking (adjust as needed)
    time.sleep(0.1)