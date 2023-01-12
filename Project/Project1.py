#科学数据包：
import sys
import pygame
from pygame.sprite import Group
from setting import settings
from game_stats import GameStats
from cat import Cat
from mouse import Mouse
import project_function as pf
from button import Button

def run_game():
    # 初始化
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Cats Vs Mice")
    #
    play_button = Button(ai_settings,screen,"play")
    #
    stats = GameStats(ai_settings)
    #创建 一只 Cat
    cat = Cat(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一mouse编组
    Mice = Group()

    # 创建一个Mouse：
    """mouse = Mouse(ai_settings,screen)"""

    #创建一个 mouse 群
    pf.create_fleet(ai_settings,screen,cat,Mice)
    while True:
        #
        pf.check_events(ai_settings,screen,stats,play_button,cat,Mice,bullets)
        if stats.game_active:
            cat.update()
            pf.update_bullet(ai_settings,screen,cat,bullets,Mice)
            pf.update_Mice(ai_settings,stats,screen,cat,Mice,bullets)
        pf.update_screen(ai_settings,screen,stats,cat,Mice,bullets,play_button)




#运行区
run_game()