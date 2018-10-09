import pygame as pg
import math

pg.init()
clock = pg.time.Clock()


window = pg.display.set_mode((800, 480))
window.fill((255, 255, 255))
running = True


sur = pg.Surface((800, 300))
sur.fill((5, 200, 255))

rect = pg.Rect(0, 0, 50, 50)
btn = pg.Rect(0, 0, 100, 50)


def update():
    t = -math.pi
    while t < math.pi:
        rect.x += math.sin(t)
        rect.y += math.cos(t)
        t += 0.1
        sur.fill((5, 200, 255))
        pg.draw.rect(sur, (100, 200, 100), rect)
        window.blit(sur, (0,100))

        pg.display.update(sur.get_rect())


print(math.sin(0))
print(math.cos(0))
print(math.pi)
while running:
    clock.tick(60)
    window.fill((255, 255, 255))
    sur.fill((5, 200, 255))

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        if e.type == pg.MOUSEBUTTONDOWN:
            if btn.collidepoint(pg.mouse.get_pos()):
                update()
    # end event handling

    pg.draw.rect(window, (200, 0, 150), btn)

    pg.draw.rect(sur, (100, 200, 100), rect)
    window.blit(sur, (0,100))

    pg.display.flip()

pg.quit()
