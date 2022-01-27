import sys, pygame
import random

pygame.init()
size = width, height = 1000, 1000
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)

class Vector:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    
    def draw(self):
        pygame.draw.line(screen, self.color, (500, 500), (self.x, self.y))
        pygame.draw.circle(screen, self.color, (self.x, self.y), 2)

class Generator:
    def __init__(self):
        self.randomvectors()
        self.drawvectors()

    def drawvectors(self):
        self.va.draw()
        self.vb.draw()

    def randomvectors(self):
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        x = random.randint(250, 750)
        y = random.randint(250, 750)
        self.va = Vector(color, x, y)

        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        x = random.randint(250, 750)
        y = random.randint(250, 750)
        self.vb = Vector(color, x, y)

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

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            screen.fill(black)
            if event.key == pygame.K_KP_1:
                Generator()
                

    rowsandcols()
    pygame.display.update()

    pygame.display.flip()