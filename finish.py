import pygame
import linecache
import os
WIN_WIDTH = 1430
WIN_HEIGHT = 780
FPS = 60
result_image = pygame.transform.scale(pygame.image.load("image/background/result.png"), (WIN_WIDTH, WIN_HEIGHT))
red_image = pygame.transform.scale(pygame.image.load("image/other/red.png"), (100,100))
class Finish:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.state = 0
        self.red = red_image
    def update(self):
        pass

    def draw(self, surf):
        f = open("./txt/points.txt", "r+")
        flist = f.readlines()
        result = (int(flist[0]) + int(flist[1])) * int(flist[2])/100
        f.close()
        red_rect = self.red.get_rect()
        if result <= 6000:
            red_rect.center = (820, 665)
        elif 6000 < result <= 7000:
            red_rect.center = (835, 555)
        elif 7000 < result <= 8000:
            red_rect.center = (840, 610)
        else:
            red_rect.center = (850, 500)
        surf.blit(result_image, (0, 0))
        surf.blit(self.red, red_rect)


    def game_run(self):
        # game loop
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:# 若使用者按下角落的打叉按鈕，則將running定為False跳出迴圈
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        if 1319 <= x <= 1418 and 706 <= y <= 780:
                            running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        running = False

            # 更新遊戲
            self.update()
            # 畫面顯示
            self.draw(self.win)
            pygame.display.update()
        return 0



