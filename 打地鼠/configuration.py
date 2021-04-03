import pygame
import os 

#声音开关 默认关闭，若默认打开则取消 下面pygame.mixer.music.play(-1)注释
Audio_Off =  False
#锤子颜色
Super_Hammer = False
#鼠标坐标
mouse_x_y = (800,800)
#锤子状态
Mouse_ture = False
#鼠标状态
MouseButtonDown = False
#游戏状态
Game_status = 0
#锤子动画
hammer_picture = 0
#fps
FPS = 18
#游戏时长
game_time = 60*FPS
#地鼠计数器
character_quantity = 0
#地鼠状态[有没有0-2,位置0-9,颜色0-4,动作0-30]
character_status = [[0,0,0,0],[0,1,0,0],[0,2,0,0],[0,3,0,0],[0,4,0,0],[0,5,0,0],[0,6,0,0],[0,7,0,0],[0,8,0,0]]
#出场速度
speed = 20
#总成绩
Total_score = 0
#图形切片
slice_character = [[],[],[],[],[]]
slice_hammer = [[],[]]
Images = {}


def img_path(file_name):
    for pic in os.listdir(os.path.join(os.getcwd(),"images")):
        name, ext = os.path.splitext(pic)
        if name == file_name:
            return os.path.join(os.getcwd(),f"images\{name+ext}")#暂时先这样
    print("文件名错误")

def audio_path(file_name):
    for pic in os.listdir(os.path.join(os.getcwd(),"audios")):
        name, ext = os.path.splitext(pic)
        if name == file_name:
            return os.path.join(os.getcwd(),f"audios\{name+ext}")
    print("文件名错误")
  
#加载图片
def load_from_sheet():
    #炸弹鼠
    for coordinate in character_list():

        slice_character[0].append(slice_img(img_path("character_0"),coordinate))
        slice_character[1].append(slice_img(img_path("character_1"),coordinate))
        slice_character[2].append(slice_img(img_path("character_2"),coordinate))
        slice_character[3].append(slice_img(img_path("character_3"),coordinate))
        slice_character[4].append(slice_img(img_path("character_4"),coordinate))
    #锤子
    for coordinate in hammer_list(i=0):
        slice_hammer[0].append(slice_img(img_path("hammer"),coordinate))
    for coordinate in hammer_list(i=1):
        slice_hammer[1].append(slice_img(img_path("hammer"),coordinate))
    #背景
    bg_game = pygame.image.load(img_path("bg_game"))
    Images['bg_game'] = pygame.transform.scale(bg_game, (600,600))

    #土地&土堆
    game_area = pygame.image.load(img_path("game_area"))
    Images['game_area'] = pygame.transform.scale(game_area, (360,280))

    terrain_hole = pygame.image.load(img_path("terrain_hole"))
    Images['terrain_hole'] = pygame.transform.scale(terrain_hole, (75,45))
    #时间
    timebar_frame = pygame.image.load(img_path("timebar_frame"))
    Images['timebar_frame'] = pygame.transform.scale(timebar_frame, (150,30))

    Images['timebar_1'] = pygame.image.load(img_path("timebar_1"))
    
    time_icon = pygame.image.load(img_path("time_icon"))
    Images['time_icon'] = pygame.transform.scale(time_icon, (30,30))
    #普通锤
    Images['ordinary_hammer'] = slice_img(img_path("hammer_icon"),(0,0,58,69))
    #超级锤
    Images['super_hammer'] = slice_img(img_path("hammer_icon"),(58,0,58,69))

    score_panel = pygame.image.load(img_path("score_panel"))
    Images['score_panel'] = pygame.transform.scale(score_panel, (148,30))
    #声音开关
    Images['audio_off'] = slice_img(img_path("audio_icon"),(0,0,118,112))
    Images['audio_on'] = slice_img(img_path("audio_icon"),(118,0,118,112))
    


#图片裁剪函数(需要裁剪的图片,开始坐标及尺寸)
def slice_img(img_name,x_y_width_height):
    screen = pygame.display.set_mode((600,600))
    image = pygame.Surface((x_y_width_height[2], x_y_width_height[3])).convert()
    big_image = pygame.image.load(img_name)
    image.get_rect()
    image.blit(big_image,(0,0),x_y_width_height)
    image.set_colorkey((  0,   0,   0))

    return image
#炸弹鼠图片裁剪坐标
def character_list():
	x = 218
	y = 192
	lists = []
	for i in range(5):
		for j in range(6):
			lists += [(j*x,i*y,x,y)]
	return lists
#锤子图片裁剪坐标
def hammer_list(i):
	x = 258
	y = 225
	lists = []
	for j in range(7):
			lists += [(j*x,i*y,x,y)]
	return lists

#初始化图形切片
load_from_sheet()

#加载声音
pygame.mixer.init()
pygame.mixer.music.load(audio_path("soundtrack"))
#pygame.mixer.music.play(-1)
def audios_on():
    if Audio_Off:
        pygame.mixer.music.stop()
        return False
    else:
        pygame.mixer.music.play(-1)
        return True

audios = {
        'bomb': pygame.mixer.Sound(audio_path("bomb")),
        'click': pygame.mixer.Sound(audio_path("click")),
        'game_over': pygame.mixer.Sound(audio_path("game_over")),
        'hammer': pygame.mixer.Sound(audio_path("hammer")),
        'superhammer': pygame.mixer.Sound(audio_path("superhammer"))
    }