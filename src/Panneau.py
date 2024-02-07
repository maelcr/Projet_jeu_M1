from src.Caractere import Caractere

class Panneau(Caractere):
    #voir classe parenjte Caractere()
    def __init__(self):
        super().__init__(chr(63))  # symbole "?"

    def traversable(self, joueur):
        return 0
    
    def boiteDialogue(self, joueur):
        return 1