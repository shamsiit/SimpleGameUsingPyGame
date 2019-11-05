from game_utility import ScreenInitializer

class GameFlow:

    screen = None
    background = None
    bullet = None
    one = None
    two = None
    three = None
    ship = None
    clock = None
    pygame_instance = None

    def __init__(self, pygame_instance):
        """Constructor which initializes the requirements for the game logic."""

        self.pygame_instance = pygame_instance
        self.screen = pygame_instance.display.set_mode(ScreenInitializer.screen_size)
        self.background = pygame_instance.image.load(ScreenInitializer.background_path)
        self.bullet = pygame_instance.image.load(ScreenInitializer.bullet_path)
        self.one = pygame_instance.image.load(ScreenInitializer.one_path)
        self.two = pygame_instance.image.load(ScreenInitializer.two_path)
        self.three = pygame_instance.image.load(ScreenInitializer.three_path)
        self.ship = pygame_instance.image.load(ScreenInitializer.ship_path)
        self.clock = pygame_instance.time.Clock()

    def run_game_logic(self):
        """Run the game logic."""
        
        while ScreenInitializer.keep_alive == True:
            for event in self.pygame_instance.event.get():
                keys = self.pygame_instance.key.get_pressed()
                if keys[self.pygame_instance.K_q] == True:
                    print("q for quit!")
                    ScreenInitializer.keep_alive = False
                if keys[self.pygame_instance.K_SPACE] == True:
                    ScreenInitializer.Fired = True
                
            px = self.pygame_instance.image.load(ScreenInitializer.planet[ScreenInitializer.index])
            self.screen.blit(self.background, [0,0])
            self.screen.blit(self.bullet, [180, ScreenInitializer.bullet_y])
            self.screen.blit(self.ship, [160, 500])
            self.screen.blit( px, [ScreenInitializer.planet_x, 50])
            
                

            if ScreenInitializer.move_direction == 'right':
                ScreenInitializer.planet_x = ScreenInitializer.planet_x + 3
                if ScreenInitializer.planet_x >= 300:
                    ScreenInitializer.move_direction = 'left'
            else:
                ScreenInitializer.planet_x = ScreenInitializer.planet_x - 3
                if ScreenInitializer.planet_x <= 0:
                    ScreenInitializer.move_direction = 'right'
            if ScreenInitializer.Fired == True:
                ScreenInitializer.bullet_y = ScreenInitializer.bullet_y - 5
                if ScreenInitializer.bullet_y == 50:
                    ScreenInitializer.Fired = False
                    ScreenInitializer.bullet_y = 500
            if ScreenInitializer.bullet_y < 80 and ScreenInitializer.planet_x >120 and ScreenInitializer.planet_x <180:
                ScreenInitializer.index += 1
                ScreenInitializer.planet_x += 10
                ScreenInitializer.bullet_y = 500
                ScreenInitializer.Fired = False
                print("BOOM")
                if ScreenInitializer.index == 3 :
                    print("Winner")
                    break
            ScreenInitializer.cycles += 1
            self.pygame_instance.display.update()
            self.clock.tick(60)