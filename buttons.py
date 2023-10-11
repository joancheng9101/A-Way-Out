import pygame
from settings import *

class Buttons:
    def __init__(self, x, y, btn_image):
        self.x = x
        self.y = y
        self.image = btn_image
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def is_clicked(self, x, y):
        if (self.x - self.width/2) < x < (self.x + self.width/2) \
                and (self.y - self.height/2) < y < (self.y + self.height/2):
            return True
        pass

    def draw(self, surf):
        surf.blit(self.image, (self.x - self.width/2, self.y - self.height/2))  # 畫出按鈕
        pass