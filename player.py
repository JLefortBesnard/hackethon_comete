import pygame
import random
from projectile import Projectile

screen_x = 1500
screen_y = 900

# création de la classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game, name, picture_path, projectile_path, surname, x, y):
        super().__init__()
        self.game = game
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.projectile_path = projectile_path
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.origin_image = self.image # used to get back to original after rotation
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.surname = surname
        self.position = 'right'
        self.shoot_av = True
        self.memory = []

    def recharge_weapon(self):
        self.shoot_av = True

    def rotate(self, angle):
        # tourner le projectile
        self.image = pygame.transform.rotozoom(self.origin_image, angle, 1)


    def remove(self):
        self.game.all_players.remove(self)
        for projectile in self.all_projectiles:
            projectile.remove()

    def print_surname(self, screen):
        # define txt to put on top of player
        sticker = pygame.font.SysFont('Consolas', 32).render(self.surname, True, pygame.color.Color('White'))
        # draw the sticker
        screen.blit(sticker, (self.rect.x, self.rect.y))

    def move_right(self):
        self.image = self.origin_image
        self.rect.x += self.velocity
        self.position = 'right'

    def move_left(self):
        self.image = pygame.transform.flip(self.origin_image, True, False) # no ratation, just flip of the image
        self.rect.x -= self.velocity
        self.position = 'left'

    def move_down(self):
        self.rotate(270)
        self.rect.y += self.velocity
        self.position = 'down'

    def move_up(self):
        self.rotate(90)
        self.rect.y -= self.velocity
        self.position = 'up'

    def move_upright(self):
        self.rotate(45)
        self.rect.y -= self.velocity
        self.rect.x += self.velocity
        self.position = 'upright'

    def move_upleft(self):
        self.rotate(45)
        self.image = pygame.transform.flip(self.image, True, False)  # no ratation, just flip of the image
        self.rect.y -= self.velocity
        self.rect.x -= self.velocity
        self.position = 'upleft'


    def move_downleft(self):
        self.image = pygame.transform.flip(self.origin_image, True, False)  # no ratation, just flip of the image
        self.image = pygame.transform.rotozoom(self.image, 45, 1)
        self.rect.y += self.velocity
        self.rect.x -= self.velocity
        self.position = 'downleft'

    def move_downright(self):
        self.image = pygame.transform.flip(self.origin_image, True, False)  # no ratation, just flip of the image
        self.rotate(315)
        self.rect.y += self.velocity
        self.rect.x += self.velocity
        self.position = 'downright'

    def launch_projectile(self):
        # creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self, self.position, self.projectile_path))
        self.shoot_av = False









