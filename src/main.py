from test_affichage_map import affichage_map
from clavier_jeu import *
from person import Player


joueur=Player(0, 0, 3, 0)

while True:
    if keyboard.is_pressed("LEFT"):
        handle_key_press("LEFT", "L")
        joueur.move(-1, 0)
        os.system('cls')
        affichage_map(joueur)
        while keyboard.is_pressed("LEFT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("RIGHT"):
        handle_key_press("RIGHT", "R")
        joueur.move(+1, 0)
        os.system('cls')
        affichage_map(joueur)
        while keyboard.is_pressed("RIGHT"):
            time.sleep(0.01)

    elif keyboard.is_pressed("UP"):
        handle_key_press("UP", "U")
        joueur.move(0, +1)
        os.system('cls')
        affichage_map(joueur)
        while keyboard.is_pressed("UP"):
            time.sleep(0.01)

    elif keyboard.is_pressed("DOWN"):
        handle_key_press("DOWN", "D")
        joueur.move(0, -1)
        os.system('cls')
        affichage_map(joueur)
        while keyboard.is_pressed("DOWN"):
            time.sleep(0.01)

    elif keyboard.is_pressed("A"):
        handle_key_press("A", "Function A")
        #current_position = 0  # Reset the position
        while keyboard.is_pressed("A"):
            time.sleep(0.01)

    # Add a delay to avoid constant checking (adjust as needed)
    time.sleep(0.1)