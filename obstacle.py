import pygame
import random
from settings import *

# load image
obstacle_image = []
obstacle_image.append(pygame.transform.scale(pygame.image.load("image/obstacles/ceiling_light.png"), (166, 52)))
obstacle_image.append(pygame.transform.scale(pygame.image.load("image/obstacles/chair.png"), (85, 130)))
obstacle_image.append(pygame.transform.scale(pygame.image.load("image/obstacles/fan.png"), (180, 130)))
obstacle_image.append(pygame.transform.scale(pygame.image.load("image/obstacles/projector.png"), (91, 52)))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(obstacle_image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-200, -50)
        self.upper = 2
        self.lower = 1
        self.speedy = random.randrange(self.lower, self.lower + 1)
        self.speedx = random.randrange(-1, 1)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(self.lower, self.lower + 1)
            self.speedx = random.randrange(-1, 1)
        elif self.rect.right > WIDTH or self.rect.left < 0:
            self.speedx *= -1
        pass

    def level_update(self):
        self.speedy = random.randrange(self.lower, self.lower + 1)