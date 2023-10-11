import pygame
image_size = (1430, 780)
end = pygame.transform.scale(pygame.image.load("image/background/End.png"), image_size)


class Endpage():
    def __init__(self):
        self.end = end
        self.bonus_font = pygame.font.Font("fonts/New-Super-Mario-Font-U-1.ttf", 60)

    def draw_end(self, surf):
        surf.blit(self.end, (0, 0))

    def draw_bonus(self, score, surf):
        self.bonus = 0
        if score <= 30:
            self.bonus = 105
            game_bonus = self.bonus_font.render("bonus: {}%".format(self.bonus), True, (0, 0, 0))
            bonus_rect = game_bonus.get_rect()
            bonus_rect.center = (715, 390)
            surf.blit(game_bonus, bonus_rect)
        elif score <= 60:
            self.bonus = 110
            game_bonus = self.bonus_font.render("bonus: {}%".format(self.bonus), True, (0, 0, 0))
            bonus_rect = game_bonus.get_rect()
            bonus_rect.center = (715, 390)
            surf.blit(game_bonus, bonus_rect)
        elif score <= 80:
            self.bonus = 125
            game_bonus = self.bonus_font.render("bonus: {}%".format(self.bonus), True, (0, 0, 0))
            bonus_rect = game_bonus.get_rect()
            bonus_rect.center = (715, 390)
            surf.blit(game_bonus, bonus_rect)
        elif score <= 90:
            self.bonus = 150
            game_bonus = self.bonus_font.render("bonus: {}%".format(self.bonus), True, (0, 0, 0))
            bonus_rect = game_bonus.get_rect()
            bonus_rect.center = (715, 390)
            surf.blit(game_bonus, bonus_rect)
        f = open("txt/points.txt", "r+")
        flist = f.readlines()
        if int(flist[2]) < self.bonus:
            flist[2] = str(self.bonus) + "\n"
            f = open("txt/points.txt", "w+")
            f.writelines(flist)
            f.close()