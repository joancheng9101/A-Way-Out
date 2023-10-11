import subprocess, time
from controller import*
import pygame
import linecache
from stage_one import*
from stage_two import*
from stage_three import*
from story_one import*
from story_two import*
from story_three import*
from finish import *
from bag import *
from settings import *
WIN_WIDTH = 1430
WIN_HEIGHT = 780
FPS = 60
background_image = pygame.transform.scale(pygame.image.load("picture/gamestart.png"), (WIN_WIDTH, WIN_HEIGHT))
lock_image = pygame.transform.scale(pygame.image.load("picture/lock.png"), (130, 130))
scoreboard_image = pygame.transform.scale(pygame.image.load("picture/scoreboard.png"), (169, 169))
pygame.display.set_caption('Team 4')
file_path_one = './story_one/main.py'
file_path_two = './stage_one/main.py'
file_path_three = './story_two/main.py'
file_path_four = './stage_two/main.py'
file_path_five = './story_three/main.py'
file_path_six = './stage_three/main.py'
file_path_seven = './finish/main.py'
file_path_bag = './bag/main.py'
pygame.init()
#if __name__ == '__main__':
    #main()
pygame.display.set_caption('逃出生天')

class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.Font('fonts/New-Super-Mario-Font-U-1.ttf', 40)
        self.get_state = 0
        self.pass_list = [0, 0, 0, 0, 0, 0]
        self.lock_list = [(793, 325), (1105, 325), (195, 585), (494, 585), (793, 585), (1105, 585)]
        self.scoreboard_list = [(773.5, 117),(169, 377),(773.5, 377)]
        self.score_list = [(858, 234),(253.5, 487.5),(858, 487.5)]
        self.text_score_list = ['a','b','c']
        self.points_list = [0, 0, 0]
        self.points_total = 0
        self.points_three = linecache.getline('points.txt', 3)
        self.points_one = 0
        self.points_two = 0
        self.points_three = 0
        self.font_size = 46
        self.font_points = pygame.font.Font("fonts/New-Super-Mario-Font-U-1.ttf", self.font_size)
    def open_file(self,child):
        while child.poll() is None:
            print("parent: child (pid = %d) is still running" % child.pid)
            # do parent stuff
            time.sleep(1)
        print("parent: child has terminated, returncode = %d" % child.returncode)
        self.get_state = 0

    def update(self):
        pass

    def draw(self, surf):
        # ---第一題---
        # 請把1.地圖背景 2.敵人(水)畫出來
        surf.blit(background_image, (0, 0))# 地圖背景
        for index in range(len(self.pass_list)):
            if self.pass_list[index] == 0:
                surf.blit(lock_image, self.lock_list[index])
        for i in range(len(self.scoreboard_list)):
            if self.pass_list[2*i]:
                surf.blit(scoreboard_image, self.scoreboard_list[i])
    def score(self,surf):
        f = open("./txt/points.txt", "r+")
        flist = f.readlines()
        self.points_one = int(flist[0])
        self.points_two = int(flist[1])
        self.points_three = int(flist[2])
        self.points_total = (int(self.points_one) + int(self.points_two)) * int(self.points_three) / 100
        text = self.font.render("Points: " + str(self.points_total) , True, (123, 90, 16))
        self.text_score_list[0] = self.font_points.render(str(self.points_one), True, (123, 90, 16))
        self.text_score_list[1] = self.font_points.render(str(self.points_two), True, (123, 90, 16))
        self.text_score_list[2] = self.font_points.render(str(self.points_three)+" %" , True, (123, 90, 16))
        textRect = text.get_rect()
        textRect.center = (1200, 52)
        surf.blit(text, textRect)
        for i in range(len(self.scoreboard_list)):
            if self.pass_list[2 * i]:
                textRect = self.text_score_list[i].get_rect()
                textRect.center = self.score_list[i]
                surf.blit(self.text_score_list[i], textRect)
    def draw_time(self, surf):
        pass

    def game_run(self):
        # game loop
        running = True
        clock = pygame.time.Clock()
        pygame.mixer.music.load("sound/So Bueno.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 若使用者按下角落的打叉按鈕，則將running定為False跳出迴圈
                    if self.get_state == 0:
                        clear_p = open("txt/points.txt", "w+")
                        clear_p.write("0\n0\n100\n")
                        clear_p.close()
                        clear_s = open("txt/supplies_count.txt", "w+")
                        clear_s.write("1\n1\n1\n1\n")
                        clear_s.close()
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 20 <= x <= 102 and 705 <= y <= 780:
                        clear_p = open("txt/points.txt", "w+")
                        clear_p.write("0\n0\n100\n")
                        clear_p.close()
                        clear_s = open("txt/supplies_count.txt", "w+")
                        clear_s.write("1\n1\n1\n1\n")
                        clear_s.close()
                        self.pass_list = [0, 0, 0, 0, 0, 0]
                    if 1221 <= x <= 1299 and  714 <= y <= 780:
                        pygame.mixer.music.unpause()
                    elif 1317 <= x <= 1410 and  714 <= y <= 780:
                        pygame.mixer.music.pause()
                    self.get_state = controller(x, y)
                    pygame.mouse.set_pos(156, 325)

            if self.get_state == 1:
                pygame.mixer.music.load("sound/Silver.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(-1)
                story_one_main = Story_one()
                if story_one_main.game_run() == 0:
                    pygame.mixer.music.load("sound/So Bueno.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    self.get_state = 0
                    self.pass_list[0] = 1
            elif self.get_state == 2:
                if self.pass_list[0]:
                    pygame.mixer.music.load("sound/蒐集物資Very Right.mp3")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.3)
                    stage_one_main = Stage_one()
                    if stage_one_main.game_run() == 0:
                        pygame.mixer.music.load("sound/So Bueno.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                        self.points_one = linecache.getline('txt/points.txt', 1)
                        self.get_state = 0
                        self.pass_list[1] = 1
                else:
                    self.get_state = 0
            elif self.get_state == 3:
                if self.pass_list[1]:
                    pygame.mixer.music.load("sound/Tidal Wave .mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    story_two_main = Story_two()
                    if story_two_main.game_run() == 0:
                        pygame.mixer.music.load("sound/So Bueno.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                        self.get_state = 0
                        self.pass_list[2] = 1
                else:
                    self.get_state = 0
            elif self.get_state == 4:
                if self.pass_list[2]:
                    pygame.mixer.music.load("sound/Friction Looks.mp3")
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                    #stage_two_main = stage_two()
                    if stage_two() == 0:
                        pygame.mixer.music.load("sound/So Bueno.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                        self.get_state = 0
                        self.pass_list[3] = 1
                        self.points_two = linecache.getline('txt/points.txt', 2)
                else:
                    self.get_state = 0
            elif self.get_state == 5:
                if self.pass_list[3]:
                    pygame.mixer.music.load("sound/Going, Going, Gone.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    story_three_main = Story_three()
                    if story_three_main.game_run() == 0:
                        pygame.mixer.music.load("sound/So Bueno.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                        self.pass_list[4] = 1
                        self.get_state = 0
                else:
                    self.get_state = 0
            elif self.get_state == 6:
                if self.pass_list[4]:
                    pygame.mixer.music.load("sound/music.mp3")
                    pygame.mixer.music.play(-1)
                    stage_three_main = Stage_three()
                    if stage_three_main.game_run() == 0:
                        pygame.mixer.music.load("sound/So Bueno.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                        self.pass_list[5] = 1
                        self.points_three = linecache.getline('txt/points.txt', 3)
                        self.get_state = 0
                else:
                    self.get_state = 0
            elif self.get_state == 7:
                pygame.mixer.music.load("sound/win.mp3")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)
                finish_main = Finish()
                if finish_main.game_run() == 0:
                    pygame.mixer.music.load("sound/So Bueno.mp3")
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play(-1)
                    self.get_state = 0
            elif self.get_state == 8:
                    pygame.mixer.music.load("sound/Splashing Around .webm")
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play(-1)
                    bag_main = Bag()
                    if bag_main.game_run() == 0:
                        pygame.mixer.music.load("sound/So Bueno.mp3")
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play(-1)
                        self.get_state = 0
            elif self.get_state == 0:
            # 更新遊戲
                self.update()
            # 畫面顯示
                self.draw(self.win)
                self.score(self.win)

            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.game_run()

