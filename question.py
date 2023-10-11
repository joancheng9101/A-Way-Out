import pygame

image_size = (1430, 780)
qt_list = [pygame.transform.scale(pygame.image.load("image/Question_List/Q1.jpg"), image_size),
           pygame.transform.scale(pygame.image.load("image/Question_List/Q2.jpg"), image_size),
           pygame.transform.scale(pygame.image.load("image/Question_List/Q3.jpg"), image_size),
           pygame.transform.scale(pygame.image.load("image/Question_List/Q4.jpg"), image_size),
           pygame.transform.scale(pygame.image.load("image/Question_List/Q5.jpg"), image_size),
           pygame.transform.scale(pygame.image.load("image/Question_List/Q6.jpg"), image_size),
           pygame.transform.scale(pygame.image.load("image/Question_List/Q7.jpg"), image_size),
           pygame.transform.scale(pygame.image.load("image/Question_List/Q8.jpg"), image_size),
           pygame.transform.scale(pygame.image.load("image/Question_List/Q9.jpg"), image_size),
           ]

class Question():
    def __init__(self):
        self.qt = qt_list

    def draw_question(self, num, surf):
        surf.blit(self.qt[num], (0, 0))