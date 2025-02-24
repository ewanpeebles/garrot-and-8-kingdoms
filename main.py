# Import pygame library
import pygame
from pygame.locals import *

# Import Rectangle class from assets/scripts/pawn.py
from assets.scripts.pawn import Rectangle

# Initialize pygame
pygame.init()

# Load textures
missing = pygame.image.load('assets/images/missing.png')
generic_terrain = pygame.image.load('assets/images/terrain/generic_terrain.png')

# Screen creation and size
screen = pygame.display.set_mode((500, 500))
screenX = screen.get_width()
screenY = screen.get_height()
generic_terrain_bg = pygame.transform.scale(generic_terrain, (screen.get_width(), screen.get_height()))

# Create a pawn object for player
pawn = Rectangle()
pawn.coordinates = (((screen.get_height() / 2) - (pawn.length / 2)), ((screen.get_width() / 2) - (pawn.length / 2)))
pawn.playerspeed = 0.1

# Prepare for game loop
gameOn = True

screen.blit(generic_terrain_bg, (0, 0))

# Game loop
while gameOn:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
    
    pawn.moveByKeysDown(screen.get_width(), screen.get_height())

    screen.blit(generic_terrain_bg, (0, 0))
    screen.blit(pawn.surf, pawn.coordinates)
    pygame.display.flip()