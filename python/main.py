import pygame as pg
from classes import *
from modules import *

pg.init()
window = pg.display.set_mode((648, 480))
window.fill((255, 255, 255))
running = True
font = pg.font.SysFont('Arial', 15)
# Buttons
selectionSortBtn = MySurface(window, 0, 0, 100, 50, (255, 200, 200), font, 'selection sort')
quickSortBtn = MySurface(window, 100, 0, 100, 50, (255, 200, 250), font, 'quick sort')
sequentialSearchBtn = MySurface(window, 200, 0, 100, 50, (255, 100, 250), font, 'sequential search')
binarySearchBtn = MySurface(window, 300, 0, 100, 50, (0, 100, 250), font, 'binary search')

while running:

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False
        if e.type == pg.MOUSEBUTTONDOWN:
            # Button handles selection sort
            if selectionSortBtn.collide(e.pos):
                selection_sort_module()
            # Button handles quick sort
            if quickSortBtn.collide(e.pos):
                quick_sort_module()
            # Button handles sequential search
            if sequentialSearchBtn.collide(e.pos):
                sequential_search_module()
            #Button handles binary search
            if binarySearchBtn.collide(e.pos):
                binary_search_module()

    #end event handling
    selectionSortBtn.draw()
    quickSortBtn.draw()
    sequentialSearchBtn.draw()
    binarySearchBtn.draw()
    pg.display.flip()

# end while
pg.quit()
