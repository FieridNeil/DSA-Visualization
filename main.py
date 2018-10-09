import pygame as pg
from control import *
from vector import *
from sort import *

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

btn1 = Button(window, 500, 0, 100, 30, (255, 255, 255), (231, 21, 32), 1)
btn1.addText('Generate2')

btn2 = Button(window, 0, 50, 100, 30, (255, 255, 255), (231, 21, 32), 1)
btn2.addText('swap')

btn3 = Button(window, 100, 50, 100, 30, (255, 255, 255), (231, 21, 32), 1)
btn3.addText('test')

btn4 = Button(window, 200, 50, 100, 30, (255, 255, 255), (231, 21, 32), 1)
btn4.addText('clear')

btn5 = Button(window, 300, 50, 150, 30, (255, 255, 255), (231, 21, 32), 1)
btn5.addText('selection sort')

btn6 = Button(window, 450, 50, 100, 30, (255, 255, 255), (231, 21, 32), 1)
btn6.addText('quick sort')
def drawbox(items):
    sur1.fill((0, 255, 255))
    for i,val in enumerate(items):
        box = Control(sur1, i * 100, 0, 100, 100, (255, 255, 255), (255, 0, 0), 1)
        box.addText(str(val))
        box.draw()

v1 = [2,6,4,7,8,5,1,3]
print(v1)
# v1 = in_place_selection_sort(v1)
# print(v1)

v = VectorAnim(sur1)


while running:
    # window.fill((255, 255, 255)) # To clear the screen
    clock.tick(10)
    for event in pg.event.get():
        input.handle(event)
        generateBtn.click(event, v.addElms, input.getText().split())
        Btn.click(event, v.addBack, 0)
        btn1.click(event, v. addElms, v1)
        btn2.click(event, v.swap, 0, 2)
        btn3.click(event, v.draw)
        btn4.click(event, v.clear)
        btn5.click(event, lambda : selection_sort(v))
        btn6.click(event, lambda : quick_sort(v))
        if event.type == pg.QUIT:
            running = False
    #End event


    # v.swapAnim(0, 2, 0, 200)
    v.draw()

    window.blit(sur1, (0, 100))
    label.draw()
    input.draw()
    generateBtn.draw()
    Btn.draw()
    btn1.draw()
    btn2.draw()
    btn3.draw()
    btn4.draw()
    btn5.draw()
    btn6.draw()


    pg.display.flip()



pg.quit()
