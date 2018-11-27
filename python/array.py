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

# NOTE:
# we can draw rect without having to use an extra surface, however the reason a surface is used is because we want to fill the background
# of the rect however we want while keeping border (rect itself has no background fill property and if we want to fill the background we have
# to sacrifice border)

# TODO: refactor code:
# 1: make a base class for all the controls that has a contructor and a draw function
# 2: Button class can be derived from label which is derived from base class with click functionality
# 3: TextBox class can also be derived from Label class
class Control:
    """Parent class for all the controls"""
    def __init__(self, window, *args, **kwargs):
        # The window (screen) that will be drawn on
        self.window : window
        self.x : 100
        self.y : 100
        self.w : 200
        self.h : 200
        self.backgroundColor : [255, 255, 25]
        self.borderColor : [0, 255, 0]
        self.borderThickness : 1
        self.rect : pygame.Rect(self.x, self.y, self.w, self.h)
        self.surface : pygame.Surface((self.w, self.h))
        #self.surface.fill(self.backgroundColor)



class Button():
    def __init__(self, window):
        # The window (screen) that will be drawn on
        self.window = window
        self.x = 100;
        self.y = 100;
        self.w = 200;
        self.h = 200;
        self.backgroundColor = [255, 255, 25]
        self.borderColor = [0, 255, 0]
        self.borderThickness = 1
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
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
            #if(mouseX >= self.x and mouseX <= self.x + self.w and mouseY >= self.y and mouseY <= self.y + self.h) :
            if(self.rect.collidepoint((mouseX, mouseY))):
                callback(*args, **kwargs)

    def draw(self):
        # Draw a rect on top of self.surface at position (0,0) relative to the self.surface.  It is different than the self.rect declared above
        self.window.blit(self.surface, (self.x, self.y))
        pygame.draw.rect(self.surface, self.borderColor, [0, 0, self.w, self.h], self.borderThickness)
# End class button

# Textbox
class TextBox:
    def __init__(self, window):
        self.window = window
        self.x = 200;
        self.y = 0;
        self.w = 100
        self.h = 50
        self.backgroundColor = [255, 255, 25]
        self.borderColor = [0, 255, 0]
        self.borderThickness = 1
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.surface = pygame.Surface((self.w, self.h))
        self.surface.fill(self.backgroundColor)
        self.active = False
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.text_surface = self.font.render(self.text, True, (255, 0 , 100))


    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                print(self.active)
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                # When return key is pressed
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                # Delete character
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                # To clear the text or delete character when users press backspace, we fill the surface first with a solid color
                self.surface.fill(self.backgroundColor)
                # Then we update the surface with text
                self.text_surface = self.font.render(self.text, True, (255, 0, 10))

    def draw(self):
        self.window.blit(self.surface, (self.x, self.y))
        pygame.draw.rect(self.surface, self.borderColor, [0, 0, self.w, self.h], self.borderThickness)
        self.surface.blit(self.text_surface, (0, 0))
# End class TextBox

# Label
class Label:
    def __init__(self, window):
        self.window = window
        self.x = 200;
        self.y = 0;
        self.w = 100
        self.h = 50
        self.backgroundColor = [255, 255, 25]
        self.borderColor = [0, 255, 0]
        self.borderThickness = 1
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.surface = pygame.Surface((self.w, self.h))
        self.surface.fill(self.backgroundColor)
        self.active = False
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.text_surface = self.font.render(self.text, True, (255, 0 , 100))


    def draw(self):
        self.window.blit(self.surface, (self.x, self.y))
        pygame.draw.rect(self.surface, self.borderColor, [0, 0, self.w, self.h], self.borderThickness)
        self.surface.blit(self.text_surface, (0, 0))


size = [1200,800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Testing with draw module")
background = (255, 255, 255)
color = [243, 183, 198]

button1 = pygame.Rect(0,0, 100, 50)
button2 = pygame.Rect(0,button1.y + 60, 100, 50)
button3 = pygame.Rect(0,button2.y + 60, 100, 50)
button4 = Button(screen)
button4.addText("Hello")
input1 = TextBox(screen)

# Used to control the while loop
done = False
screen.fill(background)
# Main loop
while not done:
    for event in pygame.event.get():
        button4.click(event, lambda x, y, z: print(x + y + z), 10, 2, 30)
        input1.handle(event)
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
    input1.draw()
    # Clear the screen each iteration
    pygame.display.flip()



pygame.quit()
