import pygame as pg
class MySurface:
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
