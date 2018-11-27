import pygame as pg
import random
window = pg.display.set_mode((800, 500))
window.fill((255, 255, 255))
running = True
clock = pg.time.Clock()

s = pg.Surface((100, 100))
s.fill((100, 255, 50))
srunning = True
window.blit(s, (0,0))

s2 = pg.Surface((100, 100))
s2.fill((50, 100, 250))
s2.set_colorkey((250, 0 ,0))

s2running = True
window.blit(s2,(100,0))

s3 = pg.Surface((50,50))
s3.fill((255, 0 ,0))
s2.blit(s3, (50,0))
s.blit(s3, (0,0))
window.blit(s2,(100,0))

class Button():
    def __init__(self, window):
        # The window (screen) that will be drawn on
        self.window = window
        self.x = 100;
        self.y = 200;
        self.w = 100;
        self.h = 50;
        self.backgroundColor = [255, 255, 25]
        self.borderColor = [0, 255, 0]
        self.borderThickness = 1
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.surface = pg.Surface((self.w, self.h))
        self.surface.fill(self.backgroundColor)

    def addText(self, text):
        self.font = pg.font.SysFont('Arial', 25)
        self.text = self.font.render(text, True, (100,120,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.w/2, self.h/2)
        self.surface.blit(self.text, self.text_rect)


    def click(self, event, callback, *args, **kwargs):
        if event.type == pg.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pg.mouse.get_pos()
            #if(mouseX >= self.x and mouseX <= self.x + self.w and mouseY >= self.y and mouseY <= self.y + self.h) :
            if(self.rect.collidepoint((mouseX, mouseY))):
                callback(*args, **kwargs)

    def draw(self):
        # Draw a rect on top of self.surface at position (0,0) relative to the self.surface.  It is different than the self.rect declared above
        self.window.blit(self.surface, (self.x, self.y))
        pg.draw.rect(self.surface, self.borderColor, [0, 0, self.w, self.h], self.borderThickness)
# End class button


b1 = Button(window)

def test(x):
    s.fill(x)
    window.blit(s, (0,0))

while running:
    clock.tick(10)
    for event in pg.event.get():
        b1.click(event, test, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
        if event.type == pg.QUIT:
            running = False

    # if srunning:
    #     s.fill((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    #     window.blit(s, (0,0))
    #
    # if s2running:
    #     s2.fill((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    #     window.blit(s2, (100,0))

    b1.draw()

    pg.display.flip()



pg.quit()
