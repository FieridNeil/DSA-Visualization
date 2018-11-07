import pygame as pg
import math
import random
from vector import *
from sort import *

# Variable initialization
pg.init()
window = pg.display.set_mode((680,480))
window.fill((255, 255, 255))
running = True
font = pg.font.SysFont('Arial', 15)

class MySurface:
    def __init__(self, parent, x, y, w, h, color, font, value):
        # self.font = font
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

    def draw(self):
        self.surface.fill(self.color)
        self.surface.blit(self.text, (self.w / 2 - self.text.get_width() / 2, self.h / 2 - self.text.get_height() / 2))
        self.parent.blit(self.surface, (self.x, self.y))

    def collide(self, point):
        if(pg.Rect(self.x, self.y, self.w, self.h).collidepoint(point)):
            return True
        return False

    def __lt__(self, other):
        return self.v < other.v

# SELECTION SORT
# Vector to animate
isV = VectorLog(0, 0)
# VectorLog just to log the index pair, has to have the same number and order of elements as v
islog = VectorLog(0,0)
for i in range(0, 10):
    val = random.randrange(0, 20)
    isV.add_back(MySurface(window, i * 50, 100, 50, 50, (255, random.randrange(0, 255), 255), font, val))
    islog.add_back(val)

# QUICK SORT
# Vector to animate
qs = VectorLog(0, 0)
# VectorLog just to log the index pair, has to have the same number and order of elements as v
qslog = VectorLog(0,0)
for i in range(0, 10):
    val = random.randrange(0, 20)
    qs.add_back(MySurface(window, i * 50, 200, 50, 50, (255, 255, random.randrange(0, 255)), font, val))
    qslog.add_back(val)

# Buttons
selectionSortBtn = MySurface(window, 0, 0, 100, 50, (255, 200, 200), font, 'selection sort')
quickSortBtn = MySurface(window, 100, 0, 100, 50, (255, 200, 250), font, 'quick sort')
sequentialSearchBtn = MySurface(window, 200, 0, 100, 50, (255, 100, 250), font, 'sequential search')

# SEQUENTIAL SEARCH
# Vector to animate
ss = VectorLog(0, 0)
# VectorLog just to log the comparing element has to have the same number and order of elements as v
sslog = VectorLog(0,0)
for i in range(0, 10):
    val = random.randrange(0, 20)
    ss.add_back(MySurface(window, i * 50, 300, 50, 50, (random.randrange(0, 255), 255, 255), font, val))
    sslog.add_back(val)

# Buttons
selectionSortBtn = MySurface(window, 0, 0, 100, 50, (255, 200, 200), font, 'selection sort')
quickSortBtn = MySurface(window, 100, 0, 100, 50, (255, 200, 250), font, 'quick sort')
sequentialSearchBtn = MySurface(window, 200, 0, 100, 50, (255, 100, 250), font, 'sequential search')

# 9.5 seems to be the magic number
t = 9.5
while running:
    pg.time.delay(50)
    window.fill((255, 255, 255))
    for e in pg.event.get():
        if e.type == pg.MOUSEBUTTONDOWN:
            # Button handles selection sort
            if selectionSortBtn.collide(e.pos):
                islog = in_place_selection_sort(islog)
            # Button handles quick sort
            if quickSortBtn.collide(e.pos):
                for i in qslog:
                    print(i)
                # print("HI")
                qslog = inplace_quick_sort(qslog)
                for i in qslog.log:
                    print(i)
            # Button handles sequential search
            if sequentialSearchBtn.collide(e.pos):
                ans = sequential_search(sslog, 15)
                for i in sslog.log:
                    print(i)
                print("found {}".format(ans))
                print(len(sslog.log))
        elif e.type == pg.QUIT:
            running = False
    #end event handling

    # animation state, if there is something in the log queue
    if islog.log:
        # get the first (i,j) index pair in the log queue
        i = islog.log[0][0]
        j = islog.log[0][1]

        if t >= -9.5:
            neg = 1
            if t <= 0:
                neg = -1
            # to get consistent different distance between 2 points we want to move, get the index and multiply with 50 (default width)
            # v[j].x - v[i].x where i < j will NOT work since v[i].x and v[j].x are changing with every iteration
            isV[i].x += math.fabs(j * 50 - i * 50) / 20
            isV[i].y -= t ** 2 * 0.4 * neg
            isV[j].x -= math.fabs(j * 50 - i * 50) / 20
            isV[j].y += t ** 2 * 0.4 * neg
            t -= 1
        else:
            # after swap animation of 1 pair completes, swap the actual element as well since animation doesnt actually swap the elements
            temp = isV[i]
            isV[i] = isV[j]
            isV[j] = temp
            t = 9.5
            # delete the first element so that the 2nd element becomes first again (act like a queue)
            del islog.log[0]
    # end animation state

    # animation state, if there is something in the log queue
    if qslog.log:
        # get the first (i,j) index pair in the log queue
        i = qslog.log[0][0]
        j = qslog.log[0][1]

        if t >= -9.5:
            neg = 1
            if t <= 0:
                neg = -1
            # to get consistent different distance between 2 points we want to move, get the index and multiply with 50 (default width)
            # v[j].x - v[i].x where i < j will NOT work since v[i].x and v[j].x are changing with every iteration
            qs[i].x += math.fabs(j * 50 - i * 50) / 20
            qs[i].y -= t ** 2 * 0.4 * neg
            qs[j].x -= math.fabs(j * 50 - i * 50) / 20
            qs[j].y += t ** 2 * 0.4 * neg
            t -= 1
        else:
            # after swap animation of 1 pair completes, swap the actual element as well since animation doesnt actually swap the elements
            temp = qs[i]
            qs[i] = qs[j]
            qs[j] = temp
            t = 9.5
            # delete the first element so that the 2nd element becomes first again (act like a queue)
            del qslog.log[0]
    # end animation state

    # Animation state for sequential search
    if sslog.log:
        pg.time.delay(200)
        if ans == None:
            ss[sslog.log[0]].color = (255, 0, 0)
            del sslog.log[0]
        else:
            if len(sslog.log) > 1:
                ss[sslog.log[0]].color = (255, 0, 0)
                del sslog.log[0]
            else:
                ss[sslog.log[0]].color = (0, 255 , 0)
    # draw every element in the vector v

    for sur in isV:
        sur.draw()

    for sur in qs:
        sur.draw()

    for sur in ss:
        sur.draw()

    selectionSortBtn.draw()
    quickSortBtn.draw()
    sequentialSearchBtn.draw()
    pg.display.flip()




#end while
pg.quit()
