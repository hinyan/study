import pygame
import os 
'''游戏设置'''
# 声音开关
Audio_On = False
# 游戏状态
Game_status = 'ready_status'
# 游戏时长
FPS = 18
game_time = 60*FPS

'''属性设置'''
# 图形切片
slice_character = [[],[],[],[],[]]
slice_hammer = [[],[]]
Images = {}
# 锤子颜色，动画
Super_Hammer = False
hammer_picture = 0
# 鼠标坐标，状态
mouse_x_y = (800,800)
MouseButtonDown = False
# 地鼠状态[有没有0-1,位置0-8,颜色0-4,动作0-29]
character_status = [[0,0,0,0],[0,1,0,0],[0,2,0,0],\
                    [0,3,0,0],[0,4,0,0],[0,5,0,0],\
                    [0,6,0,0],[0,7,0,0],[0,8,0,0]]
# 出现速度
speed = 0
# 总成绩
Total_score = 0

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


'''加载图片'''
def load_from_sheet():
    # 炸弹 地鼠
    for coordinate in character_list():
        slice_character[0].append(slice_img(img_path("character_0"),coordinate))
        slice_character[1].append(slice_img(img_path("character_1"),coordinate))
        slice_character[2].append(slice_img(img_path("character_2"),coordinate))
        slice_character[3].append(slice_img(img_path("character_3"),coordinate))
        slice_character[4].append(slice_img(img_path("character_4"),coordinate))
    # 锤子
    for coordinate in hammer_list(i=0):
        slice_hammer[0].append(slice_img(img_path("hammer"),coordinate))
    for coordinate in hammer_list(i=1):
        slice_hammer[1].append(slice_img(img_path("hammer"),coordinate))

    # 加载背景图并修改尺寸
    bg_game = pygame.image.load(img_path("bg_game"))
    Images['bg_game'] = pygame.transform.scale(bg_game, (600, 600))
    # 声音开关
    Images['audio_off'] = slice_img(img_path("audio_icon"), (0, 0, 118, 112))
    Images['audio_on'] = slice_img(img_path("audio_icon"), (118, 0, 118, 112))
    # 加载土地&土堆并修改尺寸
    game_area = pygame.image.load(img_path("game_area"))
    Images['game_area'] = pygame.transform.scale(game_area, (360, 280))
    terrain_hole = pygame.image.load(img_path("terrain_hole"))
    Images['terrain_hole'] = pygame.transform.scale(terrain_hole, (75, 45))
    # 加载时间模块图及修改尺寸
    timebar_frame = pygame.image.load(img_path("timebar_frame"))
    Images['timebar_frame'] = pygame.transform.scale(timebar_frame, (150, 30))
    Images['timebar_1'] = pygame.image.load(img_path("timebar_1"))
    time_icon = pygame.image.load(img_path("time_icon"))
    Images['time_icon'] = pygame.transform.scale(time_icon, (30, 30))
    # 加载计分区域图并修改尺寸
    # 普通锤
    ordinary_hammer = slice_img(img_path("hammer_icon"), (0, 0, 58, 69))
    Images['ordinary_hammer'] = pygame.transform.scale(ordinary_hammer, (35, 35))
    # 超级锤
    super_hammer = slice_img(img_path("hammer_icon"), (58, 0, 58, 69))
    Images['super_hammer'] = pygame.transform.scale(super_hammer, (35, 35))
    # 计分框
    score_panel = pygame.image.load(img_path("score_panel"))
    Images['score_panel'] = pygame.transform.scale(score_panel, (148, 30))


# 图片裁剪函数(需要裁剪的图片,开始坐标及尺寸)
def slice_img(img_name,x_y_width_height):
    image = pygame.Surface((x_y_width_height[2], x_y_width_height[3])) #创建Surface图像
    big_image = pygame.image.load(img_name)
    image.blit(big_image,(0,0),x_y_width_height)
    image.set_colorkey((0,0,0)) #去掉背景颜色
    return image
# 炸弹和地鼠图片裁剪坐标
def character_list():
	x, y= 218, 192
	lists = []
	for i in range(5):
		for j in range(6):
			lists += [(j*x,i*y,x,y)]
	return lists
# 锤子图片裁剪坐标
def hammer_list(i):
	x, y = 258, 225
	lists = []
	for j in range(7):
			lists += [(j*x,i*y,x,y)]
	return lists

# 加载声音
pygame.mixer.init()
pygame.mixer.music.load(audio_path("soundtrack"))

def audios_on_off():
    #判断如果开关是打开的，那么把开关关闭，否则相反
    if Audio_On:
        pygame.mixer.music.stop()
        return False
    else:
        pygame.mixer.music.play(-1)
        return True
#加载音效
audios = {
        'bomb': pygame.mixer.Sound(audio_path("bomb")),
        'click': pygame.mixer.Sound(audio_path("click")),
        'game_over': pygame.mixer.Sound(audio_path("game_over")),
        'hammer': pygame.mixer.Sound(audio_path("hammer")),
        'superhammer': pygame.mixer.Sound(audio_path("superhammer"))
    }

# 播放音效 调用传入文件名
def audio_play(name):
    if Audio_On:
        audios[name].play()
