import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.Post import *
from test_methods import test_comment
from buttons import *
from helpers import *
from classes.Comment import *


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    post_list = []
    post = Post("Images//noa_kirel.jpg", "Israel", "hiii")
    post2 = Post("Images//ronaldo.jpg", "Israel", "hiii")
    post3 = Post("Images//noa_kirel.jpg", "Israel", "hiii")
    post4 = Post("Images//ronaldo.jpg", "Israel", "hiii")
    post_list.append(post)
    post_list.append(post2)
    post_list.append(post3)
    post_list.append(post4)
    current_index = 0
    current_post = post_list[current_index]

    print(post.user_name)
    running = True

    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_in_button(click_post_button, mouse_pos):
                    if current_index == len(post_list) - 1:
                        current_index = 0
                    else:
                        current_index += 1
                    current_post = post_list[current_index]

                if mouse_in_button(like_button, mouse_pos):
                    current_post.add_like()
                elif mouse_in_button(comment_button, mouse_pos):
                    comment = read_comment_from_user()  # Comment.user,,,(comment)
                    current_post.add_comment(comment)
        # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()
#        test_comment()
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)
    pygame.quit()
    quit()


main()


def mouse_in_button(button, mouse_pos):
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True
