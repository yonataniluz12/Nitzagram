from constants import *
import pygame
from helpers import screen


class Filter:

    def __init__(self,color,transparency):
        self.color = color
        self.transparency = transparency

    def apply_filter(self):
        rect = pygame.Surface((POST_WIDTH, POST_HEIGHT))
        rect.set_alpha(self.transparency)
        rect.fill(self.color)
        screen.blit(rect, (POST_X_POS, POST_Y_POS))