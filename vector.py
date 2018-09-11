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

input = TextBox(window, 100, 0, 200, 30, (255, 255, 25), (0, 0, 0), 1)
generateBtn = Button(window, 300, 0, 100, 30, (255, 255, 255), (231, 21, 32), 1)
generateBtn.addText('Generate')
Btn = Button(window, 400, 0, 100, 30, (255, 255, 255), (231, 21, 32), 1)
Btn.addText('add back')
def drawbox(items):
    sur1.fill((0, 255, 255))
    for i,val in enumerate(items):
        box = Control(sur1, i * 100, 0, 100, 100, (255, 255, 255), (255, 0, 0), 1)
        box.addText(str(val))
        box.draw()

class Vector:
    ''' @s: the surface that will be drawn on
        @elms: a list of elements
    '''
    def __init__(self, s):
        self.s = s
        self.elms = []

    def addElms(self, elms):
        self.elms = elms

    def addBack(self, *args):
        self.elms.append(args[0])
        self.draw()

    def draw(self):
        self.s.fill((0, 255, 255))
        for i,val in enumerate(self.elms):
            box = Control(self.s, i * 100, 0, 100, 100, (255, 255, 255), (255, 0, 0), 1)
            box.addText(str(val))
            box.draw()
# End class Vector

v = Vector(sur1)


while running:
    # window.fill((255, 255, 255)) # To clear the screen
    clock.tick(10)
    for event in pg.event.get():
        input.handle(event)
        generateBtn.click(event, v.addElms, input.getText().split())
        Btn.click(event, v.addBack, 0)
        if event.type == pg.QUIT:
            running = False
    #End event

    window.blit(sur1, (0, 100))
    v.draw()
    label.draw()
    input.draw()
    generateBtn.draw()
    Btn.draw()
    pg.display.flip()



pg.quit()
