__author__ = 'wing2048'
import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_BORDER_TOP = True
SCREEN_BORDER_BOTTOM = True
SCREEN_BORDER_LEFT = True
SCREEN_BORDER_RIGHT = True

PIXELS_IN_METRE = 1
DOT_GAP = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FRAMERATE = 30

GRAVITY = 9.8 / PIXELS_IN_METRE
AIR_RESISTANCE_MULTIPLIER = 1
