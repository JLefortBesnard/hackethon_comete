import pygame
from player import Player



# classe qui represente le jeu
class Game:
    def __init__(self, pool):
        self.pool = pool
        self.all_comets = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()

        # charger joueur 1
        self.player1 = Player(self, pool[0][0], pool[0][1], pool[0][2], pool[0][3], 150, 150)
        self.all_players.add(self.player1)

        # charger joueur 2
        self.player2 = Player(self, pool[1][0], pool[1][1], pool[1][2], pool[1][3], 800, 150)
        self.all_players.add(self.player2)

        # charger joueur 3
        self.player3 = Player(self, pool[2][0], pool[2][1], pool[2][2], pool[2][3], 150, 800)
        self.all_players.add(self.player3)

        # charger joueur 4
        self.player4 = Player(self, pool[3][0], pool[3][1], pool[3][2], pool[3][3], 800, 800)
        self.all_players.add(self.player4)


    # def check_collision_sprites(self, sprite):
     #   return pygame.sprite.collide_mask(sprite1, sprite2)

    def check_collision_group(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


