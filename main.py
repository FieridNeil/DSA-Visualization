import pygame as pg
from classes import *
from modules import *

# Initialize some required variables
pg.init()
window = pg.display.set_mode((648, 480))
running = True
font = pg.font.SysFont('Arial', 15)
font2 = pg.font.SysFont('Arial', 30)

# Text
welcomeText = font2.render("Data Structure and Algorithm Visualization", False, (0, 0, 0))
authorText = font2.render("By: Hympert Nguyen", False, (0, 0, 0))
sortText = font.render("Sorting Algorithms", False, (0, 0, 0))
searchText = font.render("Searching Algorithms", False, (0, 0, 0))
treeText = font.render("Tree Data Structure", False, (0, 0, 0))

# Buttons
selectionSortBtn = Rectangle(window, 50, 100, 100, 50, (255, 200, 200), font, 'selection sort')
quickSortBtn = Rectangle(window, 150, 100, 100, 50, (255, 200, 250), font, 'quick sort')
sequentialSearchBtn = Rectangle(window, 50, 200, 100, 50, (255, 100, 250), font, 'sequential search')
binarySearchBtn = Rectangle(window, 150, 200, 100, 50, (0, 100, 250), font, 'binary search')
BSTBtn = Rectangle(window, 50, 300, 100, 50, (100, 200, 200), font, 'binary search tree')


# Main loop
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
            #Button handles binary search tree
            if BSTBtn.collide(e.pos):
                binary_search_tree_module()
    #end event handling

    # Draw text and buttons
    window.fill((180, 220, 255))
    window.blit(welcomeText, (100, 10))
    window.blit(authorText, (400, 400))
    window.blit(sortText, (50, 80))
    selectionSortBtn.draw()
    quickSortBtn.draw()
    window.blit(searchText, (50, 180))
    sequentialSearchBtn.draw()
    binarySearchBtn.draw()
    window.blit(treeText, (50, 280))
    BSTBtn.draw()
    pg.display.flip()

# end while
pg.quit()
