import pygame
WIN_WIDTH = 1430
WIN_HEIGHT = 780
FPS = 60
one = pygame.transform.scale(pygame.image.load("image/story/story1-1.png"), (WIN_WIDTH, WIN_HEIGHT))
two = pygame.transform.scale(pygame.image.load("image/story/story1-2.png"), (WIN_WIDTH, WIN_HEIGHT))
three = pygame.transform.scale(pygame.image.load("image/story/story1-3.png"), (WIN_WIDTH, WIN_HEIGHT))
four = pygame.transform.scale(pygame.image.load("image/story/story1-4.png"), (WIN_WIDTH, WIN_HEIGHT))
five = pygame.transform.scale(pygame.image.load("image/story/story1-5.png"), (WIN_WIDTH, WIN_HEIGHT))

class Story_one:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.state = 0
    def update(self):
        pass

    def draw(self, surf):
       if self.state == 0:
           surf.blit(one, (0, 0))
       elif self.state == 1:
           surf.blit(two, (0, 0))
       elif self.state == 2:
           surf.blit(three, (0, 0))
       elif self.state == 3:
           surf.blit(four, (0, 0))
       elif self.state == 4:
           surf.blit(five, (0, 0))
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
                    x, y = pygame.mouse.get_pos()
                    if 1214 <= x <= 1306 and 706 <= y <= 780 :
                        if self.state != 0:
                            self.state -= 1
                    elif 1319 <= x <= 1418 and 706 <= y <= 780 :
                        if self.state != 4:
                            self.state += 1
                        else:
                            running = False
                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                         if self.state != 0:
                             self.state -= 1
                     elif event.key == pygame.K_RIGHT:
                         if self.state != 4:
                            self.state += 1
                         else:
                            running = False
            # 更新遊戲
            self.update()
            # 畫面顯示
            self.draw(self.win)
            pygame.display.update()
        return 0



