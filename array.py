# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:49:58 2018

@author: hympert
"""
import sys
import pygame
import random

pygame.init()

class myArray:
    data = []
    def __init__(self, value = None):
        if value is not None :
            self.data.append(value)

    def append(self, value):
        self.data.append(value)

    def print(self):
        for i in range(0, len(self.data)):
            print('{}'.format(self.data[i]))
# End myArray class

class Button:
    def __init__(self, surface):
        self.surface = surface
        self.color = [0,0,0]
        self.x = 0
        self.y = 0
        self.w = 100
        self.h = 50
        self.border = 0


    def setup(self, color, x, y, w, h, border):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.border = border

    def addText(self, text):
        self.font = pygame.font.SysFont('Arial', 25)
        self.text = self.font.render(text, True, (100,120,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.w/2, self.y + self.h/2)
        self.surface.blit(self.text, self.text_rect)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, [self.x, self.y, self.w, self.h], self.border)

    def click(self, event, callback, *args, **kwargs):
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if(mouseX >= self.x and mouseX <= self.x + self.w and mouseY >= self.y and mouseY <= self.y + self.h) :
                callback(*args, **kwargs)


class testbutton:
    def __init__(self, window):
        self.window = window
        self.x = 100;
        self.y = 100;
        self.w = 200;
        self.h = 200;
        self.backgroundColor = [255, 255, 25]
        self.borderColor = [0, 255, 0]
        self.borderThickness = 1
        # The rect will always be drawn on top of the surface, therefore pos x and pos y are set to be 0, 0
        self.rect = pygame.Rect(0, 0, self.w, self.h)
        self.surface = pygame.Surface((self.w, self.h))
        self.surface.fill(self.backgroundColor)

    def addText(self, text):
        self.font = pygame.font.SysFont('Arial', 25)
        self.text = self.font.render(text, True, (100,120,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.w/2, self.h/2)
        self.surface.blit(self.text, self.text_rect)


    def click(self, event, callback, *args, **kwargs):
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if(mouseX >= self.x and mouseX <= self.x + self.w and mouseY >= self.y and mouseY <= self.y + self.h) :
                callback(*args, **kwargs)

    def draw(self):
        pygame.draw.rect(self.surface, self.borderColor, self.rect, self.borderThickness)
        self.window.blit(self.surface, (100, 100))






arr = myArray()
for i in range(0,10):
    arr.append(i)
    print(i)


def printstuff():
    print("Hello, this is a callback function")
def add(x, y):
    print(x + y)

size = [1200,800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Testing with draw module")
background = (255, 255, 255)
color = [243, 183, 198]

button1 = pygame.Rect(0,0, 100, 50)
button2 = pygame.Rect(0,button1.y + 60, 100, 50)
button3 = pygame.Rect(0,button2.y + 60, 100, 50)
button4 = Button(screen)
button4.setup(color, 0, button3.y + 60, 100, 50, 1)
button4.border = 0
button4.color = [255, 0, 0]

button5 = testbutton(screen)
button5.addText("Hello")
# Used to control the while loop
done = False
screen.fill(background)
button4.addText("Hello")
# Main loop
while not done:
    for event in pygame.event.get():
        button4.click(event, lambda x, y, z: print(x + y + z), 10, 2, 30)
        if event.type == pygame.QUIT:
            done = True

        # Check for mouse press on button and get the mouse's location when it is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Check if a button is clicked
            if button1.collidepoint(mouse_pos) or button2.collidepoint(mouse_pos) or button3.collidepoint(mouse_pos):
                color = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]


    # Background color

    pygame.draw.rect(screen, color, button1, 1)
    pygame.draw.rect(screen, color, button2, 1)
    pygame.draw.rect(screen, color, button3, 1)
    button4.draw()
    button5.draw()
    # Clear the screen each iteration
    pygame.display.flip()



pygame.quit()
