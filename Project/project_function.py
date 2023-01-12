import sys
from time import sleep

import pygame
from bullet import Bullet
from mouse import Mouse
def fire_bullet(ai_settings,screen,cat,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, cat)
        bullets.add(new_bullet)
def check_keydown_events(event,ai_settings,screen,cat,bullets):
    if event.key == pygame.K_RIGHT:
        cat.moving_right = True
    elif event.key == pygame.K_LEFT:
        cat.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, cat, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event,cat):
    if event.key == pygame.K_RIGHT:
        cat.moving_right = False
    elif event.key == pygame.K_LEFT:
        cat.moving_left = False

def get_number_rows(ai_settings,cat_height,mouse_height):
    available_space_y = (ai_settings.screen_height-(3*mouse_height)-cat_height)
    number_rows = int(available_space_y/(2*mouse_height))
    return  number_rows

def get_number_mouse_x(ai_settings,mouse_width):
    availiable_space_x = ai_settings.screen_width - 2 * mouse_width
    number_mouse_x = int(availiable_space_x / (2 * mouse_width))
    return number_mouse_x
def create_mouse(ai_settings,screen,Mice,mouse_number,row_number):
    mouse = Mouse(ai_settings, screen)
    mouse_width = mouse.rect.width
    mouse.x = mouse_width + 2 * mouse_width * mouse_number
    mouse.rect.x = mouse.x
    mouse.rect.y = mouse.rect.height + 2*mouse.rect.height*row_number
    Mice.add(mouse)

def create_fleet(ai_settings,screen,cat,Mice):
    """创建 mouse 群"""
    mouse = Mouse(ai_settings,screen)
    number_mouse_x = get_number_mouse_x(ai_settings,mouse.rect.width)
    number_rows =get_number_rows(ai_settings,cat.rect.height,mouse.rect.height)

    for row_number in range(number_rows):
        for mouse_number in range(number_mouse_x):
          create_mouse(ai_settings,screen,Mice,mouse_number,row_number)


def check_events(ai_settings,screen,stats,play_button,cat,Mice,bullets):
    """响应按键 和 鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,cat,bullets)
        elif event.type == pygame.KEYUP:
           check_keyup_events(event,cat)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,cat,Mice,bullets,mouse_x,mouse_y)
def check_play_button(ai_settings,screen,stats,play_button,cat,Mice,bullets,mouse_x,mouse_y):

    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        Mice.empty()
        bullets.empty()

        create_fleet(ai_settings,screen,cat,Mice)
        cat.center_cat()

def update_bullet(ai_settings,screen,cat,bullets,Mice):
    bullets.update()
    # 删除已经消失的bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    collisions = pygame.sprite.groupcollide(bullets,Mice,True,True)

    if len(Mice) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen,cat,Mice)
def update_screen(ai_settings, screen,stats, cat,Mice,bullets,play_button):
    """更新窗口图像"""
    #重绘屏幕
    screen.fill(ai_settings.bg_color)
    cat.blitme()
    #
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    Mice.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    #最近屏幕可见
    pygame.display.flip()
def check_Mice_bottom(ai_settings,stats,screen,cat,Mice,bullets):
    screen_rect = screen.get_rect()
    for mouse in Mice.sprites():
        if mouse.rect.bottom >= screen_rect.bottom:
            cat_die(ai_settings,stats,screen,cat,Mice,bullets)
            break

def check_fleet_edges(ai_settings,Mice):
    for mouse in Mice.sprites():
        if mouse.check_edges():
            change_fleet_direction(ai_settings,Mice)
            break
def change_fleet_direction(ai_settings, Mice):
    for mouse in Mice.sprites():
        mouse.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
def cat_die(ai_settings,stats,screen,cat,Mice,bullets):
   if stats.cat_left>0:
       stats.cat_left -= 1;

       Mice.empty()
       bullets.empty()

       create_fleet(ai_settings,screen,cat,Mice)
       cat.center_cat()

       sleep(0.5)
   else:
       stats.game_active = False
       pygame.mouse.set_visible(True)
def update_Mice(ai_settings,stats,screen,cat,Mice,bullets):
    check_fleet_edges(ai_settings,Mice)
    Mice.update()

    if pygame.sprite.spritecollideany(cat,Mice):
        cat_die(ai_settings,stats,screen,cat,Mice,bullets)
        #print("cat died")
    check_Mice_bottom(ai_settings,stats,screen,cat,Mice,bullets)

