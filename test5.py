import pygame as pg
pg.init()
clock = pg.time.Clock()
running = True
window = pg.display.set_mode((640, 480))
window.fill((255, 255, 255))
btn = pg.Rect(0, 0, 100, 30)
rect1 = pg.Rect(0, 30, 100, 100)

def test():
    while rect1.x < 500:
        rect1.x += 1
        window.fill((255, 255, 255))
        pg.draw.rect(window, (255, 0, 255), rect1, 1)
        pg.display.flip()

while running:
    clock.tick(5)
    window.fill((255, 255, 255))
    for e in pg.event.get():
        if e.type == pg.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pg.mouse.get_pos()
            if(btn.collidepoint((mouseX, mouseY))):
                test()
        if e.type == pg.QUIT:
            running = False
    #end event handling


    pg.draw.rect(window, (255, 0, 255), rect1, 1)
    pg.draw.rect(window, (0, 255, 255), btn)

    pg.display.flip()

#end main loop
pg.quit()
