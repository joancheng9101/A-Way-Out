import pygame
WIN_WIDTH = 1430
WIN_HEIGHT = 780
FPS = 60
bag_image = pygame.transform.scale(pygame.image.load("image/background/bag.png"), (WIN_WIDTH, WIN_HEIGHT))
class Bag:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.state = 0
        self.font = pygame.font.Font('fonts/New-Super-Mario-Font-U-1.ttf', 50)
    def bag_in(self,surf):
        ff = open("./txt/supplies_count.txt", "r+")
        flists = ff.readlines()
        text_one = self.font.render(str(int(flists[0])), True, (0, 0, 0))
        text_two = self.font.render(str(int(flists[2])), True, (0, 0, 0))
        text_three = self.font.render(str(int(flists[3])), True, (0, 0, 0))
        text_four = self.font.render(str(int(flists[1])), True, (0, 0, 0))
        text_one_ = self.font.render(str(int(flists[0]))+" (FULL)", True, (0, 0, 0))
        text_two_ = self.font.render(str(int(flists[2]))+" (FULL)", True, (0, 0, 0))
        text_three_ = self.font.render(str(int(flists[3]))+" (FULL)", True, (0, 0, 0))
        text_four_ = self.font.render(str(int(flists[1]))+" (FULL)", True, (0, 0, 0))
        textRect_one = text_one.get_rect()
        textRect_two = text_one.get_rect()
        textRect_three = text_one.get_rect()
        textRect_four = text_one.get_rect()
        textRect_one_ = text_one.get_rect()
        textRect_two_ = text_one.get_rect()
        textRect_three_ = text_one.get_rect()
        textRect_four_ = text_one.get_rect()
        textRect_one.center = (628, 305)
        textRect_two.center = (628, 450)
        textRect_three.center = (628, 597)
        textRect_four.center = (628, 747)
        textRect_one_.center = (628, 305)
        textRect_two_.center = (628, 450)
        textRect_three_.center = (628, 597)
        textRect_four_.center = (628, 747)
        if int(flists[0]) == 3:
            surf.blit(text_one_, textRect_one_)
        else:
            surf.blit(text_one, textRect_one)
        if int(flists[2]) == 3:
            surf.blit(text_two_, textRect_two_)
        else:
            surf.blit(text_two, textRect_two)
        if int(flists[3]) == 3:
            surf.blit(text_three_, textRect_three_)
        else:
            surf.blit(text_three, textRect_three)
        if int(flists[1]) == 3:
            surf.blit(text_four_, textRect_four_)
        else:
            surf.blit(text_four, textRect_four)
        surf.blit(text_two, textRect_two)
        surf.blit(text_three, textRect_three)
        surf.blit(text_four, textRect_four)
        ff.close()
        pass
    def update(self):
        pass

    def draw(self, surf):
       if self.state == 0:
           surf.blit(bag_image, (0, 0))
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
                    if 1319 <= x <= 1418 and 706 <= y <= 780 :
                            running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                            running = False
            # 更新遊戲
            self.update()
            # 畫面顯示
            self.draw(self.win)
            self.bag_in(self.win)
            pygame.display.update()
        return 0



