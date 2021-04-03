import pygame
import os
import random
import configuration as c 
import module
import time
IMGS = None
BLACK = (0,0,0)

#对象模型


class interface():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("打地鼠")
        self.screen = pygame.display.set_mode((600,600))
        self.running = True
        self.clock = pygame.time.Clock()
        self.caption = "打地鼠"
        self.fps = c.FPS

    #准备界面
    def ready(self):
        module.background()
        module.play_game()
        module.background_mask()
        module.ready()
    #初始化游戏
    def game_init(self):
        c.game_time = 60*self.fps
        c.character_status = [[0,0,0,0],[0,1,0,0],[0,2,0,0],[0,3,0,0],[0,4,0,0],[0,5,0,0],[0,6,0,0],[0,7,0,0],[0,8,0,0]]
        c.Total_score = 0
        c.Game_status = 2

    def start(self):
        module.background()
        module.click_time()
        module.score()
        module.play_game(True)
        if c.game_time >= 0:
            if c.game_time/c.FPS < 20:
                if not c.Super_Hammer and c.Audio_Off:
                    c.audios['superhammer'].play()
                c.Super_Hammer = True
        else:
            c.Super_Hammer = False
            c.game_time = 0
            if c.Audio_Off:
                c.audios['game_over'].play()
            c.Game_status = 3
        c.game_time -= 1

    def end(self):
        module.background()
        module.click_time()
        module.score()
        module.background_mask()
        module.settlement()

        
    def main(self):

        while self.running:
            c.MouseButtonDown = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    c.MouseButtonDown = True
                    c.Mouse_ture = True
                    c.mouse_x_y = event.pos

            if c.Game_status == 0:
                self.ready()
            elif c.Game_status == 1:
                self.game_init()
            elif c.Game_status ==2:
                self.start()
            elif c.Game_status == 3:
                self.end()
            module.audio()

            pygame.display.update()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    interface().main()
    pygame.quit()


