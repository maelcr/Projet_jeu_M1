import xml.etree.ElementTree as ET
import random
import time

class Quiz:
    """
    Cette classe, de maniére similaire à Dialogue(), vient sortir des question d'un fichier xml. La difference est ici que les questions sont 
    aléatoire et que chaque question demande un input, et demande un input correcte pour renvoyer que la réponse est vrais. 
    """
    def __init__(self, nom_fichier):
        self.questions = self.charger_questions_depuis_xml(nom_fichier)
        self.question_choisie = None

    def charger_questions_depuis_xml(self, nom_fichier):
        tree = ET.parse(nom_fichier)
        root = tree.getroot()
        return root.findall('question')


            
    def afficher_question(self):
        texte_question = self.question_choisie.find('text').text
        print(texte_question)

        choix = self.question_choisie.find('choices')
        for choix_element in choix.findall('choice'):
            print(f"{choix_element.text}")

        print("Choisissez la lettre correspondante à votre réponse.")


    def verifier_reponse(self, choix_utilisateur):
        reponse = self.question_choisie.find('answer').text

        
        if choix_utilisateur.lower() == reponse.lower():
            return True
        else:
            return False

    def poser_question_au_hasard(self):
        self.question_choisie = random.choice(self.questions)


    def jouer(self):
        self.poser_question_au_hasard()
        self.afficher_question()

        choix_utilisateur =""
        choix_utilisateur = input("Entrez le numéro de votre choix : ")

        if self.verifier_reponse(choix_utilisateur):
            print("Correct !")
            time.sleep(1)
            return 1
        else:
            print(f"Faux. La réponse correcte est le choix {self.question_choisie.find('answer').text}.")
            time.sleep(1)
            return 0

