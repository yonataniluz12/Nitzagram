from classes.Post import Post
from constants import *
import pygame
from helpers import screen


class ImagePost(Post):

    def __init__(self, image_src, location, description, filter=None):
        Post.__init__(self, location, description)
        self.image_src = image_src
        self.filter = filter

        def display_content(self):
            img = pygame.image.load(self.image_src)
            img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))

            screen.blit(img, (POST_X_POS, POST_Y_POS))
            if(self.filter != None):
                self.filter = filter