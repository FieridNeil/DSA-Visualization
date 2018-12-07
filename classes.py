import pygame as pg

# class to draw a rectangle
class Rectangle:
    def __init__(self, parent, x, y, w, h, color, font, value):
        # self.font = font
        self.parent = parent
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = value
        self.surface = pg.Surface((self.w, self.h))
        self.color = color
        self.text = font.render(str(value), False, (0, 0, 0))

    def draw(self):
        self.surface.fill(self.color)
        self.surface.blit(self.text, (self.w / 2 - self.text.get_width() / 2, self.h / 2 - self.text.get_height() / 2))
        self.parent.blit(self.surface, (self.x, self.y))

    def collide(self, point):
        if(pg.Rect(self.x, self.y, self.w, self.h).collidepoint(point)):
            return True
        return False

    def __lt__(self, other):
        return self.v < other.v

# class to draw an ellipse
class Ellipse:
    def __init__(self, parent, x, y, w, h, color, font, value):
        # self.font = font
        self.parent = parent
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = value
        self.color = color
        self.text = font.render(str(value), False, (0, 0, 0))

    def draw(self):
        pg.draw.ellipse(self.parent, self.color, (self.x, self.y, self.w, self.h), 0)
        self.parent.blit(self.text, (self.x + self.w / 2 - self.text.get_width() / 2, self.y + self.h / 2 - self.text.get_height() / 2))
