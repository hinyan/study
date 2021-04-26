import pygame
import random
import configuration as c 

screen = pygame.display.set_mode((600,600))
# 生成文字函数(文字大小，内容，颜色)
def draw_text(d_x,text_z,colors):
    pygame.font.init()
    font = pygame.font.SysFont('cooperblack',d_x)
    text_sf = font.render(str(text_z),True,colors)
    return text_sf

# 声音开关按钮
def audio():
    if c.Audio_On:
        audio_off_on = c.Images['audio_off']
    else:
        audio_off_on = c.Images['audio_on']
    x,y = c.mouse_x_y
    if c.MouseButtonDown and 5<= x <=45 and 5<= y <=45:
        audio_icon = pygame.transform.scale(audio_off_on, (34,34))
        screen.blit(audio_icon,(8,8))
        c.Audio_On = c.audios_on_off()
    else:
        audio_icon = pygame.transform.scale(audio_off_on, (40,40))
        screen.blit(audio_icon,(5,5))

#开始按钮
def ready():
    but_play = pygame.image.load(c.img_path("but_play"))
    x,y = c.mouse_x_y
    if c.MouseButtonDown and 260< x <320 and 360< y <420 :
        but_play = pygame.transform.scale(but_play, (70,66))
        screen.blit(but_play,(260,355))
        c.Game_status = 'init_status'
        c.audio_play('click')
    else:
        but_play = pygame.transform.scale(but_play, (80,75))
        screen.blit(but_play,(255,350))
    screen.blit(draw_text(60,"BEGIN",(255,184,93)),(190,255))

# 背景和蒙版
def background():
    screen.blit(c.Images['bg_game'], (0, 0))
    screen.blit(c.Images['game_area'], (120, 200))
    mound()
def background_mask():
    image = pygame.Surface((600, 600)) #创建黑色背景
    # 蒙版可见度0最低，255最高
    image.set_alpha(180) #对黑色背景透视化处理
    screen.blit(image, (0, 0))
# 小土堆设置
def mound():
    # 坐标
    x_y_lists = [(152, 235), (256, 235), (362, 235),\
                 (152, 325), (256, 325), (362, 325),\
                 (152, 415), (256, 415), (362, 415)]
    for x_y in x_y_lists :
        screen.blit(c.Images['terrain_hole'], x_y)

# 锤子动画
def hammer_hit():
    if c.Super_Hammer == True:
        hammer = c.slice_hammer[1][c.hammer_picture]
    else:
        hammer = c.slice_hammer[0][c.hammer_picture]
    hammer = pygame.transform.scale(hammer, (86, 75))
# 检测鼠标坐标
    x, y = c.mouse_x_y
    if 140 <= x < 243 and 176 <= y < 264:
        screen.blit(hammer, (175, 120))
        if 0 < c.character_status[0][3] < 17:
            c.character_status[0][3] = 17
    elif 140 <= x < 243 and 264 <= y < 352:
        screen.blit(hammer, (175, 210))
        if 0 < c.character_status[1][3] < 17:
            c.character_status[1][3] = 17
    elif 140 <= x < 243 and 352 <= y < 440:
        screen.blit(hammer, (175, 300))
        if 0 < c.character_status[2][3] < 17:
            c.character_status[2][3] = 17
    elif 243 <= x < 364 and 176 <= y < 264:
        screen.blit(hammer, (280, 120))
        if 0 < c.character_status[3][3] < 17:
            c.character_status[3][3] = 17
    elif 243 <= x < 364 and 264 <= y < 352:
        screen.blit(hammer, (280, 210))
        if 0 < c.character_status[4][3] < 17:
            c.character_status[4][3] = 17
    elif 243 <= x < 364 and 352 <= y < 440:
        screen.blit(hammer, (280, 300))
        if 0 < c.character_status[5][3] < 17:
            c.character_status[5][3] = 17
    elif 364 <= x < 449 and 176 <= y < 264:
        screen.blit(hammer, (385, 120))
        if 0 < c.character_status[6][3] < 17:
            c.character_status[6][3] = 17
    elif 364 <= x < 449 and 264 <= y < 352:
        screen.blit(hammer, (385, 210))
        if 0 < c.character_status[7][3] < 17:
            c.character_status[7][3] = 17
    elif 364 <= x < 449 and 352 <= y < 440:
        screen.blit(hammer, (385, 300))
        if 0 < c.character_status[8][3] < 17:
            c.character_status[8][3] = 17

# 锤子动画，判断是否有鼠标点击操作或锤子是否已经开始动画
def Hammer():
    if c.MouseButtonDown or c.hammer_picture>=1 :
        hammer_hit()
        c.hammer_picture += 1
        if c.hammer_picture == 7:
            c.hammer_picture = 0

#地鼠和炸弹动画
def character(who,where,what):
    character = c.slice_character[who][what]
    character = pygame.transform.scale(character, (86, 75))
    # 地鼠坐标
    character_x_y = ((147, 180), (147, 270), (147, 360),\
                     (251, 180), (251, 270), (251, 360),\
                     (356, 180), (356, 270), (356, 360))
    screen.blit(character, character_x_y[where])
    mound()

def character_random():
    #每隔0.5s生成一只地鼠，并判断是否已经有地鼠，如果没有则随机生成一种颜色给地鼠
    if c.speed > 9:#PFS为18 所以为0.5s
        rand = random.randint(0, 8)
        if c.character_status[rand][0] == 0:
            c.character_status[rand][0] = 1
            c.character_status[rand][2] = random.randint(0, 4)
            c.speed = 0
    c.speed += 1

def character_dancing():
    #遍历所有洞口
    for character_status_list in c.character_status:
        bool_0_1 , where, who, what = character_status_list
        if bool_0_1:
            character(who,where,what)
            character_status_list[3] += 1
            if what == 16 or what == 29:
                character_status_list[0] = 0
                character_status_list[3] = 0
            elif what == 17:
                total_score(who)
    character_random()

# 倒计时
def click_time():
    times = 133 * c.game_time/(60 * c.FPS)
    screen.blit(c.Images['timebar_frame'], (145, 165))
    if times >= 1:
        timebar_1 = pygame.transform.scale(c.Images['timebar_1'], (int(times), 22))
        screen.blit(timebar_1, (152, 168))
        screen.blit(draw_text(20, int(c.game_time / c.FPS), (255, 184, 93)), (210, 165))
    screen.blit(c.Images['time_icon'], (145, 165))
# 分数显示 普通锤1倍超级锤2倍
def score():
    if c.Super_Hammer == True:
        hammer_audio = c.Images['super_hammer']
        x = 'x2'
    else:
        hammer_audio = c.Images['ordinary_hammer']
        x = 'x1'
    screen.blit(c.Images['score_panel'], (300, 165))
    screen.blit(hammer_audio, (295, 165))
    screen.blit(draw_text(20, c.Total_score, (255, 183, 90)), (365, 165))
    screen.blit(draw_text(10, x, (255, 183, 90)), (335, 175))

# 游戏结算
def settlement():
    #加载结算面板并修改尺寸
    msg_box = pygame.image.load(c.img_path("msg_box"))
    msg_box = pygame.transform.scale(msg_box, (300,220))

    screen.blit(msg_box,(150,195))
    screen.blit(draw_text(35,"TIME OVER",(255,181,87)),(195,250))
    screen.blit(draw_text(25,f"score: {c.Total_score}",(255,181,87)),(230,295))
    #加载返回主页并修改大小尺寸
    but_home = pygame.image.load(c.img_path("but_home"))
    but_home_big = pygame.transform.scale(but_home, (58,55))
    but_home_small = pygame.transform.scale(but_home, (50,47))
    #加载重新开始并修改大小尺寸
    but_restart = pygame.image.load(c.img_path("but_restart"))
    but_restart_big = pygame.transform.scale(but_restart, (58,55))
    but_restart_small = pygame.transform.scale(but_restart, (50,47))

    x,y = c.mouse_x_y
    if c.MouseButtonDown and 210< x <250 and 340< y <380:
        screen.blit(but_home_small,(204,339))
        c.Game_status = 'ready_status'
        c.audio_play('click')
    else:
        screen.blit(but_home_big,(200,335))
    if c.MouseButtonDown and 350< x <395 and 340< y <=380:
        screen.blit(but_restart_small,(349,337))
        c.Game_status = 'init_status'
        c.audio_play('click')
    else:
        screen.blit(but_restart_big,(345,333))
# 分数统计
def total_score(who):
    if c.Super_Hammer:
        times = 20
    else:
        times = 10
    if who == 4 :
        c.Total_score -= times*5
        c.audio_play('bomb')
    else :
        c.Total_score += (who+1)*times
        c.audio_play('hammer')
