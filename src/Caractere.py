class Caractere:
    def __init__(self, symbole):
        self.symbole = symbole

    def traversable(self, joueur):
        pass  # Méthode à implémenter dans les sous-classes
    
    def trouveTresors(self, joueur):
        return 0
    
    def boiteDialogue(self, joueur):
        return 0
    
    def enigme(self):
        return 0
    
    def piege(self, joueur):
        return 0
    
    def ending(self, joueur):
        return 0
    
    def gagneVie(self, joueur):
        return 0