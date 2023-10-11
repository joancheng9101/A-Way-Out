import pygame
from bullets import Bullets
from settings import *

# load image
player1_image = pygame.transform.scale(pygame.image.load("image/player/player1.png"), (104, 156))
player2_image = pygame.transform.scale(pygame.image.load("image/player/player2.png"), (104, 156))
gun_image = pygame.transform.scale(pygame.image.load("image/supplies/gun.png"), (65, 65))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player1_image
        self.gun_image = gun_image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 30
        self.health = 100

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.move_right()
        if key_pressed[pygame.K_a]:
            self.move_left()
        if key_pressed[pygame.K_w]:
            self.move_up()
        if key_pressed[pygame.K_s]:
            self.move_down()
        #self.rect.x += 2
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.bottom < HEIGHT - 100:
            self.rect.bottom = HEIGHT - 100
        pass

    def move_right(self):
        self.rect.x += 10

    def move_left(self):
        self.rect.x -= 10

    def move_up(self):
        self.rect.y -= 10

    def move_down(self):
        self.rect.y += 10

    def shoot(self):
        bullet = Bullets(self.rect.centerx, self.rect.top)
        return bullet

    def draw_gun(self, surf):
        surf.blit(self.gun_image, (self.rect.right - 25, self.rect.centery - 25))
        pass