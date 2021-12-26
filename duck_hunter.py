import pygame
from random import randint, choice
#from ctypes import *
from math import sin, cos, pi

WIDTH, HEIGHT = 640, 500#windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)

FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 255)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#piu = pygame.image.load('C:\Python\Pygame graphics\пиу.png').convert()

d1 = pygame.image.load('C:\Python\Pygame graphics\duck1.png').convert()

d2 = pygame.transform.flip(d1, True, False)

duck = [d1, d2]

font = pygame.font.SysFont('Arial', 30)

duckappeartime = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5)

ducks = []

dspeed = 5

duckturnv = []

n = pi / 180

n2 = 0 - pi / 2

for i in range(20, 161):
    duckturnv.append(0 - (n * i))

duckdirs = []

duckcoords = []

nextducktime = sum(duckappeartime) / len(duckappeartime)

def calculate_new_xy(x, y, speed, angle_in_radians):
    new_x = x + (speed * cos(angle_in_radians))
    new_y = y + (speed * sin(angle_in_radians))
    return new_x, new_y

def fillscreen():
    screen.fill(BLUE)

def effect(text, size, x, y):
    a = 75
    screen.blit(piu, (x - a / 2, y - a / 2))

def duckappear(x, y):
    global duckcoords, duckdirs
    duckcoords.append([x, y])
    duckdirs.append(choice(duckturnv))
    #print(choice(duckturnv))
    #pygame.draw.rect(screen, YELLOW, (x, y, 120, 90))

def getTime():
    return pygame.time.get_ticks() / 1000

def genNextDuckTime():
    global nextducktime
    nextducktime = choice(duckappeartime) + time

d = duck[0]

while True:
    fillscreen()
    pygame.draw.rect(screen, GREEN, (0, HEIGHT // 1.5, WIDTH, HEIGHT // 2))

    time = getTime()
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                time = time

    for i, s in enumerate(duckcoords):
        #print(s)
        x, y = s[0], s[1]

        if x < (-30) or x > WIDTH or y < (-(45 / 2)):
            duckcoords.pop(i)
            duckdirs.pop(i)
            ducks.pop(i)
            continue
        #print(len(duckcoords))

        print(duckdirs[i], n2)

        if duckdirs[i] > n2:
            d = duck[0]
        if duckdirs[i] < n2:
            d = duck[1]

        ducks.append(d)
        
        screen.blit(ducks[i], (x, y))
        
        duckcoords[i] = calculate_new_xy(x, y, dspeed, duckdirs[i])
    
    if time > nextducktime:
        duckappear(randint(0, WIDTH - 45), randint(HEIGHT // 2, HEIGHT // 1.8))
        genNextDuckTime()

    pygame.display.update()
    clock.tick(FPS)
