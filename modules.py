import math
from classes import *
from algorithms import *

def selection_sort_module():
    window = pg.display.set_mode((640, 480))
    running = True
    font = pg.font.SysFont('Arial', 15)
    t = 9.5     # input of parameterized parabola equation for animation movement.  9.5 seems to work thru trials and errors
    sorting = False
    # Button
    sort = Rectangle(window, 0, 0, 100, 50, (255, 200, 200), font, 'sort')
    home = Rectangle(window, 100, 0, 100, 50, (255, 200, 200), font, 'return to menu')

    # Vector to animate
    v = VectorLog(0, 0)
    # VectorLog just to log the index pair, has to have the same number and order of elements as v
    log = VectorLog(0,0)
    arr = random.sample(range(20), 10)
    for i, val in enumerate(arr):
        v.add_back(Rectangle(window, i * 50, 200, 50, 50, (255, 150, 255), font, val))
        log.add_back(val)

    while running:
        window.fill((255, 255, 255))
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            if e.type == pg.MOUSEBUTTONDOWN:
                if sort.collide(e.pos):
                    log = in_place_selection_sort(log)
                    sorting = True
                if home.collide(e.pos):
                    running = False
        # end event handling
        # animation state
        if sorting:
            # if there is something in the log queue, do the animation
            if log.log:
                pg.time.delay(50)
                # get the first (i,j) index pair in the log queue
                i = log.log[0][0]
                j = log.log[0][1]

                # t controls the movement of the animation (input to the parameterized parabola equation)
                if t >= -9.5:
                    neg = 1
                    if t <= 0:
                        neg = -1
                    # set color of the 2 currently being animated values to another color for visual effect
                    v[i].color = (255, 255, 0)
                    v[j].color = (255, 255, 0)
                    # to get consistent different distance between 2 points we want to move, get the index and multiply with 50 (default width)
                    # v[j].x - v[i].x where i < j will NOT work since v[i].x and v[j].x are changing with every iteration
                    v[i].x += math.fabs(j * 50 - i * 50) / 20
                    v[i].y -= t ** 2 * 0.4 * neg
                    v[j].x -= math.fabs(j * 50 - i * 50) / 20
                    v[j].y += t ** 2 * 0.4 * neg
                    t -= 1

                else:
                    # after swap animation of 1 pair completes, swap the actual element as well since animation doesnt actually swap the elements
                    temp = v[i]
                    v[i] = v[j]
                    v[j] = temp
                    t = 9.5
                    # delete the first element so that the 2nd element becomes first again (act like a queue)
                    del log.log[0]
                    # the ith item is already in the right place, however the jth item might not, so we need to set the color back to the same color as the whole array
                    v[j].color = (255, 150, 255)
            else:
                # Done sorting
                sorting = False
                # Change the color of the whole array to indicate that it's done
                for sur in v:
                    sur.color = (255, 255, 0)
            # end animation state

        for sur in v:
            sur.draw()

        sort.draw()
        home.draw()
        pg.display.flip()
    # end while
    # Final clear of the screen before return to the menu
    window.fill((255, 255, 255))

# End selection_sort

def quick_sort_module():
    window = pg.display.set_mode((640, 480))
    running = True
    font = pg.font.SysFont('Arial', 15)
    t = 9.5     # input of parameterized parabola equation for animation movement.  9.5 seems to work thru trials and errors
    sorting = False
    pivot = 0
    # Button and text
    sort = Rectangle(window, 0, 0, 100, 50, (255, 200, 200), font, 'sort')
    home = Rectangle(window, 100, 0, 100, 50, (255, 200, 200), font, 'return to menu')
    text = font.render("pivot: " + str(pivot), False, (0, 0, 0))

    # Vector to animate
    v = VectorLog(0, 0)
    # VectorLog just to log the index pair, has to have the same number and order of elements as v
    log = VectorLog(0,0)
    arr = random.sample(range(20), 10)
    for i, val in enumerate(arr):
        v.add_back(Rectangle(window, i * 50, 200, 50, 50, (255, 150, 255), font, val))
        log.add_back(val)

    while running:
        window.fill((255, 255, 255))
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            if e.type == pg.MOUSEBUTTONDOWN:
                if sort.collide(e.pos):
                    log = inplace_quick_sort(log)
                    for i in log.log:
                        print(i)
                    for key, value in log.extra.items():
                        print(key, value)
                    sorting = True
                    for j in log.pivot:
                        print(j)
                if home.collide(e.pos):
                    running = False
        # end event handling
        # animation state
        if sorting:
            # if there is something in the log queue, do the animation
            if log.log:
                # print out the pivot on the screen
                if log.pivot:
                    text = font.render("pivot: " + str(log.pivot[0]), False, (0, 0, 0))
                pg.time.delay(100)
                # get the first (i,j) index pair in the log queue
                i = log.log[0][0]
                j = log.log[0][1]

                # t controls the movement of the animation (input to the parameterized parabola equation)
                if t >= -9.5:
                    neg = 1
                    if t <= 0:
                        neg = -1
                    # set color of the 2 currently being animated values to another color for visual effect
                    v[i].color = (255, 255, 0)
                    v[j].color = (255, 255, 0)
                    # to get consistent different distance between 2 points we want to move, get the index and multiply with 50 (default width)
                    # v[j].x - v[i].x where i < j will NOT work since v[i].x and v[j].x are changing with every iteration
                    v[i].x += math.fabs(j * 50 - i * 50) / 20
                    v[i].y -= t ** 2 * 0.4 * neg
                    v[j].x -= math.fabs(j * 50 - i * 50) / 20
                    v[j].y += t ** 2 * 0.4 * neg
                    t -= 1

                else:
                    # after swap animation of 1 pair completes, swap the actual element as well since animation doesnt actually swap the elements
                    temp = v[i]
                    v[i] = v[j]
                    v[j] = temp
                    t = 9.5
                    # delete the first element so that the 2nd element becomes first again (act like a queue)
                    del log.log[0]
                    if log.pivot:
                        del log.pivot[0]
                    # the ith item is already in the right place, however the jth item might not, so we need to set the color back to the same color as the whole array
                    v[j].color = (255, 150, 255)
            else:
                # Done sorting
                sorting = False
                # Change the color of the whole array to indicate that it's done
                for sur in v:
                    sur.color = (255, 255, 0)
            # end animation state

        for sur in v:
            sur.draw()

        sort.draw()
        home.draw()
        window.blit(text, (0, 100))
        pg.display.flip()

    # end while
    # Final clear of the screen before return to the menu
    window.fill((255, 255, 255))
# End quick_sort

def sequential_search_module():
    window = pg.display.set_mode((640, 480))
    running = True
    font = pg.font.SysFont('Arial', 15)
    elmToSearch = random.randrange(0, 100)
    text = font.render("Searching for: " + str(elmToSearch), False, (0, 0, 0))

    # Button
    search = Rectangle(window, 0, 0, 100, 50, (255, 200, 200), font, 'search')
    home = Rectangle(window, 100, 0, 100, 50, (255, 200, 200), font, 'return to menu')

    v = VectorLog(0, 0)
    # VectorLog just to log the comparing element has to have the same number and order of elements as v
    log = VectorLog(0,0)
    arr = random.sample(range(20), 10)
    for i, val in enumerate(arr):
        v.add_back(Rectangle(window, i * 50, 200, 50, 50, (50, 255, 255), font, val))
        log.add_back(val)

    while running:
        window.fill((255, 255, 255))
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            if e.type == pg.MOUSEBUTTONDOWN:
                for elm in v:
                    if elm.collide(e.pos):
                        elmToSearch = elm.v
                        text = font.render("Searching for: " + str(elmToSearch), False, (0, 0, 0))
                if search.collide(e.pos):
                    ans = sequential_search(log, elmToSearch)
                if home.collide(e.pos):
                    running = False
        # end event handling
        # animation state
        if log.log:
            pg.time.delay(200)
            if ans == None:
                v[log.log[0]].color = (200, 200, 200)
                del log.log[0]
            else:
                if len(log.log) > 1:
                    v[log.log[0]].color = (200, 200, 200)
                    del log.log[0]
                else:
                    v[log.log[0]].color = (0, 255 , 0)

        for sur in v:
            sur.draw()

        search.draw()
        home.draw()
        window.blit(text, (0, 100))
        pg.display.flip()

    # end while
    # Final clear of the screen before return to the menu
    window.fill((255, 255, 255))
# End sequential_search

def binary_search_module():
    window = pg.display.set_mode((640, 480))
    font = pg.font.SysFont('Arial', 15)
    running = True
    searching = False
    elmToSearch = random.randrange(0, 100)
    text = font.render("Searching for: " + str(elmToSearch), False, (0, 0, 0))
    idx = 0
    # Button
    search = Rectangle(window, 0, 0, 100, 50, (255, 200, 200), font, 'search')
    home = Rectangle(window, 100, 0, 100, 50, (255, 200, 200), font, 'return to menu')

    v = VectorLog(0, 0)
    # VectorLog just to log the comparing element has to have the same number and order of elements as v
    log = VectorLog(0,0)
    arr = random.sample(range(20), 10)
    for i in arr:
        log.add_back(i)

    log = inplace_quick_sort(log)
    # clear the log because quicksort will also store the indices that are swapping, which we arent interested  in
    log.log = []
    for i, val in enumerate(log):
        v.add_back(Rectangle(window, i * 50, 200, 50, 50, (90, 255, 255), font, val))


    while running:
        window.fill((255, 255, 255))

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            if e.type == pg.MOUSEBUTTONDOWN:
                for elm in v:
                    if elm.collide(e.pos):
                        elmToSearch = elm.v
                        text = font.render("Searching for: " + str(elmToSearch), False, (0, 0, 0))
                if search.collide(e.pos):
                    print(elmToSearch)
                    ans = binary_search(log, elmToSearch)
                    print(ans)
                    for i in log.log:
                        print(i)
                    searching = True
                if home.collide(e.pos):
                    running = False
        # end event handling
        # animation state
        if searching:
            pg.time.delay(100)
            # magic
            if log.log:
                if idx < log.log[0][0]:
                    v[idx].color = (200, 200, 200)
                elif (log.log[0][1] - 1 - log.log[0][0] >= 0):
                    v[log.log[0][0]].color = (90, 255, 255)
                    log.log[0][0] += 1
                elif idx > len(log.log):
                    del log.log[0]
                    idx = -1
                else:
                    v[idx].color = (200, 200, 200)
                idx += 1
            else:
                for i in v:
                    i.color = (200, 200, 200)
                if ans != None:
                    v[ans].color = (50, 255, 50)
        # end animation

        for sur in v:
            sur.draw()

        search.draw()
        home.draw()
        window.blit(text, (0, 100))
        pg.display.flip()

    # end while
    # Final clear of the screen before return to the menu
    window.fill((255, 255, 255))
# End sequential_search

# BST module
def _inorder(tree, parent, x, y, w, h, color, font, diffX):
    '''diffX is the X difference between parent node and its children nodes
        the difference is shortened by half going from parent to children
                  O
                 / \
               /     \
             /         \
            O -- 100 -- 0
          /    \     /    \
        O - 50 - O O - 50 - O
    '''
    if tree != None:
        _inorder(tree.leftChild, parent, x - diffX, y + 50, w, h, color, font, diffX / 2)
        if(tree.leftChild != None):
            pg.draw.aaline(parent, (0, 0, 0), (x + 25, y+ 25), (x + 25 - diffX, y + 25 + 50), 1)
        Ellipse(parent, x, y, w, h, color, font, tree.get()).draw()
        if(tree.rightChild != None):
            pg.draw.aaline(parent, (0, 0, 0), (x + 25, y + 25), (x + 25 + diffX, y + 25 +50), 1)
        _inorder(tree.rightChild, parent, x + diffX, y + 50, w, h, color, font, diffX / 2)

def binary_search_tree_module():
    window = pg.display.set_mode((640, 480))
    running = True
    font = pg.font.SysFont('Arial', 15)
    # Button
    home = Rectangle(window, 0, 0, 100, 50, (255, 200, 200), font, 'return to menu')

    mytree = BST()
    mytree.insert(8)
    mytree.insert(4)
    mytree.insert(2)
    mytree.insert(1)
    mytree.insert(3)
    mytree.insert(6)
    mytree.insert(5)
    mytree.insert(7)
    mytree.insert(12)
    mytree.insert(10)
    mytree.insert(9)
    mytree.insert(11)
    mytree.insert(14)
    mytree.insert(13)
    mytree.insert(15)

    print(mytree.root.get())

    while running:
        window.fill((255, 255, 255))

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            if e.type == pg.MOUSEBUTTONDOWN:
                if home.collide(e.pos):
                    running = False
        # end event handling
        # function that draws the tree
        _inorder(mytree.root, window, 300, 100, 50, 50, (90, 250, 255), font, 150)
        home.draw()

        pg.display.flip()

    # end while
    # Final clear of the screen before return to the menu
    window.fill((255, 255, 255))
# End bst
