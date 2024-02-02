import xml.etree.ElementTree as ET
import random
import time

class Dialoque:
    
    def __init__(self, nom_fichier):
        self.dialogue = self.charger_dialogue_depuis_xml(nom_fichier)
        

    def charger_dialogue_depuis_xml(self, nom_fichier):
        tree = ET.parse(nom_fichier)
        if ssssss:
            dialogue = tree.getroot()[0]  
        elif cnnnn:
            dialogue = tree.getroot()[1] 
        elif ffffff:
            dialogue = tree.getroot()[2]  
        elif jjjj:
            dialogue = tree.getroot()[3]  
        elif nnnn:
            dialogue = tree.getroot()[4]
        elif nnn:
            dialogue = tree.getroot()[5]
        elif jjjjj:
            dialogue = tree.getroot()[6]
        elif hhhh:
            dialogue = tree.getroot()[7] 
        elif jjj:
            dialogue = tree.getroot()[8]
        elif mmmm:
            dialogue = tree.getroot()[9]
        elif jjjjj:
            dialogue = tree.getroot()[10]  
        dialogue = tree.getroot()[2]   
        return dialogue


            
    def afficher_dialogue(self):
        texte_dialogue = self.dialogue.find('text').text
        print(texte_dialogue)


    def jouer(self):
        self.afficher_dialogue()
        time.sleep(1)
        
        
if __name__ == "__main__":
    fichier_xml = "C:/Users/karim/Desktop/test/dialogue.xml"
    dial = Dialoque(fichier_xml)
    dial.jouer()


