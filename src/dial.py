import xml.etree.ElementTree as ET
import random
import time

class Dialogue:
    
    def __init__(self, nom_fichier, joueur, direction):
        self.joueur=joueur
        self.direction=direction
        self.dialogue = self.charger_dialogue_depuis_xml(nom_fichier)
        
        

    def charger_dialogue_depuis_xml(self, nom_fichier):
        tree = ET.parse(nom_fichier)
        dialogue=""
        
        x_position_joueur=self.joueur.x
        y_position_joueur=self.joueur.y

        if(self.direction==0):
            x_position_joueur=x_position_joueur-1
        if(self.direction==1):
            x_position_joueur=x_position_joueur+1
        if(self.direction==3):
            y_position_joueur=y_position_joueur-1
        if(self.direction==2):
            y_position_joueur=y_position_joueur+1


        if (x_position_joueur==8 and y_position_joueur==10):
            dialogue = tree.getroot()[0]  
        elif (x_position_joueur==24 and y_position_joueur==15):
            dialogue = tree.getroot()[1] 
        elif (x_position_joueur==44 and y_position_joueur==8):
            dialogue = tree.getroot()[2]  
        elif (x_position_joueur==49 and y_position_joueur==15):
            dialogue = tree.getroot()[3]  
        elif (x_position_joueur==49 and y_position_joueur==18):
            dialogue = tree.getroot()[4]
        elif (x_position_joueur==80 and y_position_joueur==9):
            dialogue = tree.getroot()[5]
        elif (x_position_joueur==80 and y_position_joueur==12):
            dialogue = tree.getroot()[6]
        elif (x_position_joueur==88 and y_position_joueur==11):
            dialogue = tree.getroot()[7]
        elif (x_position_joueur==87 and y_position_joueur==19):
            dialogue = tree.getroot()[8] 
        elif (x_position_joueur==8 and y_position_joueur==20):
            dialogue = tree.getroot()[9]
        elif (x_position_joueur==8 and y_position_joueur==19):
            dialogue = tree.getroot()[10]
        elif (x_position_joueur==26 and y_position_joueur==20):
            dialogue = tree.getroot()[11]  
        elif (x_position_joueur==28 and y_position_joueur==15):
            dialogue = tree.getroot()[12]  
        elif (x_position_joueur==21 and y_position_joueur==9):
            dialogue = tree.getroot()[13]  
        elif (x_position_joueur==23 and y_position_joueur==5):
            dialogue = tree.getroot()[14]  
        elif (x_position_joueur==41 and y_position_joueur==7):
            dialogue = tree.getroot()[15]  
        elif (x_position_joueur==41 and y_position_joueur==14):
            dialogue = tree.getroot()[16]  
        elif (x_position_joueur==56 and y_position_joueur==6):
            dialogue = tree.getroot()[17]  
        
          
        return dialogue


            
    def afficher_dialogue(self):
        texte_dialogue = self.dialogue.find('text').text
        print(texte_dialogue)


    def jouer(self):
        self.afficher_dialogue()
        time.sleep(5)
        
        


