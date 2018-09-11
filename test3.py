import pygame as pg
import random
from control import *
pg.init()

window = pg.display.set_mode((860, 480))
window.fill((255, 255, 255))

clock = pg.time.Clock()
running = True
list = []
for i in range(0, 10):
    list.append(IControl(window, i * 50, 0, 50, 50, (255, 255, 255), (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), 3))


def mouseover():
    for c in list:
        if c.rect.collidepoint(pg.mouse.get_pos()):
            c.borderThickness = 0
        else:
            c.borderThickness = 3



while running:
    clock.tick(20)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    # end event
    mouseover()
    for c in list:
        c.draw()

    pg.display.flip()

#end program
pg.quit()
