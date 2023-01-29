from classes.Post import Post
from constants import *
import pygame
from helpers import screen
import pywhatkit


class ImagePost(Post):

    def __init__(self, image_src, location, description, filter=None):
        Post.__init__(self, location, description)
        self.image_src = image_src
        self.filter = filter
        img = pygame.image.load(self.image_src)
        self.image = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))

        def display_content(self):
            screen.blit(self.image, (POST_X_POS, POST_Y_POS))
            if self.filter is not None:
                screen.blit(self.filter, (POST_X_POS, POST_Y_POS))

    def share(self,phnum):
        if "+972" in phnum:
            pywhatkit.sendwhats_image(phnum, self.image_src,self.description)
            pywhatkit.sendwhatmsg_instantly(phnum,"image" + "\n" + "location:"
                                            + self.location + "\n"
                                            +"description:" + self.description + "\n" , wait_time = 15)