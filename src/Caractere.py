class Caractere:
    def __init__(self, symbole):
        self.symbole = symbole

    def traversable(self, joueur):
        pass  # Méthode à implémenter dans les sous-classes
    #savoir si une case peux être traverser
    
    def trouveTresors(self, joueur):
        return 0
    #Savoir si la case déclenche la fonction augmentant la richesse du joueur
    
    def boiteDialogue(self, joueur):
        return 0
    #Savoir si la case déclenche la fonction de dialogue
    
    def enigme(self):
        return 0
    #Savoir si la case déclenche la fonction de quizz
    
    def piege(self, joueur):
        return 0
    #Savoir si la case déclenche la fonction diminuant la santé du joueur
    
    def ending(self, joueur):
        return 0
    #Savoir si la case déclenche la fin du jeu
    
    def gagneVie(self, joueur):
        return 0
    #Savoir si la case déclenche la fonction augmentant la santé du joueur