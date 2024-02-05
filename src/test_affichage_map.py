import pandas as pd 
import numpy as np
import scipy as sp
from src.person import Player
import os
from colorama import Fore, Back, Style

def affichage_map(map, joueur):
        """
        input : map, une liste de liste
                joueur : une instance de la classe Player()
        output: rien, cette fonction ne fait que print
        Cette fonction fait le lien entre les information du csv et l'affichage en ascii. En effet, la map est sauvegarder dans le document csv
        Comme une suite de chiffre de 0 à 16. Cela representes les 17 case possibles pouvant être afficher pour faire la map.
        Il faut ensuite transformer ces chiffres en caractere ascci. C'est ce que fait cette fonction. Elle vérifie une à une toutes les cases
        et y associe le bon caractere ascii.
        Cette fonction sert aussi à mettre en forme les caractere grace à colorama avant de les afficher
        """

        map_a_print=""
        x_position_joueur=joueur.x
        y_position_joueur=joueur.y


        for i in range(len(map)):
                for j in range(len(map[i])): 
                        #On verifie si le joueur est présent sur la case. Si oui, on affiche le joueur, sinon on affiche la case normalement
                        if(j==x_position_joueur and i==y_position_joueur):
                                map_a_print+=Back.RED
                                map_a_print+=("#")
                                map_a_print+=Style.RESET_ALL
                        else :
                                tuille = map[i][j]
                                if(tuille=="0"):  
                                        map_a_print+=Fore.WHITE  
                                        map_a_print+=(".")
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="1"):    
                                        map_a_print+=Fore.RED 
                                        map_a_print+=Back.GREEN 
                                        map_a_print+=("@")
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="2"):  
                                        map_a_print+=Fore.BLUE  
                                        map_a_print+=("§")
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="3"):    
                                        map_a_print+=("/")
                                elif(tuille=="4"):    
                                        map_a_print+=("b")
                                elif(tuille=="5"):    
                                        map_a_print+=("→")
                                elif(tuille=="6"):    
                                        map_a_print+=("↓")
                                elif(tuille=="7"):    
                                        map_a_print+=("↑")
                                elif(tuille=="8"):
                                        map_a_print+=Fore.YELLOW    
                                        map_a_print+=("$")
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="9"):    
                                        map_a_print+=("M")
                                elif(tuille=="10"):    
                                        map_a_print+=("¶")
                                elif(tuille=="11"):    
                                        map_a_print+=("!")
                                elif(tuille=="12"):    
                                        map_a_print+=("?")
                                elif(tuille=="13"):    
                                        map_a_print+=("♫")
                                elif(tuille=="14"):
                                        map_a_print+=Fore.RED    
                                        map_a_print+=("o")
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="15"): 
                                        map_a_print+=Fore.WHITE 
                                        map_a_print+=Back.BLACK  
                                        map_a_print+=("‼")
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="16"):    
                                        map_a_print+=("↨")
                                else:
                                        map_a_print+="-"
                #On affiche aussi les informations du joueur à coté de la map
                if(i== 1):
                        map_a_print+="      position x :"+str(joueur.x)
                elif(i== 3):
                        map_a_print+="      position y :"+str(joueur.y)
                elif(i== 5):
                        map_a_print+="      santé du personange :"+str(joueur.health)
                elif(i== 7):
                        map_a_print+="      richesse du personnage :"+str(joueur.resources)
                        
                map_a_print+=Style.RESET_ALL
                map_a_print+="\n"

        os.system('cls' if os.name == 'nt' else 'clear')
        print(chr(27) + "[2J")
        print(map_a_print)