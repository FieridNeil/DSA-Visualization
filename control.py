import pygame as pg


class Control():
    def __init__(self, window, x, y, w, h, bgColor, borderColor, borderThickness):
        # The window (screen) that will be drawn on
        self.window = window
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.bgColor = bgColor
        self.borderColor = borderColor
        self.borderThickness = borderThickness
        self.rect = pg.Rect(self.x, self.y, self.w, self.h) # Needed for interaction (button click, mouseover, etc), not needed for decoration
        self.surface = pg.Surface((self.w, self.h))
        self.surface.fill(self.bgColor)

    def addText(self, text):
        self.t = text;
        self.font = pg.font.SysFont('Arial', 25)
        self.text = self.font.render(self.t, True, (100,120,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.w/2, self.h/2)
        self.surface.blit(self.text, self.text_rect)

    def draw(self):
        # Draw a rect on top of self.surface at position (0,0) relative to the self.surface.  It is different than the self.rect declared above
        pg.draw.rect(self.surface, self.borderColor, [0, 0, self.w, self.h], self.borderThickness)
        self.window.blit(self.surface, (self.x, self.y))
# End class Control

# Interactive control (will update everything)
class IControl(Control):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def addText(self, *args, **kwargs):
        super().addText(*args, **kwargs)

    def draw(self):
        # Draw a rect on top of self.surface at position (0,0) relative to the self.surface.  It is different than the self.rect declared above
        self.rect = pg.Rect(self.x, self.y, self.w, self.h) # Recreating when x, y, w, h change
        self.surface = pg.Surface((self.w, self.h)) # Recreating when x, y, w, h change
        self.surface.fill(self.bgColor)
        # draw text on top
        pg.draw.rect(self.surface, self.borderColor, [0, 0, self.w, self.h], self.borderThickness)
        self.surface.blit(self.text, self.text_rect)
        self.window.blit(self.surface, (self.x, self.y))


# End class IControl

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

# End class button

# Textbox
class TextBox(Control):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.active = False
        self.text = ''
        self.fontsize = 30
        self.font = pg.font.Font(None, self.fontsize)
        self.text_surface = self.font.render(self.text, True, (255, 0 , 100))



    def handle(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.active = True
                print(self.active)
            else:
                self.active = False

        if event.type == pg.KEYDOWN:
            if self.active:
                # When return key is pressed
                if event.key == pg.K_RETURN:
                    self.text = ''
                # Delete character
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

            # To clear the text or delete character when users press backspace, we fill the surface first with a solid color
            self.surface.fill(self.bgColor)
            # Then we update the surface with text
            self.text_surface = self.font.render(self.text, True, (255, 0, 10))

    def getText(self):
        return self.text

    def draw(self):
        self.surface.blit(self.text_surface, (0, self.h / 2 - self.fontsize / 2))
        super().draw()

# End class TextBox
