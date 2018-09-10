import pygame as pg
pg.init()
window = pg.display.set_mode((840, 460))
window.fill((255, 255, 255))
running = True
clock = pg.time.Clock()

class A:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def show(self):
        print(self.v1, self.v2, self.v3)

class B(A):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show(self):
        super().show()


a = A(1,2,3)
a.show()

b = B(v1 = 5, v2 = 9, v3 = 1)
b.show()

class Control():
    def __init__(self, window, x, y, w, h, bgColor, borderColor, borderThickness):
        # The window (screen) that will be drawn on
        self.window = window
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
        self.backgroundColor = bgColor
        self.borderColor = borderColor
        self.borderThickness = borderThickness
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.surface = pg.Surface((self.w, self.h))
        self.surface.fill(self.backgroundColor)

    def addText(self, text):
        self.font = pg.font.SysFont('Arial', 25)
        self.text = self.font.render(text, True, (100,120,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.w/2, self.h/2)
        self.surface.blit(self.text, self.text_rect)

    def draw(self):
        # Draw a rect on top of self.surface at position (0,0) relative to the self.surface.  It is different than the self.rect declared above
        self.window.blit(self.surface, (self.x, self.y))
        pg.draw.rect(self.surface, self.borderColor, [0, 0, self.w, self.h], self.borderThickness)
# End class button


class Button(Control):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def addText(self, text):
        super().addText(*args, **kwargs)


    def click(self, event, callback, *args, **kwargs):
        if event.type == pg.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pg.mouse.get_pos()
            #if(mouseX >= self.x and mouseX <= self.x + self.w and mouseY >= self.y and mouseY <= self.y + self.h) :
            if(self.rect.collidepoint((mouseX, mouseY))):
                callback(*args, **kwargs)

    def draw(self):
        super().draw()
# End class button
b1 = Button(window, 100, 200, 100, 50, [255, 255, 20], [0, 255, 0], 1)
b2 = Button(window, 200, 200, 100, 50, [0, 255, 20], [20, 255, 0], 1)

while running:
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

    b1.draw()
    b2.draw()
    pg.display.flip()



pg.quit()
