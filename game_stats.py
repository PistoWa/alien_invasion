class GameStats():
    '''follow the maths'''

    def __init__(self, ai_setting):
        #initions
        self.ai_setting = ai_setting
        self.reset_stats(ai_setting)
        self.game_active = False

    def reset_stats(self, ai_setting):
    	self.ships_left = self.ai_setting.ship_limit