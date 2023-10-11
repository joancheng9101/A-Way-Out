import pygame
import time
from question import Question
from answer import Answer
from position import position_x, position_y
from endpage import Endpage
from buttons import*
#init

pygame.mixer.init()

#load bg
background = pygame.transform.scale(pygame.image.load("image/background/background_3.jpg"), (1430, 780))
start_btn_image = pygame.transform.scale(pygame.image.load("image/other/start_button.png"), (190, 78))
title_image = pygame.transform.scale(pygame.image.load("image/title/title_three.png"), (520, 130))


class Stage_three:
    def __init__(self):
        self.win = pygame.display.set_mode((1430, 780))
        self.bg = background
        self.is_running = True
        self.font_size = 40
        self.font = pygame.font.Font("fonts/Alphabet_soup.ttf", self.font_size)
        self.score_font = pygame.font.Font("fonts/New-Super-Mario-Font-U-1.ttf", self.font_size)
        self.bonus_font = pygame.font.Font("fonts/New-Super-Mario-Font-U-1.ttf", 60)
        self.start_sound = pygame.mixer.Sound("sound/cat_like1a.mp3")
        self.game_time = time.time()
        self.start_time = time.time()

        self.question = Question()
        self.answer = Answer()
        self.end = Endpage()

        self.Inhomepage = "Inhomepage"
        self.Inquestion = None
        self.Inanswer = 1
        self.start_button = Buttons(1430 / 2, 3 * 780 / 4, start_btn_image)
        self.position_x = position_x
        self.position_y = position_y
        self.num = 0
        self.play = True
        self.pop = pygame.mixer.Sound("sound/countdown.mp3")
        self.out = False
    def Homepage(self, surf):
        surf.blit(self.bg, (0, 0))
        self.win.blit(background, (0, 0))
        self.win.blit(title_image, (465, 350))
        self.start_button.draw(self.win)

    def draw_time(self, surf):
        self.game_time = int(time.time() - self.start_time)
        if 20-self.game_time < 0:
            self.out = True
            self.end.draw_end(self.win)
        else:
            if 20 - self.game_time == 5 and self.play:
                self.pop.set_volume(1.0)
                self.pop.play()
                self.play = False
            time_text = self.font.render("{}s".format(20-self.game_time), True, (0, 0, 0))
            time_rect = time_text.get_rect()
            time_rect.topleft = (50, 100)
            surf.blit(time_text, time_rect)

    def draw_score(self, surf):
        self.game_time = int(time.time() - self.start_time)
        if 20 - self.game_time < 0:
            self.end.draw_bonus(self.answer.score, self.win)
        else:
            game_score = self.score_font.render("score: {}".format(self.answer.score), True, (0, 0, 0))
            score_rect = game_score.get_rect()
            score_rect.topleft = (50, 30)
            surf.blit(game_score, score_rect)


    def game_run(self):
        clock = pygame.time.Clock()
        clock.tick(60)

        while self.is_running:
            if self.Inhomepage == "Inhomepage":
                self.Homepage(self.win)
            elif self.Inquestion == "Inquestion":
                if self.num == 9:
                    self.end.draw_end(self.win)
                    self.end.draw_bonus(self.answer.score, self.win)
                else:
                    self.question.draw_question(self.num, self.win)
                    self.draw_time(self.win)
                    self.draw_score(self.win)
            elif self.Inanswer == "Inanswer":
                self.answer.draw_ans(0, 0, self.num-1, self.win)
                self.draw_time(self.win)
                self.draw_score(self.win)




            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN and self.out:
                    if event.key == pygame.K_RIGHT:
                        self.is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.start_button.is_clicked(x, y) and self.Inhomepage is not None:
                        self.start_sound.play()
                        self.start_time = time.time()
                        self.Inhomepage = None
                        self.Inquestion = "Inquestion"
                        self.Inanswer = None
                        self.question.draw_question(self.num, self.win)
                        self.draw_time(self.win)

                    elif x in range(1307, 1390) and y in range(702, 748) and self.Inquestion == None:
                        self.Inquestion = "Inquestion"
                        self.Inanswer = None
                        print(self.num)
                        if self.num == 9:
                            self.out = True
                            self.end.draw_bonus(self.answer.score, self.win)
                        else:
                            self.question.draw_question(self.num, self.win)
                    elif self.num < 9:
                        if x in range (self.position_x[self.num][0], self.position_x[self.num][1]) \
                            and y in range(self.position_y[self.num][0], self.position_y[self.num][1]) \
                            and self.Inanswer == None:
                            self.Inquestion = None
                            self.Inanswer = "Inanswer"
                            self.answer.draw_ans(x, y, self.num, self.win)
                            x = None
                            y = None
                            self.num += 1
                    elif 1317 <= x <= 1419 and 685 <= y <= 780 and self.out:
                        self.is_running = False
                    if self.num < 9 and self.out:
                        if 1317 <= x <= 1419 and 685 <= y <= 780 :
                            self.is_running = False


            pygame.display.update()
        return 0



