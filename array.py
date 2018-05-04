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
        
        
    
            
arr = myArray()
for i in range(0,10):
    arr.append(i)






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
# Used to control the while loop
done = False

# Main loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        # Check for mouse press on button and get the mouse's location when it is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            # Check if a button is clicked
            if button1.collidepoint(mouse_pos) or button2.collidepoint(mouse_pos) or button3.collidepoint(mouse_pos):
                color = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
    
    # Background color
    screen.fill(background)

    pygame.draw.rect(screen, color, button1, 1)
    pygame.draw.rect(screen, color, button2, 1)
    pygame.draw.rect(screen, color, button3, 1)
    button4.draw()

    # Clear the screen each iteration
    pygame.display.flip()
    
    
    
pygame.quit()
