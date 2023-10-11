import pygame
import time
import os
from player import Player
from obstacle import Obstacle
from supplies import Supplies, supply_image
from gun import Gun
from buttons import Buttons
from settings import *



# initialization
#pygame.init()
#pygame.display.set_caption('收集物資')
pygame.mixer.init()

# load image
background_image = pygame.transform.scale(pygame.image.load("image/background/background_1.png"), (WIDTH, HEIGHT))
start_btn_image = pygame.transform.scale(pygame.image.load("image/other/start_button.png"), (190, 78))
title_image = pygame.transform.scale(pygame.image.load("image/title/title_one.png"), (520, 130))
aid_image = pygame.transform.scale(pygame.image.load("image/supplies/first_aid_kit.png"), (45, 45))
food_image = pygame.transform.scale(pygame.image.load("image/supplies/water_and_chocolate.png"), (42, 49))
communication_image = pygame.transform.scale(pygame.image.load("image/supplies/communication_supplies.png"), (47, 36))
helmet_image = pygame.transform.scale(pygame.image.load("image/supplies/helmet.png"), (45, 35))

# load sound
#pygame.mixer.music.load("sound/蒐集物資Very Right.mp3")
shoot_sound = pygame.mixer.Sound("sound/shoot1.mp3")
expl_sound = pygame.mixer.Sound("sound/bomb.mp3")
get_sound = pygame.mixer.Sound("sound/coin03.mp3")
get_gun_sound = pygame.mixer.Sound("sound/powerup01.mp3")
hit_sound = pygame.mixer.Sound("sound/powerdown07.mp3")
start_sound = pygame.mixer.Sound("sound/cat_like1a.mp3")



class Stage_one:
    def __init__(self):
        self.show_init = True
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_time = time.time()
        self.start_time = time.time()
        self.last_shot_time = time.time()
        self.is_running = True
        self.font_size = 45
        self.font = pygame.font.match_font('arial')
        self.score = 0
        self.bg = background_image
        self.title = title_image
        self.start_button = Buttons(WIDTH/2, 3*HEIGHT/4, start_btn_image)
        self.gun_available = False

        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.g = Gun()
        self.all_sprites.add(self.player)

        self.obstacles = pygame.sprite.Group()
        self.supplies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.gun = pygame.sprite.Group()
        self.temp = 0
        self.next_level = 1
        self.level = 1
        self.supplies_count = {'aid_kit': 0, 'food': 0, 'communication': 0, 'helmet': 0}

        # open file
        #self.text_file = open('./txt/supplies_count.txt', 'r+')
        # self.text_file.close()

    # --update--
    def update(self):
        self.game_time = int(time.time() - self.start_time)
        self.all_sprites.update()
        self.obstacle_hit_update()
        self.get_update()
        self.bullet_hit_update()
        self.level_update()
        for i in self.obstacles:
            i.upper = self.level + 1
            i.lower = self.level
        if self.score >= 100 and (not self.gun_available):
            self.gun_appear()
            self.get_gun_update()

    def obstacle_hit_update(self):
        hits = pygame.sprite.spritecollide(self.player, self.obstacles, True)
        for hit in hits:
            hit_sound.play()
            damage = hit.rect.width * hit.rect.height / 1000
            o = Obstacle()
            o.lower = self.level
            o.level_update()
            self.all_sprites.add(o)
            self.obstacles.add(o)
            self.player.health -= damage
            if self.player.health <= 0:
                ff = open("txt/supplies_count.txt", "r+")
                flists = ff.readlines()
                flists[0] = str(int(self.supplies_count['aid_kit'])//5 + int(flists[0])) + "\n"
                flists[1] = str(int(self.supplies_count['food'])//10 + int(flists[1])) + "\n"
                flists[2] = str(int(self.supplies_count['communication'])//10 + int(flists[2])) + "\n"
                flists[3] = str(int(self.supplies_count['helmet'])//5 + int(flists[3])) + "\n"
                for i in range(len(flists)):
                    if int(flists[i]) > 3:
                         flists[i] = str(3) + "\n"
                ff = open("txt/supplies_count.txt", "w+")
                ff.writelines(flists)
                ff.close()

    def get_update(self):
        gets = pygame.sprite.spritecollide(self.player, self.supplies, True)
        for get in gets:
            get_sound.play()
            if get.name == 'aid':
                self.supplies_count['aid_kit'] += 1
            elif get.name == 'choclate' or get.name == 'water':
                self.supplies_count['food'] += 1
            elif get.name == 'phone' or get.name == 'radio':
                self.supplies_count['communication'] += 1
            elif get.name == 'helmet':
                self.supplies_count['helmet'] += 1
            s = Supplies()
            self.all_sprites.add(s)
            self.supplies.add(s)
            self.score += 10

    def bullet_hit_update(self):
        hits = pygame.sprite.groupcollide(self.bullets, self.obstacles, True, True)
        for hit in hits:
            expl_sound.play()
            o = Obstacle()
            o.lower = self.level
            o.level_update()
            self.all_sprites.add(o)
            self.obstacles.add(o)
            self.score += 5

    def get_gun_update(self):
        get = pygame.sprite.spritecollide(self.player, self.gun, True)
        if get:
            get_gun_sound.play()
            self.gun_available =True


    def gun_appear(self):
        self.all_sprites.add(self.g)
        self.gun.add(self.g)

    def level_update(self):
        if self.score >= self.temp + 80 * self.next_level:
            self.level += 1
            for i in self.obstacles:
                i.upper = self.level + 1
                i.lower = self.level

            for i in range(2):
                o = Obstacle()
                o.lower = self.level
                o.level_update()
                self.all_sprites.add(o)
                self.obstacles.add(o)

            for i in range(1):
                s = Supplies()
                self.all_sprites.add(s)
                self.supplies.add(s)
            self.temp += 80 * self.next_level
            self.next_level += 1


    # --draw--
    def draw(self, surf):
        surf.blit(self.bg, (0, 0))
        self.draw_text(surf, str(self.score), self.font_size, WIDTH/2, 10, BLACK)
        self.draw_health(surf, self.player.health, 15, 10)
        self.draw_supplies_gotten()
        pass

    def draw_text(self, surf, text, size, x, y, color):
        font = pygame.font.Font(self.font, size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.centerx = x
        text_rect.top = y
        surf.blit(text_surf, text_rect)
        pass

    def draw_health(self, surf, hp, x, y):
        if hp < 0:
            hp = 0
            f = open("txt/points.txt", "r+")
            flist = f.readlines()
            if int(flist[0]) < self.score:
                flist[0] = str(self.score) + "\n"
                f = open("txt/points.txt", "w+")
                f.writelines(flist)
                f.close()
            self.is_running = False
        hp_bar_length = 200
        hp_bar_height = 20
        outline_bar = pygame.Rect(x, y, hp_bar_length, hp_bar_height)
        fill_bar = pygame.Rect(x, y, (hp/100)*hp_bar_length, hp_bar_height)
        pygame.draw.rect(surf, BLACK, outline_bar)
        pygame.draw.rect(surf, GREEN, fill_bar)
        pygame.draw.rect(surf, WHITE, outline_bar, 3)
        pass
    def draw_supplies_gotten(self):
        self.win.blit(aid_image, (15, 30))
        self.draw_text(self.win, str(self.supplies_count['aid_kit']), 30, 80, 30, BLACK)
        self.win.blit(food_image, (15, 70))
        self.draw_text(self.win, str(self.supplies_count['food']), 30, 80, 70, BLACK)
        self.win.blit(communication_image, (15, 115))
        self.draw_text(self.win, str(self.supplies_count['communication']), 30, 80, 110, BLACK)
        self.win.blit(helmet_image, (15, 150))
        self.draw_text(self.win, str(self.supplies_count['helmet']), 30, 80, 150, BLACK)


        pass


    def draw_init(self, surf):
        self.player.health = 100
        self.score = 0
        self.gun_available = False
        self.g.kill()
        self.g = Gun()
        self.temp = 0
        self.level = 1
        self.next_level = 1
        self.supplies_count = {'aid_kit': 0, 'food': 0, 'communication': 0, 'helmet': 0}
        #self.text_file = open('./txt/supplies_count.txt', 'w')
        for i in self.bullets:
            i.kill()
        for i in self.obstacles:
            i.kill()
        for i in self.supplies:
            i.kill()

        for i in range(3):
            o = Obstacle()
            self.all_sprites.add(o)
            self.obstacles.add(o)

        for i in range(4):
            s = Supplies()
            self.all_sprites.add(s)
            self.supplies.add(s)

        surf.blit(self.bg, (0, 0))
        surf.blit(self.title, (465, 180))
        self.start_button.draw(surf)
        pygame.display.update()
        waiting = True
        clock = pygame.time.Clock()
        while waiting and self.is_running:
            clock.tick(FPS)
            for event in pygame.event.get():
                # quit the game
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.start_button.is_clicked(x, y):
                        start_sound.play()
                        waiting = False
                    pass

        pass

    # --about game--
    def game_operation(self):
        pass


    def game_run(self):


        # game loop
        clock = pygame.time.Clock()
        while self.is_running:
            #初始畫面
            if self.show_init:
                self.draw_init(self.win)
                self.show_init = False
            clock.tick(FPS)
            # 取得輸入
            # event loop
            for event in pygame.event.get():
                # quit the game
                if event.type == pygame.QUIT:
                    self.is_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.gun_available:
                        now = time.time()
                        if now - self.last_shot_time > 0.2:
                            shoot_sound.play()
                            b = self.player.shoot()
                            self.all_sprites.add(b)
                            self.bullets.add(b)
                            self.last_shot_time = now
                    pass

                if event.type == pygame.MOUSEBUTTONDOWN:

                    pass


            # 更新遊戲
            self.update()
            self.game_operation()


            # 畫面顯示
            self.draw(self.win)
            self.all_sprites.draw(self.win)
            if self.gun_available:
                self.player.draw_gun(self.win)
            pygame.display.update()

        return 0





