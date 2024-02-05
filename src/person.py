class Player:
#Cette classe sauvegarde les informations du personnage du joueur : la position, la vie, la richesse. Elle contient certaines méthodes pour les modifier
    def __init__(self, x, y, health, resources):
        self.x = x
        self.y = y
        self.health = health
        self.resources = resources

    def move(self, dx, dy):
        """Move the player by the specified delta in x and y."""
        self.x += dx
        self.y += dy

    def update_health(self, delta_health):
        """Update the player's health by the specified amount."""
        self.health += delta_health
        if self.health>3 :
            self.health=3

    def update_resources(self, delta_resources):
        """Update the player's resources by the specified amount."""
        self.resources += delta_resources

    def get_position_x(self):
        return self.x
    def get_position_y(self):
        return self.y
    def get_health(self):
        return self.health
    def get_ressource(self):
        return self.resources

    

#player = Player(x=0, y=0, health=100, resources=50)


"""
print(f"Initial Position: ({player.x}, {player.y})")
print(f"Initial Health: {player.health}")
print(f"Initial Resources: {player.resources}")

player.move(2, 3)
print(f"New Position: ({player.x}, {player.y})")

player.update_health(-20)
print(f"Updated Health: {player.health}")

player.update_resources(30)
print(f"Updated Resources: {player.resources}")
"""