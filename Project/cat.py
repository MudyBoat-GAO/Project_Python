import pygame

class Cat():
    """Cat 主体 的相关设置"""

    def __init__(self,ai_settings,screen):
        """初始化"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载 Cat主体图像 及 外接矩形
        self.image = pygame.image.load('Sources/Cat.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #初始于底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #centerx
        self.centerx = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False
    def center_cat(self):
        self.center = self.screen_rect.centerx
    def update(self):
        """根据移动标志调整Cat位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.ai_settings.cat_speed_factor
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.cat_speed_factor

    def blitme(self):
        """指定位置绘制 Cat主体"""
        self.screen.blit(self.image, self.rect)

