
class GameStats():
    """跟踪游戏信息"""
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.cat_left = self.ai_settings.cat_limit
