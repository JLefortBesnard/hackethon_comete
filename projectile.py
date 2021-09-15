import pygame

screen_x = 1500
screen_y = 900

# création de la classe projectile
class Projectile(pygame.sprite.Sprite):
    # definir le constructeur de la classe
    def __init__(self, player, direction, image_path):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.center[0]
        self.rect.y = player.rect.center[1]
        self.origin_image = self.image
        self.angle = 0
        self.direction = direction

    def rotate(self):
        # tourner le projectile
        self.angle += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        # self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def check_if_outside_screen(self):
        coord_x = self.rect.center[0]
        coord_y = self.rect.center[1]
        if coord_x < 0:
            return True
        elif coord_x > screen_x:
            return True
        elif coord_y < 0:
            return True
        elif coord_y > screen_y:
            return True
        return False

    def move(self):
        boom = []  # make explosion image disappear
        if self.direction == 'right':
            self.rect.x += self.velocity
        elif self.direction == 'left':
            self.rect.x -= self.velocity
        elif self.direction == 'up':
            self.rect.y -= self.velocity
        elif self.direction == 'down':
            self.rect.y += self.velocity
        elif self.direction == 'upleft':
            self.rect.y -= self.velocity
            self.rect.x -= self.velocity
        elif self.direction == 'downleft':
            self.rect.y += self.velocity
            self.rect.x -= self.velocity
        elif self.direction == 'upright':
            self.rect.y -= self.velocity
            self.rect.x += self.velocity
        elif self.direction == 'downright':
            self.rect.y += self.velocity
            self.rect.x += self.velocity
        self.rotate()
        # si collision avec un monstre
        for player in self.player.game.check_collision_group(self, self.player.game.all_players):
            if player.surname != self.player.surname:
                boom.append([player.rect.x, player.rect.y])
                player.remove()
                self.remove()
        # si collision avec un autre projectile
        for player in self.player.game.all_players:
            if player.surname != self.player.surname:
                for projectile in self.player.game.check_collision_group(self, player.all_projectiles):
                    boom.append([projectile.rect.x, projectile.rect.y])
                    projectile.remove()
                    self.remove()
        if self.check_if_outside_screen():
            boom.append([self.rect.x, self.rect.y])
            self.remove()
        return boom

