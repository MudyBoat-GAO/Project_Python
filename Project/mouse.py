import pygame
from pygame.sprite import Sprite

class Mouse(Sprite):

    """单个 Mouse"""
    def __init__(self,ai_settings,screen):
        """初始化"""
        super(Mouse,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载图像 获取rect
        self.image = pygame.image.load("Sources/mouse.jpg")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return  True
        elif self.rect.left <= 0:
            return True

    def blitme(self):

        self.screen.blit(self.image,self.rect)
    def update(self):
        self.x += (self.ai_settings.mouse_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x

