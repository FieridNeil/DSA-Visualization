import pygame as pg
from control import *

pg.init()
clock = pg.time.Clock()
window = pg.display.set_mode((860, 480))
window.fill((255, 255, 255))
running = True

sur1 = pg.Surface((860, 300))
sur1.fill((0, 255, 255))
window.blit(sur1, (0, 100))

label = Control(window, 0, 0, 100, 30, (255, 255, 255), (255, 255, 255), 1)
label.addText('Elements: ')

input = TextBox(window, 100, 0, 150, 30, (255, 255, 25), (0, 0, 0), 1)
generateBtn = Button(window, 300, 0, 100, 30, (255, 255, 255), (231, 21, 32), 1)
generateBtn.addText('Generate')

def drawbox(items):
    sur1.fill((0, 255, 255))
    for i,val in enumerate(items):
        box = Control(sur1, i * 100, 0, 100, 100, (255, 255, 255), (255, 0, 0), 1)
        box.addText(str(val))
        box.draw()




while running:
    # window.fill((255, 255, 255)) # To clear the screen
    clock.tick(10)
    for event in pg.event.get():
        input.handle(event)
        generateBtn.click(event, drawbox, input.getText().split())
        if event.type == pg.QUIT:
            running = False
    #End event

    window.blit(sur1, (0, 100))

    label.draw()
    input.draw()
    generateBtn.draw()
    pg.display.flip()



pg.quit()
