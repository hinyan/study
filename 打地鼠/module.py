import pygame
import random
import configuration as c 
screen = pygame.display.set_mode((600,600))
#开始按钮
def ready():
    but_play = pygame.image.load(c.img_path("but_play"))
    x,y = c.mouse_x_y
    if c.MouseButtonDown and 260< x <320 and 360< y <420 :
        but_play = pygame.transform.scale(but_play, (70,66))
        screen.blit(but_play,(260,355))
        c.Game_status = 1
        c.Mouse_ture = False
        if c.Audio_Off:
            c.audios['click'].play()            
    else:
        but_play = pygame.transform.scale(but_play, (80,75))
        screen.blit(but_play,(255,350))
    screen.blit(draw_text(60,"BEGIN",(255,184,93)),(190,240))
#游戏结算
def settlement():

    msg_box = pygame.image.load(c.img_path("msg_box"))
    msg_box = pygame.transform.scale(msg_box, (300,220))
    
    but_home = pygame.image.load(c.img_path("but_home"))
    but_home_b = pygame.transform.scale(but_home, (58,55))
    but_home_s = pygame.transform.scale(but_home, (50,47))
    
    but_restart = pygame.image.load(c.img_path("but_restart"))
    but_restart_b = pygame.transform.scale(but_restart, (58,55))
    but_restart_s = pygame.transform.scale(but_restart, (50,47))
    
    screen.blit(msg_box,(150,195))
    screen.blit(draw_text(35,"TIME OVER",(255,181,87)),(190,240))
    screen.blit(draw_text(25,f"score: {c.Total_score}",(255,181,87)),(230,290))
    x,y = c.mouse_x_y
    if c.MouseButtonDown and 210< x <250 and 340< y <380:
        screen.blit(but_home_s,(204,339))
        c.Game_status = 0
        c.Mouse_ture = False
        if c.Audio_Off:
            c.audios['click'].play()
    else:
        screen.blit(but_home_b,(200,335))
    if c.MouseButtonDown and 350< x <395 and 340< y <=380:
        screen.blit(but_restart_s,(349,337))
        c.Game_status = 1
        c.Mouse_ture = False
        if c.Audio_Off:
            c.audios['click'].play()
    else:
        screen.blit(but_restart_b,(345,333))

    
    

#声音开关按钮
def audio():
    if c.Audio_Off:
        audio_off_on = c.Images['audio_off']
    else:
        audio_off_on = c.Images['audio_on']
    x,y = c.mouse_x_y
    if c.MouseButtonDown and 5<= x <=45 and 5<= y <=45:
        audio = pygame.transform.scale(audio_off_on, (34,34))
        screen.blit(audio,(8,8))
        c.Audio_Off = c.audios_on()
    else:
        audio = pygame.transform.scale(audio_off_on, (40,40))
        screen.blit(audio,(5,5))
        
    
#游戏界面
def background():
    
    screen.blit(c.Images['bg_game'],(0,0))
    screen.blit(c.Images['game_area'],(120,200))
    mound()

def background_mask():
    image = pygame.Surface((400,400))
    big_image = pygame.image.load(c.img_path('msg_box'))
    image.blit(big_image,(0,0),(200,200,400,400))
    image.get_rect()
    #蒙版可见度0最低，255最高
    image.set_alpha(120)
    image = pygame.transform.scale(image, (600,600))
    screen.blit(image,(0,0))

#小土堆
def mound():

    terrain_hole = c.Images['terrain_hole']
    #坐标
    screen.blit(terrain_hole,(152,235))
    screen.blit(terrain_hole,(256,235))
    screen.blit(terrain_hole,(362,235))
    screen.blit(terrain_hole,(152,325))
    screen.blit(terrain_hole,(256,325))
    screen.blit(terrain_hole,(362,325))
    screen.blit(terrain_hole,(152,415))
    screen.blit(terrain_hole,(256,415))
    screen.blit(terrain_hole,(362,415))
#分数统计
def total_score(listss):
    if c.Super_Hammer:
        num = 20
    else:
        num = 10
    if listss == 4:
        c.Total_score -= num
        if c.Audio_Off :
            c.audios['bomb'].play()
    else:
        c.Total_score += num
        if c.Audio_Off :
            c.audios['hammer'].play()

#锤子动画
def hammer_hit():
    if c.Super_Hammer == True :
        color = 1
    else:
        color = 0
    hammer = c.slice_hammer[color][c.hammer_picture]
    hammer = pygame.transform.scale(hammer, (86,75))
    #检测鼠标坐标
    x, y = c.mouse_x_y
    if 140<= x <243 and 176<= y <264 :
        screen.blit(hammer,(175,120))
        if c.character_status[0][0] == 1 :
            c.character_status[0][0] = 2

    elif 140<= x <243 and 264<= y <352 :
        screen.blit(hammer,(175,210))
        if c.character_status[1][0] == 1 :
            c.character_status[1][0] = 2

    elif 140<= x <243 and 352<= y <440 :
        screen.blit(hammer,(175,300))
        if c.character_status[2][0] == 1 :
            c.character_status[2][0] = 2

    elif 243<= x <364 and 176<= y <264 :
        screen.blit(hammer,(280,120))
        if c.character_status[3][0] == 1 :
            c.character_status[3][0] = 2

    elif 243<= x <364 and 264<= y <352 :
        screen.blit(hammer,(280,210))
        if c.character_status[4][0] == 1 :
            c.character_status[4][0] = 2

    elif 243<= x <364 and 352<= y <440 :
        screen.blit(hammer,(280,300))
        if c.character_status[5][0] == 1 :
            c.character_status[5][0] = 2

    elif 364<= x <449 and 176<= y <264 :
        screen.blit(hammer,(385,120))
        if c.character_status[6][0] == 1 :
            c.character_status[6][0] = 2

    elif 364<= x <449 and 264<= y <352 :
        screen.blit(hammer,(385,210))
        if c.character_status[7][0] == 1 :
            c.character_status[7][0] = 2

    elif 364<= x <449 and 352<= y <440 :
        screen.blit(hammer,(385,300))
        if c.character_status[8][0] == 1 :
            c.character_status[8][0] = 2

#鼠炸弹动画
def character(character_status_list):

    character = c.slice_character[character_status_list[2]][character_status_list[3]]
    character = pygame.transform.scale(character, (86,75))
    #地鼠坐标
    character_x_y = ((147,180),(147,270),(147,360),(251,180),(251,270),(251,360),(356,180),(356,270),(356,360))
    screen.blit(character,character_x_y[character_status_list[1]])
    mound()

#倒计时
def click_time():
    times = c.game_time/60*133/c.FPS
    screen.blit(c.Images['timebar_frame'],(145,165))
    if times >= 1:
        timebar_1 = pygame.transform.scale(c.Images['timebar_1'], (int(times),22))
        screen.blit(timebar_1,(152,168))
        screen.blit(draw_text(20,int(c.game_time/c.FPS),(255,184,93)),(210,160))
    screen.blit(c.Images['time_icon'],(145,165))
#分数显示 普通锤1倍超级锤2倍
def score():
    if c.Super_Hammer == True:
        hammer = c.Images['super_hammer']
        x = 'x2'
    else:
        hammer = c.Images['ordinary_hammer']
        x = 'x1'   
    screen.blit(c.Images['score_panel'],(300,165))
    hammer_audio = pygame.transform.scale(hammer, (35,35))
    screen.blit(hammer_audio,(295,165))
    screen.blit(draw_text(20,c.Total_score,(255,183,90)),(365,162))
    screen.blit(draw_text(10,x,(255,183,90)),(335,175))
#生成文字函数(大小，内容，颜色)
def draw_text(d_x,text_z,colors):
    pygame.font.init()
    font  =  pygame.font.SysFont('hgdycnki',d_x)

    text_sf  =  font.render(str(text_z),True,colors)
    return text_sf
'''
炸弹鼠运动函数
设置一个4*9的列表计算当前炸弹鼠状态
c.character_status[0-8][0-2]:0为无任何炸弹鼠,1为有炸弹鼠,2炸弹鼠被击中
c.character_status[0-8][0-8]：炸弹鼠坑位1-9
c.character_status[0-8][0-4]：炸弹鼠五种颜色，4为炸弹
c.character_status[0-8][0-29]：炸弹鼠动画1-17,被打中动画18-29,记录循环次数每次加1.
'''
def play_game(Game_status = False):
    for character_status_list in c.character_status:
        if character_status_list[0] == 0:
            c.character_quantity += 1
        elif character_status_list[0] == 1:
            character(character_status_list)
            character_status_list[3] += 1
            if character_status_list[3] == 17:
                character_status_list[0] = 0
                character_status_list[3] = -1
                c.character_quantity = 0

        elif character_status_list[0] == 2 and Game_status:
            if character_status_list[3]<=17:
                character_status_list[3] = 17
                #分数计算
                total_score(character_status_list[2])

            elif character_status_list[3] == 29:
                character_status_list[0] = 0
                character_status_list[3] = -1
                c.character_quantity = 0
            character(character_status_list)
            character_status_list[3] += 1
        #生成两个随机数，一个为位置，一个为炸弹鼠颜色，若位置上没有鼠即c.character_status[rand][0]为0 生成鼠
        if c.character_quantity > 8 and c.speed>100:
            rand = random.randint(0,8)
            if c.character_status[rand][0] == 0:
                c.character_status[rand][0] = 1
                c.character_status[rand][2] = random.randint(0,4)
                c.speed = 0
        c.speed += 1
    #锤子动画，判断是否有鼠标点击操作and游戏是否开始

    if c.Mouse_ture and Game_status:
        hammer_hit()
        c.hammer_picture += 1
        if c.hammer_picture == 7:
            c.Mouse_ture = False
            c.hammer_picture = 0
    
