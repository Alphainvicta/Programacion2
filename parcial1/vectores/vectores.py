import sys, pygame
import random
from math import sqrt

pygame.init()
size = width, height = 1000, 1000
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
nlist = [250, 300, 350, 400, 450, 550, 600, 650, 700, 750]

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self, x, y):
        mag = sqrt((x**2) + (y**2))
        self.x = x
        self.y = y
        self.normx = (x / mag) 
        self.normy = (y / mag)

class Generator:
    def __init__(self):
        self.randomvectors()

    def randomvectors(self):
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        x = random.choice(nlist)
        y = random.choice(nlist)
        self.vector = Vector(x, y)

def rowsandcols():
    ##cols
    pygame.draw.rect(screen, white, [500, 0, 1, 1000])
    y = 0
    while y <= 1000:
        if y >= 951:
            y = 999
        pygame.draw.rect(screen, white, [490, y, 20, 1])
        y += 50
    ##row
    pygame.draw.rect(screen, white, [0, 500, 1000, 1])
    x = 0
    while x <= 1000:
        if x >= 951:
            x = 999
        pygame.draw.rect(screen, white, [x, 490, 1, 20])
        x += 50

def drawvectors():
    for i in vlist:
        pygame.draw.line(screen, vlist[i].color, (500, 500), (vlist[i].vector.x, vlist[i].vector.y), 3)
        pygame.draw.circle(screen, vlist[i].color, (vlist[i].vector.x, vlist[i].vector.y), 4)

def normaddjust(nv):
    if nv.vector.x > 500 and nv.vector.y > 500:
        nv.vector.x = 500 + (nv.vector.normx * 50)
        nv.vector.y = 500 + (nv.vector.normy * 50)

    if nv.vector.x > 500 and nv.vector.y < 500:
        nv.vector.x = 500 + (nv.vector.normx * 50)
        nv.vector.y = 500 - (nv.vector.normy * 50)
    
    if nv.vector.x < 500 and nv.vector.y > 500:
        nv.vector.x = 500 - (nv.vector.normx * 50)
        nv.vector.y = 500 + (nv.vector.normy * 50)

    if nv.vector.x < 500 and nv.vector.y < 500:
        nv.vector.x = 500 - (nv.vector.normx * 50)
        nv.vector.y = 500 - (nv.vector.normy * 50)

vlist = {"vectora": Generator(), "vectorb": Generator()}


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            screen.fill(black)
            if event.key == pygame.K_KP_1:
                vlist = {"vectora": Generator(), "vectorb": Generator()}

            if event.key == pygame.K_KP_2:
                vlist["norma"] = Generator()
                vlist["norma"].vector.norm(vlist["vectora"].vector.x, vlist["vectora"].vector.y)
                normaddjust(vlist["norma"])

            if event.key == pygame.K_KP_3:
                vlist["normb"] = Generator()
                vlist["normb"].vector.norm(vlist["vectorb"].vector.x, vlist["vectorb"].vector.y)
                normaddjust(vlist["normb"])

    drawvectors()
    rowsandcols()
    pygame.display.update()
    pygame.display.flip()