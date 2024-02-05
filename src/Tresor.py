from src.Caractere import Caractere


class Tresor(Caractere):
    #voir classe parenjte Caractere()
    def __init__(self):
        super().__init__(chr(36))  # symbole "$"

    def traversable(self, joueur):
        return 1
    
    def trouveTresors(self, joueur):
        return 1