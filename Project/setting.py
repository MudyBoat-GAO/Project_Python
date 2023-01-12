
class settings():
    """存储 游戏中 的设置"""

    def __init__(self):
        """游戏初始化设置"""
        # 窗口设置：
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)
        #子弹相关设置:
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 60,60,60
        self.bullet_allowed = 20
        # Cat 相关设置
        self.cat_limit=3
        #Mouse 相关设置
        self.fleet_drop_speed = 10
        #
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""

        self.cat_speed_factor = 1
        self.bullet_speed_factor = 3
        self.mouse_speed_factor = 1
    # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        self.cat_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.mouse_speed_factor*=self.speedup_scale