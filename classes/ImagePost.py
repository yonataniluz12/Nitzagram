from classes.Post import Post
from constants import *
import pygame
from helpers import screen


class ImagePost(Post):

    def __init__(self, image_src, location, description, filter=None):
        Post.__init__(self, location, description)
        self.image_src = image_src
        self.filter = filter
        img = pygame.image.load(self.image_src)
        self.image = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))

        def display_content(self):
            screen.blit(self.image, (POST_X_POS, POST_Y_POS))
            if(self.filter != None):
                screen.blit(self.filter, (POST_X_POS, POST_Y_POS))