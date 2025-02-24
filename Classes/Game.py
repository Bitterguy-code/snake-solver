import pygame
import time
import random

class Game():
    black = pygame.Color(0,0,0)
    white = pygame.Color(255,255,255)
    red = pygame.Color(255,0,0)
    green = pygame.Color(0,255,0)
    blue = pygame.Color(0,0,255)


    def __init__(self, window_x, window_y, snake_speed):
        self._window_x = window_x
        self._window_y = window_y
        self._snake_speed = snake_speed
        self._snake_body = [[]]
        self._fruit_position = []
        self._fruit_spawn = False 

    @property
    def window_x(self):
        return self._window_x
    
    @property
    def window_y(self):
        return self._window_y

    @property
    def snake_body(self):
        return self._snake_body

    @property
    def fruit_position(self):
        return self._fruit_position

    @fruit_position.setter
    def fruit_position(self, last_fruit):
        self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10, random.randrange(1, (self.window_y//10)) * 10]

        while self.fruit_position in self.snake_body or self.fruit_position == last_fruit:
            self.fruit_position = [random.randrange(1, (self.window_x//10)) * 10, random.randrange(1, (self.window_y//10)) * 10]

    @property
    def fruit_spawn(self):
        return self._fruit_spawn

    def start_display(self):
        pygame.init()
        pygame.display.set_caption('Snake: The Movie: The Game')
        game_window = pygame.display.set_mode((self.window_x,self.windoy_y))
        fps = pygame.time.Clock()

    @classmethod
    def start_game(cls):
        #default position of the snake being set to the middle of the window
        snake_position = [cls.windoy_y/2,cls.window_x/2]

        cls.snake_body = [
            [snake_position[0],snake_position[1]],
            [snake_position[0]-10, snake_position[1]],
            [snake_position[0]-20, snake_position[1]],
            [snake_position[0]-30, snake_position[1]]
        ]

        

    
