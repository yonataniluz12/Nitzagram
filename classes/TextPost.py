from classes.Post import *
from helpers import *
import pywhatkit

class TextPost(Post):
    def __init__(self, color_text, text, background_color, location, description):
        Post.__init__(self, location, description)
        self.color_text = color_text
        self.background_color = background_color
        self.text = text
        self.textArray = from_text_to_array(self.text)

    def display_comments(self):
        square = pygame.Rect(POST_X_POS,POST_Y_POS,POST_WIDTH,POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, square)
        font = pygame.font.SysFont("chalkduster.ttf", TEXT_POST_FONT_SIZE)
        for i in range(len(self.textArray)):
            text = font.render(self.textArray[i], True, self.color_text)
            center = center_text(len(self.textArray), text, i)
            screen.blit(text, (center[0], center[1]))

    def share(self,phnum):
        if "+972" in phnum:
            pywhatkit.sendwhatmsg_instantly(phnum,"text post"+self.text + "\n" + "location:"
                                            + self.location + "\n"
                                            +"description:" + self.description, wait_time = 15)


