import pygame
import os
import random

RUNNING = [pygame.transform.scale(pygame.image.load("image/Char/CharRun1.png"), (195, 195)),
           pygame.transform.scale(pygame.image.load("image/Char/CharRun2.png"), (195, 195))]
JUMPING = pygame.transform.scale(pygame.image.load("image/Char/CharJump.png"), (195, 195))
DUCKING = [pygame.transform.scale(pygame.image.load("image/Char/CharDuck1.png"), (195, 195)),
           pygame.transform.scale(pygame.image.load("image/Char/CharDuck2.png"), (195, 195))]
HELMET_R = [pygame.transform.scale(pygame.image.load("image/Char/CharRun1_H.png"), (195, 195)),
           pygame.transform.scale(pygame.image.load("image/Char/CharRun2_H.png"), (195, 195))]
HELMET_J = pygame.transform.scale(pygame.image.load("image/Char/CharJump_H.png"), (195, 195))
HELMET_D = [pygame.transform.scale(pygame.image.load("image/Char/CharDuck1_H.png"), (195, 195)),
           pygame.transform.scale(pygame.image.load("image/Char/CharDuck2_H.png"), (195, 195))]
BIG_R = [pygame.transform.scale(pygame.image.load("image/Char/CharRun1.png"), (585, 585)),
           pygame.transform.scale(pygame.image.load("image/Char/CharRun2.png"), (585, 585))]

class Character:
    X_POS = 104
    Y_POS = 585
    Y_POS_BIG = 338
    Y_POS_DUCK = 611
    JUMP_VEL = 7.8

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.helmet_d = HELMET_D
        self.helmet_r = HELMET_R
        self.helmet_j = HELMET_J
        self.big = BIG_R

        self.char_duck = False
        self.char_run = True
        self.char_jump = False
        self.char_helmet = False
        self.char_big = False
        self.step_index = 0
        self.jump_vel = self.JUMP_VEL  # 跳上、跳下速度
        self.image = self.run_img[0]
        self.rect = pygame.Rect(104 ,364 ,130 ,130)
        self.char_rect = self.image.get_rect()
        self.char_rect.x = self.X_POS
        self.char_rect.y = self.Y_POS

    def update(self, userInput, helmet, big):
        if self.char_duck:
            self.duck()
        if self.char_run:
            self.run()
        if self.char_jump:
            self.jump()

        if self.step_index >= 10:    # 使角色看起來為動畫
            self.step_index = 0
        if userInput[pygame.K_w] and not self.char_jump and not self.char_big and self.char_rect.y == 585:
            self.char_duck = False
            self.char_run = False
            self.char_jump = True
            pop = pygame.mixer.Sound("sound/jump.mp3")
            pop.set_volume(0.3)
            pop.play()
        elif userInput[pygame.K_s] and not self.char_jump and not self.char_big:
            self.char_duck = True
            self.char_run = False
            self.char_jump = False
        elif not (self.char_jump or userInput[pygame.K_s]):
            self.char_duck = False
            self.char_run = True
            self.char_jump = False
        if helmet:
            self.char_helmet = True
        else:
            self.char_helmet = False
        if big:
            self.char_big = True
        else:
            self.char_big = False


    def duck(self):
        if self.char_helmet:
            self.image = self.helmet_d[self.step_index // 5]
        else:
            self.image = self.duck_img[self.step_index // 5]
        self.char_rect = self.image.get_rect()
        self.char_rect.x = self.X_POS
        self.char_rect.y = self.Y_POS_DUCK
        self.step_index += 1
        self.rect = pygame.Rect(self.char_rect.x, self.char_rect.y, 104, 104)
    def run(self):
        if self.char_helmet:
            self.image = self.helmet_r[self.step_index // 5]
        elif self.char_big:
            self.image = self.big[self.step_index // 5]
        else:
            self.image = self.run_img[self.step_index // 5]    # 使角色看起來為動畫
        self.char_rect = self.image.get_rect()
        self.char_rect.x = self.X_POS
        if self.char_big:
            self.char_rect.y = self.Y_POS_BIG
        else:
            self.char_rect.y = self.Y_POS
        self.step_index += 1                         # 使角色看起來為動畫
        self.rect = pygame.Rect(self.char_rect.x, self.char_rect.y, 104, 104)
    def jump(self):
        if self.char_helmet:
            self.image = self.helmet_j
        else:
            self.image = self.jump_img
        if self.char_jump:
            self.char_rect.y -= self.jump_vel * 4  # 調整y座標
            self.jump_vel -= 0.8   # 速度調整
        if self.jump_vel < - self.JUMP_VEL : # 方向像下，所以為負
            self.char_jump = False
            self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.char_rect.x, self.char_rect.y, 104, 104)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.char_rect.x, self.char_rect.y))
