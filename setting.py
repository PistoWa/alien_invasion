class Setting():
    '''store settings'''

    def __init__(self):
        #screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #about ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #about bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #about alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        #fleed direction 1 right and -1 left
        self.fleet_direction = 1
