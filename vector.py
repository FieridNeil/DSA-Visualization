import pygame as pg
import copy
from control import *

#FIRST \CodeArrayFirst
class Array:
    def __init__(self, length, default):
        if length < 0:
            raise ValueError
        self.length = length
        self.elements = [default] * length
    def __len__(self):
        return self.length
    def __iter__(self):
        return iter(self.elements)
    def __getitem__(self, i):
        if i < 0 or i >= self.length:
            raise IndexError
        return self.elements[i]
    def __setitem__(self, i, x):
        if i < 0 or i >= self.length:
            raise IndexError
        self.elements[i] = x
        return x
#LAST \CodeArrayLast

#FIRST \CodeVectorFirst
class Vector:
    def __init__(self, length, default):
        self.array = Array(length, default)
        self.in_use = 0
        for i in range(length):
            self.add_back(default)
    def __len__(self):
        return self.in_use
    def __iter__(self):
        return VectorIter(self)
    def __getitem__(self, i):
        if i < 0 or i >= self.in_use:
            raise IndexError
        return self.array[i]
    def __setitem__(self, i, x):
        if i < 0 or i >= self.in_use:
            raise IndexError
        self.array[i] = x
        return x
    def add_back(self, x):
        if self.in_use == len(self.array):
            if len(self.array) == 0:
                self._resize(1)
            else:
                self._resize(len(self.array) * 2)
        self.array[self.in_use] = x
        self.in_use += 1
    def remove_back(self):
        self.in_use -= 1
        if (3 * self.in_use) < len(self.array):
            self._resize(len(self.array) // 2)
    def _resize(self, new_capacity):
        new_array = Array(new_capacity, None)
        for i in range(self.in_use):
            new_array[i] = self.array[i]
        self.array = new_array
    def clear(self):
        while self.in_use > 0:
            self.remove_back()
    def swap_idx(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

        self.array[i], self.array[j] = self.array[j], self.array[i]
    def swap_elm(self, i, j):
        pass

#LAST \CodeVectorLast

#FIRST \CodeVectorIterFirst
class VectorIter:
    def __init__(self, vector):
        self.vector = vector
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == len(self.vector):
            raise StopIteration
        else:
            self.index = self.index + 1
            return self.vector[self.index-1]
#LAST \CodeVectorIterLast

class VectorAnim:
    ''' @s: the surface that will be drawn on
        @elms: a list of elements
    '''
    def __init__(self, s):
        self.s = s
        self.v = Vector(0, 0)


    def addElms(self, elm):
        for i, e in enumerate(elm):
            box = IControl(self.s, i * 100, 0, 100, 100, (255, 255, 255), (255, 0, 0), 1)
            box.addText(str(e))
            self.v.add_back(box)

    def addBack(self, elm):
        # TODO: check if a vector exists
        self.v[len(self.v) - 1].bgColor = (255, 255, 255)
        box = IControl(self.s, self.v[len(self.v) - 1].x + 100, 0, 100, 100, (90, 130, 246), (255, 0, 0), 1)
        box.addText(str(elm))
        self.v.add_back(box)
        for b in self.v:
            print(b.bgColor)

    def swap(self, i, j):
        # self.v.swap_idx(i, j)
        self.v[i].bgColor = (0, 255, 0) #Green
        self.v[j].bgColor = (250, 255, 25) #yellow


        temp = self.v[i].x
        self.v[i].x = self.v[j].x
        self.v[j].x = temp

        temp = self.v[i].t
        self.v[i].t = self.v[j].t
        self.v[j].t = temp

        del temp
        for i, a in enumerate(self.v):
            print(self.v[i].t)
            print(self.v[i].bgColor)

    def clear(self):
        self.s.fill((255, 255, 255))

    def draw(self):
        for b in self.v:
            b.draw()
# End class Vector
