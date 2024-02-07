from src.Caractere import Caractere

class Personne(Caractere):
    #voir classe parenjte Caractere()
    def __init__(self):
        super().__init__(chr(33))  # symbole "!"

    def traversable(self, joueur):
        return 0
    def boiteDialogue(self, joueur):
        return 1
    