import pygame
import random
pygame.init()
screen = pygame.display.set_mode((300, 300))
player, dir, size = pygame.Rect(100,100,20,20), (0, 0), 20
MOVEEVENT, APPLEEVENT, trail = pygame.USEREVENT+1, pygame.USEREVENT+2, []
pygame.time.set_timer(MOVEEVENT, 250)
pygame.time.set_timer(APPLEEVENT, 1000)
apples=[]
while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: dir = 0, -1
    if keys[pygame.K_a]: dir = -1, 0
    if keys[pygame.K_s]: dir = 0, 1
    if keys[pygame.K_d]: dir = 1, 0

    if pygame.event.get(pygame.QUIT): break
    for e in pygame.event.get():
        if e.type == MOVEEVENT: # this event happens every 250 ms
            trail.append(player.inflate((-10, -10)))
            trail = trail[-5:]
            player.move_ip(*[v*size for v in dir])
        if e.type == APPLEEVENT: # this event happens every 1000 ms
            apples.append(pygame.rect.Rect(random.randint(0, 30) * 10, random.randint(0, 30) * 10, 10, 10))

    screen.fill((0,120,0))
    for t in trail:
        pygame.draw.rect(screen, (255,0,0), t)
    for a in apples:
        pygame.draw.rect(screen, (0,255,100), a)

    pygame.draw.rect(screen, (255,0,0), player)
    pygame.display.flip()
