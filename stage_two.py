from buttons import*
from obstacles_two import*
from settings import*

# Global Constants
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
HEART = pygame.transform.scale(pygame.image.load("image/Other/heart.png"), (65, 65))
FOOD = pygame.transform.scale(pygame.image.load("image/supplies/water_and_chocolate.png"), (65, 65))
PHONE = pygame.transform.scale(pygame.image.load("image/supplies/communication_supplies.png"), (65, 65))
HELMET = pygame.transform.scale(pygame.image.load("image/supplies/helmet.png"), (60, 60))
HELP = pygame.transform.scale(pygame.image.load("image/supplies/first_aid_kit.png"), (70, 70))
UP = pygame.transform.scale(pygame.image.load("image/Other/up.png"), (75, 65))
DOWN = pygame.transform.scale(pygame.image.load("image/Other/down.png"), (65, 60))
LEFT = pygame.transform.scale(pygame.image.load("image/Other/left.png"), (65, 70))
RIGHT = pygame.transform.scale(pygame.image.load("image/Other/right.png"), (65, 65))
BG = pygame.transform.scale(pygame.image.load("image/background/background_2.png"), (WIDTH, HEIGHT))  #載入背景
title_image = pygame.transform.scale(pygame.image.load("image/title/title_two.png"), (520, 130))
start_btn_image = pygame.transform.scale(pygame.image.load("image/other/start_button.png"), (190, 78))
start_sound = pygame.mixer.Sound("sound/cat_like1a.mp3")



def stage_two():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, live, helmet,big, phone,init,run
    ff = open("txt/supplies_count.txt", "r+")
    flists = ff.readlines()
    bonus = [int(flists[0]), int(flists[2]) , int(flists[3]) ,  int(flists[1])]
    ff.close()
    run = True
    clock = pygame.time.Clock()
    player = Character()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('fonts/New-Super-Mario-Font-U-1.ttf', 40)
    font_num = pygame.font.Font('fonts/New-Super-Mario-Font-U-1.ttf', 46)
    obstacles = []
    death_count = 0
    live = 3
    helmet = False
    big = False
    phone = False
    counter, text = 5, "5".rjust(3)
    counter_p, text_p = 20, "20".rjust(3)
    pygame.time.set_timer(pygame.USEREVENT,1000)
    init= True
    def score():
        global points, game_speed
        points += 1
        if points % 250 == 0:  # 每100分，增加速度
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        food_num = font_num.render(" :  " + str(bonus[3]), True, (0, 0, 0))
        phone_num = font_num.render(" :  " + str(bonus[1]), True, (0, 0, 0))
        help_num = font_num.render(" :  " + str(bonus[0]), True, (0, 0, 0))
        helmet_num = font_num.render(" :  " + str(bonus[2]), True, (0, 0, 0))
        textRect = text.get_rect()
        food_num_rect = food_num.get_rect()
        phone_num_rect = phone_num.get_rect()
        help_num_rect = help_num.get_rect()
        heartRect_one = HEART.get_rect()
        heartRect_two = HEART.get_rect()
        heartRect_three = HEART.get_rect()
        up_rect = UP.get_rect()
        down_rect = DOWN.get_rect()
        left_rect = LEFT.get_rect()
        right_rect = RIGHT.get_rect()
        food_rect = FOOD.get_rect()
        phone_rect = PHONE.get_rect()
        helmet_rect = HELMET.get_rect()
        help_rect = HELP.get_rect()
        helmet_num_rect = helmet_num.get_rect()
        textRect.center = (1300, 52)
        food_num_rect.center = (1118, 52)
        help_num_rect.center =(416,52)
        phone_num_rect.center =(650,52)
        helmet_num_rect.center = (884,52)
        heartRect_one.center = (39, 52)
        heartRect_two.center = (117, 52)
        heartRect_three.center = (195, 52)
        food_rect.center = (1053, 52)
        help_rect.center = (351,52)
        phone_rect.center = (585,52)
        helmet_rect.center = (819,52)
        up_rect.center = (286,52)
        down_rect.center = (507,52)
        right_rect.center = (975,52)
        left_rect.center = (741,52)
        SCREEN.blit(text, textRect)
        SCREEN.blit(FOOD, food_rect)
        SCREEN.blit(HELMET, helmet_rect)
        SCREEN.blit(food_num, food_num_rect)
        SCREEN.blit(RIGHT, right_rect)
        SCREEN.blit(HELP, help_rect)
        SCREEN.blit(help_num, help_num_rect)
        SCREEN.blit(UP, up_rect)
        SCREEN.blit(RIGHT, right_rect)
        SCREEN.blit(PHONE, phone_rect)
        SCREEN.blit(phone_num, phone_num_rect)
        SCREEN.blit(DOWN, down_rect)
        SCREEN.blit(LEFT, left_rect)
        SCREEN.blit(helmet_num, helmet_num_rect)
        if live == 3:
            SCREEN.blit(HEART, heartRect_one)
            SCREEN.blit(HEART, heartRect_two)
            SCREEN.blit(HEART, heartRect_three)
        elif live == 2:
            SCREEN.blit(HEART, heartRect_one)
            SCREEN.blit(HEART, heartRect_two)
        elif live == 1:
            SCREEN.blit(HEART, heartRect_one)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))  # 接替畫面
            x_pos_bg = 0
        x_pos_bg -= game_speed
    def draw_init():
        global run
        start_button = Buttons(WIDTH / 2, 3 * HEIGHT / 4, start_btn_image)
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(title_image, (465, 180))
        start_button.draw(SCREEN)
        pygame.display.update()
        waiting = True
        clock = pygame.time.Clock()
        while waiting and run:
            clock.tick(30)
            for event in pygame.event.get():
                # quit the game
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if start_button.is_clicked(x, y):
                        start_sound.play()
                        waiting = False
                    pass


    while run:
        if init:
            draw_init()
            init = False
        background()
        #clock.tick(FPS)
        font_number = pygame.font.SysFont("fonts/New-Super-Mario-Font-U-1.ttf", 130)
        font_number_p = pygame.font.SysFont("fonts/New-Super-Mario-Font-U-1.ttf", 65)
        userInput = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.USEREVENT and big == True:
                counter -= 1
                if counter > 0:
                    text = str(counter).rjust(3)
                else:
                    text = ""
                    counter, text = 5, "5".rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    #font_number = pygame.font.SysFont("New-Super-Mario-Font-U-1.ttf", 100)
                    big = False
            if event.type == pygame.USEREVENT and phone == True:
                counter_p -= 1
                if counter_p > 0:
                    text_p = str(counter_p).rjust(3)
                else:
                    text_p = ""
                    counter_p, text_p = 20, "20".rjust(3)
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    #font_number = pygame.font.SysFont("New-Super-Mario-Font-U-1.ttf", 30)
                    phone = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if live < 3 and bonus[0] > 0:
                        bonus[0] -= 1
                        live += 1
                elif event.key == pygame.K_LEFT and big == False and helmet == False and bonus[2] > 0:
                    bonus[2] -= 1
                    helmet = True
                elif event.key == pygame.K_RIGHT and big == False and helmet == False and bonus[3] > 0:
                    bonus[3] -= 1
                    big = True
                    pop = pygame.mixer.Sound("sound/big.mp3")
                    pop.set_volume(0.4)
                    pop.play()
                elif event.key == pygame.K_DOWN and big == False and phone == False and bonus[1] > 0:
                    bonus[1] -= 1
                    phone = True
        if big == True:
            SCREEN.blit(font_number.render(text, True, (0,0,0)), (325,260))
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        if phone == True:
            SCREEN.blit(font_number_p.render(text_p, True, (0, 0, 0)), (585, 104))
        player.draw(SCREEN)       # 顯示角色

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Bricks(BRICKS))
            elif random.randint(0, 2) == 1:
                obstacles.append(Billboard(BILLBOARD))
            elif random.randint(0, 2) == 2:
                obstacles.append(Warning(WARNING))


        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles, phone)
            #if obstacle.rect.x - player.char_rect.x < 50 and player.char_duck == False and player.char_jump == False:
            if player.rect.colliderect(obstacle.rect):
                #pygame.time.delay(1500)    # 兩秒
                death_count += 1
                if helmet == False and big == False:
                    live -= 1
                elif helmet == True:
                    helmet = False
                #if phone == True and big == False and helmet == False:
                    #phone = False
                if big == False:
                    obstacle.rect.x = WIDTH
                if live == 0:
                    fff = open("txt/supplies_count.txt", "r+")
                    flists_ = fff.readlines()
                    flists_[0] = str(int(bonus[0]) )+ "\n"
                    flists_[1] = str(int(bonus[3])) + "\n"
                    flists_[2] = str(int(bonus[1])) + "\n"
                    flists_[3] = str(int(bonus[2])) + "\n"
                    fff = open("txt/supplies_count.txt", "w+")
                    fff.writelines(flists_)
                    fff.close()
                    f = open("txt/points.txt", "r+")
                    flist = f.readlines()
                    if int(flist[1]) < points:
                        #f = open("txt/points.txt", "r+")
                        #flist = f.readlines()
                        flist[1] = str(points) + "\n"
                        f = open("txt/points.txt", "w+")
                        f.writelines(flist)
                        f.close()
                    run = False
        player.update(userInput, helmet, big)  # 更新角色
        score()   # 顯示分數
        clock.tick(30)
        pygame.display.update()
    return 0



