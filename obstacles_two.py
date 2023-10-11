import pygame
import os
import random
from character import Character
from settings import*

BILLBOARD = [pygame.transform.scale(pygame.image.load("image/Billboard/Billboard1.png"), (130, 91)),
             pygame.transform.scale(pygame.image.load("image/Billboard/Billboard2.png"), (130, 130)),
             pygame.transform.scale(pygame.image.load("image/Billboard/Billboard3.png"), (130, 91))]
BRICKS = [pygame.transform.scale(pygame.image.load("image/Bricks/Bricks1.png"), (156, 156)),
          pygame.transform.scale(pygame.image.load("image/Bricks/Bricks2.png"), (156, 156)),
          pygame.transform.scale(pygame.image.load("image/Bricks/Bricks3.png"), (156, 156))]
WARNING = [pygame.transform.scale(pygame.image.load("image/other/Warning.png"), (104, 52))]

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = WIDTH
        #self.obstacles_rect = self.image[self.type].get_rect()
        self.fall_vel = 0
        self.phone = False
    def update(self, game_speed , obstacles , phone ):
        self.rect.x -= game_speed
        if phone:
            self.phone = True
        else:
            self.phone = False
        if self.rect.x < -self.rect.width:
            obstacles.pop()  #到畫面外移除
        if self.type == 2:
            if self.rect.y < 624:
                self.rect.y -= self.fall_vel*4
                self.fall_vel -= 1.04
            else:
                self.jump_vel = 0

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class Billboard(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        if self.type == 2:
            self.rect.y = 234
        else:
            self.rect.y = 637


class Bricks(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        if self.type == 2:
            self.rect.y = 234
        else:
            self.rect.y = 637

        #self.obstacles_rect = pygame.Rect(self.rect.x,self.rect.y, 80, 80)
class Warning(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 546
        #self.index = 0
        #self.obstacles_rect = pygame.Rect(self.rect.x, self.rect.y, 80, 80)
    def draw(self, SCREEN):
        if self.phone:
            if self.rect.x > 1300:
                pop = pygame.mixer.Sound("sound/warrning.mp3")
                pop.set_volume(4.0)
                pop.play()
            SCREEN.blit(self.image[self.type], self.rect)
        else:
            if self.rect.x - 104 < 650:
                SCREEN.blit(self.image[self.type], self.rect)

