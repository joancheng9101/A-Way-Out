import pygame
import random
from settings import *

# load image
gun_image = pygame.transform.scale(pygame.image.load("image/supplies/gun.png"), (65, 65))

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = gun_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(2, 5)
        self.speedx = random.randrange(-1, 1)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 5)
            self.speedx = random.randrange(-5, 5)
        elif self.rect.right > WIDTH or self.rect.left < 0:
            self.speedx *= -1
        pass

