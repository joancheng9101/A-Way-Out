import pygame
from position import*

image_size = (1430, 780)
ans_list = [pygame.transform.scale(pygame.image.load("image/Answer_list/A1.jpg"), image_size),
            pygame.transform.scale(pygame.image.load("image/Answer_list/A2.jpg"), image_size),
            pygame.transform.scale(pygame.image.load("image/Answer_list/A3.jpg"), image_size),
            pygame.transform.scale(pygame.image.load("image/Answer_list/A4.jpg"), image_size),
            pygame.transform.scale(pygame.image.load("image/Answer_list/A5.jpg"), image_size),
            pygame.transform.scale(pygame.image.load("image/Answer_list/A6.jpg"), image_size),
            pygame.transform.scale(pygame.image.load("image/Answer_list/A7.jpg"), image_size),
            pygame.transform.scale(pygame.image.load("image/Answer_list/A8.jpg"), image_size),
            pygame.transform.scale(pygame.image.load("image/Answer_list/A9.jpg"), image_size),
            ]

class Answer():
    def __init__(self):
        self.ans = ans_list
        self.score = 0
        self.position_y_ans = position_y_ans
        self.position_y = position_y

    def draw_ans(self, x, y, num, surf):
        surf.blit(self.ans[num], (0, 0))
        if y in range(self.position_y_ans[num][0], self.position_y_ans[num][1]):
            self.score += 10
            pop = pygame.mixer.Sound("sound/yes.mp3")
            pop.set_volume(0.8)
            pop.play()
        elif y in range(self.position_y[num][0], self.position_y[num][1]):
            pop = pygame.mixer.Sound("sound/wrong.mp3")
            pop.set_volume(1.5)
            pop.play()
            self.score += 0
        else:
            self.score += 0