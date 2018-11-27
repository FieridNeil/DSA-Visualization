import pygame as pg
import random as rd
pg.init()
window = pg.display.set_mode((840, 460), pg.DOUBLEBUF, 32)
window.fill((255, 255, 255))
running = True
clock = pg.time.Clock()

class Control():
    def __init__(self, window, x, y, w, h, bgColor, borderColor, borderThickness):
        # The window (screen) that will be drawn on
        self.window = window
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
        self.bgColor = bgColor
        self.borderColor = borderColor
        self.borderThickness = borderThickness
        self.rect = pg.Rect(self.x, self.y, self.w, self.h) # Needed for interaction (button click, mouseover, etc), not needed for decoration
        self.surface = pg.Surface((self.w, self.h))

    def addText(self, text):
        self.font = pg.font.SysFont('Arial', 25)
        self.text = self.font.render(text, True, (100,120,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.w/2, self.h/2)
        self.surface.blit(self.text, self.text_rect)

    def draw(self):
        # Draw a rect on top of self.surface at position (0,0) relative to the self.surface.  It is different than the self.rect declared above
        self.rect = pg.Rect(self.x, self.y, self.w, self.h) # Recreating when x, y, w, h change
        self.surface = pg.Surface((self.w, self.h)) # Recreating when x, y, w, h change
        self.surface.fill(self.bgColor)
        self.window.blit(self.surface, (self.x, self.y))
        pg.draw.rect(self.surface, self.borderColor, [0, 0, self.w, self.h], self.borderThickness)
# End class Control


class Button(Control):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def addText(self, *args, **kwargs):
        super().addText(*args, **kwargs)

    def click(self, event, callback, *args, **kwargs):
        if event.type == pg.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pg.mouse.get_pos()
            if(self.rect.collidepoint((mouseX, mouseY))):
                callback(*args, **kwargs)

    def draw(self):
        super().draw()
# End class button

# Draw transparent surface 1
s = pg.Surface((100,100), pg.SRCALPHA)   # per-pixel alpha
s.fill((255,0,255,128))                         # notice the alpha value in the color
window.blit(s, (0,0))

# Draw transparent surface 2
s2 = pg.Surface((100,100))  # the size of your rect
s2.set_alpha(255)                # alpha level
s2.fill((255,0 ,255))           # this fills the entire surface
window.blit(s2, (100,0))    # (0,0) are the top-left coordinates


b1 = Button(window, 100, 200, 100, 50, (255, 0, 20), (0, 255, 0), 1)

b1.addText("Hi")
b2 = Button(window, 200, 200, 100, 50, (0, 255, 20), (20, 255, 0), 1)

while running:
    # window.fill((255, 255, 255)) # To clear the screen
    clock.tick(10)
    for event in pg.event.get():
        b1.click(event, lambda x, y: print(x + y), 1, 2)
        b2.click(event, lambda x, y: print(x * y), 1, 2)
        if event.type == pg.QUIT:
            running = False

    # if srunning:
    #     s.fill((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    #     window.blit(s, (0,0))
    #
    # if s2running:
    #     s2.fill((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    #     window.blit(s2, (100,0))
    b1.bgColor = (rd.randrange(0, 255), rd.randrange(0, 255), rd.randrange(0, 255))
    b1.w = b1.w + 1
    b1.h = b1.h + 1
    b1.x = b1.x + 1
    b1.y = b1.y + 1
    b1.draw()
    b2.draw()
    pg.display.flip()



pg.quit()
