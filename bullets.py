import pygame
from settings import *

bul_image = pygame.transform.scale(pygame.image.load("image/supplies/bullet.png"), (17, 70))

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bul_image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()    # sprite裡的函式，在所有的sprite群組中刪掉

