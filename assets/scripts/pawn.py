# Import pygame library
import pygame
from pygame.locals import *

class Rectangle(pygame.sprite.Sprite):
    def __init__(self):
        super(Rectangle, self).__init__()

        self.length = 25
        self.height = 25

        self.surf = pygame.Surface((self.length, self.height))
         
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()

        self.coordinates = (0, 0)

        self.playerspeed = 0.1

    def moveByKeysDown(self):
        direction = ()
        for key in pygame.key.get_pressed():
            if key == 'w':
                direction = (0, self.playerspeed)
        self.coordinates += direction
    def moveByKeysDown(self, window_width, window_height):
        keys = pygame.key.get_pressed()
        x, y = self.coordinates

        if keys[K_LEFT] and x - self.playerspeed >= 0:
            x -= self.playerspeed
        if keys[K_RIGHT] and x + self.playerspeed + self.length <= window_width:
            x += self.playerspeed
        if keys[K_UP] and y - self.playerspeed >= 0:
            y -= self.playerspeed
        if keys[K_DOWN] and y + self.playerspeed + self.height <= window_height:
            y += self.playerspeed

        self.coordinates = (x, y)