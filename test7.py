import pygame as pg
import math
import random
from vector import *
from sort import *

pg.init()
window = pg.display.set_mode((680,480))
window.fill((255, 255, 255))
running = True

font = pg.font.SysFont('Comic Sans MS', 15)

#
# text = font.render('Button', False, (0,0,0))
# btn = pg.Surface((100, 50))
# btn.fill((255, 255, 200))
# btn.blit(text, (btn.get_width() / 2 - text.get_width() / 2 ,btn.get_height() / 2 - text.get_height() /2 ))
#
# text = font.render('Sort', False, (0,0,0))
# sort_btn = pg.Surface((100, 50))
# sort_btn.fill((255, 200, 200))
# sort_btn.blit(text, (sort_btn.get_width() / 2 - text.get_width() / 2 , sort_btn.get_height() / 2 - text.get_height() / 2))


class MySurface:
    def __init__(self, parent, x, y, w, h, color, value):
        self.font = pg.font.SysFont('Comic Sans MS', 10)
        self.parent = parent
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = value
        self.color = color
        self.surface = pg.Surface((self.w, self.h))
        self.color = color
        self.text = font.render(str(value), False, (0, 0, 0))

    def update(self):
        self.text = font.render(str(self.v), False, (0, 0, 0))

    def draw(self):
        self.surface.fill(self.color)
        self.surface.blit(self.text, (self.w / 2 - self.text.get_width() / 2, self.h / 2 - self.text.get_height() / 2))
        self.parent.blit(self.surface, (self.x, self.y))

    def collide(self, point):
        if(pg.Rect(self.x, self.y, self.w, self.h).collidepoint(point)):
            return True
        return False

def in_place_selection_sort(V):
    for k in range(len(V) - 1):
        least_index = k
        for i in range(k+1, len(V)):
            if V[i].v < V[least_index].v:
                least_index = i
        # swap(V[least_index], V[k])
        temp = V[least_index].v
        V[least_index].v = V[k].v
        V[k].v = temp
    return V



v = Vector(0, 0)
for i in range(0, 10):
    val = random.randrange(0, 20)
    v.add_back(MySurface(window, i * 50, 200, 50, 50, (255, random.randrange(0, 255), 255), val))

for elm in v:
    print(elm.v)

btn = MySurface(window, 0, 0, 100, 50, (255, 255, 200), 'swap')
sort_btn = MySurface(window, 100, 0, 100, 50, (255, 200, 200), 'sort')

swap = False
# 9.5 seems to be the magic number
t = 9.5
while running:
    pg.time.delay(50)
    window.fill((255, 255, 255))
    for e in pg.event.get():
        if e.type == pg.MOUSEBUTTONDOWN:
            if btn.collide(e.pos):
                swap = True
            if sort_btn.collide(e.pos):
                v = in_place_selection_sort(v)
                print('--------------')
                for e in v:
                    print(e.v)
        elif e.type == pg.QUIT:
            running = False
    #end event handling

    # TODO: make into function
    if swap:
        if t >= -9.5:
            neg = 1
            if t <= 0:
                neg = -1
            # to get consistent different distance between 2 points we want to move, get the index and multiply with 50 (default width)
            # v[j].x - v[i].x where i < j will NOT work since v[i].x and v[j].x are changing with every iteration
            v[0].x += math.fabs(6 * 50 - 0 * 50) / 20
            v[0].y -= t ** 2 * 0.4 * neg
            v[6].x -= math.fabs(6 * 50 - 0 * 50) / 20
            v[6].y += t ** 2 * 0.4 * neg
            t -= 1
        else:
            t = 9.5
            swap = False




    for sur in v:
        sur.update()
        sur.draw()

    btn.draw()
    sort_btn.draw()
    pg.display.flip()




#end while
pg.quit()
