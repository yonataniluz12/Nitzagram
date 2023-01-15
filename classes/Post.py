import pygame
from constants import *
from helpers import screen
from classes.Comment import Comment

class Post:
    """
    A class used to represent post on Nitzagram
    """
    user_name = "yonatan_iluz"
    def __init__(self, image_src, location, description):
        #TODO: write me!


        self.image_src = image_src

        self.location = location
        self.description = description
        self.comments = []
        self.likes_counter = 0
        self.comments_display_index = 0

    def display(self):
        self.display_content()
        self.display_header()
        self.display_likes()
        self.display_comments()

    def display_content(self):
        img = pygame.image.load(self.image_src)
        img = pygame.transform.scale(img,(POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))

    def display_header(self):
        font = pygame.font.SysFont("chalkduster.ttf",15)
        text = font.render(self.location, True, LIGHT_GRAY)
        screen.blit(text,[LOCATION_TEXT_X_POS,LOCATION_TEXT_Y_POS])

        font_name = pygame.font.SysFont("chalkduster.ttf", 15)
        text_name = font_name.render(self.user_name, True, GREY)
        screen.blit(text_name, [USER_NAME_X_POS, USER_NAME_Y_POS])

        font_description= pygame.font.SysFont("chalkduster.ttf",15)
        text_description= font_description.render(self.description, True, GREY)
        screen.blit(text_description,[DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS])

    def display_likes(self):
        font = pygame.font.SysFont("chalkduster.ttf",15)
        text = font.render(f"Liked by {self.likes_counter} users", True,BLACK)
        screen.blit(text,[LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS])

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, comment_text):
        comment = Comment(comment_text)
        self.comments.append(comment)
