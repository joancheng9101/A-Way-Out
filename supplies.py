import pygame
import random
from settings import *

# load image
supply_image = {'choclate': pygame.transform.scale(pygame.image.load("image/supplies/chocolate.png"), (65, 78)), \
                'aid': pygame.transform.scale(pygame.image.load("image/supplies/first_aid_kit.png"), (78, 78)), \
                'phone': pygame.transform.scale(pygame.image.load("image/supplies/phone.png"), (78, 78)), \
                'radio': pygame.transform.scale(pygame.image.load("image/supplies/radio.png"), (85, 65)), \
                'water': pygame.transform.scale(pygame.image.load("image/supplies/water.png"), (78, 78)), \
                'helmet': pygame.transform.scale(pygame.image.load('image/supplies/helmet.png'), (78, 59))}

class Supplies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_list = ['choclate', 'aid', 'phone', 'radio', 'water', 'helmet']
        self.name = random.choice(self.image_list)

        self.image = supply_image[self.name]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -70)
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

