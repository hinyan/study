import pygame
import os
import configuration as c 
import module

#对象模型
class interface():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("打地鼠")
        self.screen = pygame.display.set_mode((600,600))
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = c.FPS
        # 初始化图形切片
        c.load_from_sheet()

    #准备界面
    def ready_status(self):
        module.background() #背景
        module.character_dancing() #跳舞的地鼠
        module.background_mask() #蒙版
        module.ready() #准备按钮
        module.audio() #声音
        
    #初始化游戏
    def init_status(self):
        c.Super_Hammer = False
        #时间设置
        c.game_time = 60*self.fps
        #地鼠状态
        c.character_status = [[0,0,0,0],[0,1,0,0],[0,2,0,0],\
                              [0,3,0,0],[0,4,0,0],[0,5,0,0],\
                              [0,6,0,0],[0,7,0,0],[0,8,0,0]]
        c.Total_score = 0 #分数归零
        c.Game_status = 'run_status'

    def run_status(self):
        module.background() #背景
        module.click_time() #时间模块
        module.score() #分数模块
        module.character_dancing() #跳舞的地鼠
        module.Hammer() #锤子击打模块
        module.audio() #声音
        if 0 <= c.game_time/c.FPS <= 20:
            if not c.Super_Hammer :
                c.audio_play('superhammer')

            c.Super_Hammer = True
        elif c.game_time < 0 :
            c.audio_play('game_over')
            c.Game_status = 'over_status'
        c.game_time -= 1

    def over_status(self):
        module.background() #背景
        module.click_time() #时间模块
        module.score() #分数模块
        module.background_mask() #蒙版
        module.settlement() #结算模块
        module.audio()#声音
        
    def main(self):
        while self.running:
            c.MouseButtonDown = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    c.MouseButtonDown = True
                    c.mouse_x_y = event.pos
            if c.Game_status == 'ready_status' :
                self.ready_status()
            elif c.Game_status == 'init_status' :
                self.init_status()
            elif c.Game_status == 'run_status' :
                self.run_status()
            elif c.Game_status == 'over_status' :
                self.over_status()
            pygame.display.update() 
            self.clock.tick(self.fps) #画面刷新速度

if __name__ == "__main__":
    interface().main()
    pygame.quit()


