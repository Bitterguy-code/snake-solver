import pygame
import time
import random

class Game():
    def __init__(self, window_x, window_y, snake_speed):
        self._window_x = window_x
        self._window_y = window_y
        self._snake_speed = snake_speed
