from src.test_affichage_map import affichage_map
from src.clavier_jeu import *
from src.person import Player
from src.import_map_csv import lire_map_depuis_doc
from src.verifie_mouvement import verifie_mouvement

#On vient initialiser une instance de la classe joueur. Cela nous permetera de sauvegarder sa possition, ses points de vie et sa richesse
joueur=Player(3, 12, 3, 0)

#On extrait la map du fichier csv où elle est sauvegarder. Le fait de la garder dans un fichier csv rend la modification plus facile et plus rapide
map=lire_map_depuis_doc()
fin_du_jeu=0
#on initialise la boucle de jeu qui ne sera pas arreter tant que le personnage n'est pas mort ou n'a pas atteint la sortie
while fin_du_jeu==0:
    
    texte=""

#on attend en boucle que le joueur touche une fléche directionel
#lorsqu'une flèche directionel est touchée, on vient utiliser la fonction verifie mouvement, qui vient vérifier si le joueur peux bouger ou non,
#bouge le joueur le cas échéant, et aplique tout les effets de la case sur laquel le joueur atterie ou interagie.
#C'est cette fonction de vérifie_mouvement qui fait tour le travaille de communication entre les classes et d'apelle de fonctions.
#Une fois que cela est fait, on update si besoin la position du joueur, et on appelle affichage_map qui vas se charger de toute la partie
#affichage en ascii
    if keyboard.is_pressed("LEFT"):
        handle_key_press("LEFT", "")
        map, traversable, texte, fin_du_jeu=verifie_mouvement(map, joueur, 0)
        if(traversable==1):
            joueur.move(-1, 0)
        os.system('cls' if os.name == 'nt' else 'clear')
        affichage_map(map, joueur)
        print(texte)
        while keyboard.is_pressed("LEFT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("RIGHT"):
        handle_key_press("RIGHT", "")
        map, traversable, texte, fin_du_jeu=verifie_mouvement(map, joueur, 1)
        if(traversable==1):
            joueur.move(+1, 0)
        os.system('cls' if os.name == 'nt' else 'clear')
        affichage_map(map, joueur)
        print(texte)
        while keyboard.is_pressed("RIGHT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("UP"):
        handle_key_press("UP", "")
        map, traversable, texte, fin_du_jeu=verifie_mouvement(map, joueur, 3)
        if(traversable==1):
            joueur.move(0, -1)
        os.system('cls' if os.name == 'nt' else 'clear')
        affichage_map(map, joueur)
        print(texte)
        while keyboard.is_pressed("UP"):
            time.sleep(0.01)

    elif keyboard.is_pressed("DOWN"):
        handle_key_press("DOWN", "")
        map, traversable, texte, fin_du_jeu=verifie_mouvement(map, joueur, 2)
        if(traversable==1):
            joueur.move(0, +1)
        os.system('cls' if os.name == 'nt' else 'clear')
        affichage_map(map, joueur)
        print(texte)
        while keyboard.is_pressed("DOWN"):
            time.sleep(0.01)

    #La fin du jeu peux être atteinte soit si le joueur atteint 0 points de vie soit si il atteint la sortie
    if (joueur.get_health()<=0):
        fin_du_jeu=1

    time.sleep(0.1)

if (joueur.get_health()<=0):
    print("##########\nFin du jeux. Vous êtes malheureusement mort dans un piege.\n##########")
else:
    print("##########\nFin du jeux. Bien joué, vous avez atteint la fin du niveau !\n##########")