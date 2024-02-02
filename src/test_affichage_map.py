import pandas as pd 
import numpy as np
import scipy as sp
from src.person import Player
import os
from colorama import Fore, Back, Style

def affichage_map(map, joueur):

        map_a_print=""
        x_position_joueur=joueur.x
        y_position_joueur=joueur.y


        for i in range(len(map)):
                for j in range(len(map[i])): 

                        if(j==x_position_joueur and i==y_position_joueur):
                                map_a_print+=(chr(35))
                        else :
                                tuille = map[i][j]
                                if(tuille=="0"):  
                                        map_a_print+=Fore.WHITE  
                                        map_a_print+=(chr(46))
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="1"):    
                                        map_a_print+=Fore.RED 
                                        map_a_print+=Back.GREEN 
                                        map_a_print+=(chr(64))
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="2"):  
                                        map_a_print+=Fore.BLUE  
                                        map_a_print+=(chr(21))
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="3"):    
                                        map_a_print+=(chr(47))
                                elif(tuille=="4"):    
                                        map_a_print+=(chr(27))
                                elif(tuille=="5"):    
                                        map_a_print+=(chr(26))
                                elif(tuille=="6"):    
                                        map_a_print+=(chr(25))
                                elif(tuille=="7"):    
                                        map_a_print+=(chr(24))
                                elif(tuille=="8"):
                                        map_a_print+=Fore.YELLOW    
                                        map_a_print+=(chr(36))
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="9"):    
                                        map_a_print+=(chr(77))
                                elif(tuille=="10"):    
                                        map_a_print+=(chr(20))
                                elif(tuille=="11"):    
                                        map_a_print+=(chr(33))
                                elif(tuille=="12"):    
                                        map_a_print+=(chr(63))
                                elif(tuille=="13"):    
                                        map_a_print+=(chr(14))
                                elif(tuille=="14"):
                                        map_a_print+=Fore.RED    
                                        map_a_print+=(chr(15))
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="15"): 
                                        map_a_print+=Fore.WHITE 
                                        map_a_print+=Back.BLACK  
                                        map_a_print+=(chr(19))
                                        map_a_print+=Style.RESET_ALL
                                elif(tuille=="16"):    
                                        map_a_print+=(chr(23))
                                else:
                                        map_a_print+="-"

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