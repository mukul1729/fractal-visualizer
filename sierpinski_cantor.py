import pygame,math

class draw:
    def __init__(self):
        pygame.init()
        self.run = True
        self.display = pygame.display.set_mode((1280,720))
        self.display.fill((255,255,255))
        x,y = 600,700

def rect(x,y,degree):
    if x<0 or y<0 or x>800 or y>800 or degree<0.1:
        return
    else:
        pygame.draw.rect(display,(0,0,0),(x,y,degree,degree))
        rect(x-degree,y-degree,degree//2) #top left
        rect(x+(3/2)*degree,y-degree,degree//2) #top right
        rect(x-degree,y+(3/2)*degree,degree//2) #bottom left
        rect(x-degree,y+(1/4)*degree,degree//2) # left middle
        rect(x+(3/2)*degree,y+(1/4)*degree,degree//2) # middle right
        rect(x+(3/2)*degree,y+(3/2)*degree,degree//2) # bottom right
        rect(x+(1/4)*degree,y-degree,degree//2)
        rect(x+(1/4)*degree,y+(3/2)*degree,degree//2)
        pygame.display.update()


def circle(x,y,degree):
    if x<0 or y<0 or x>1280 or y>720 or degree<0.1:
        return
    else:
        pygame.draw.circle(display,(0,0,0),(x,y),degree)
        circle(x+degree,y+degree,degree//2)
        circle(x-degree,y-degree,degree//2)
        circle(x+degree,y-degree,degree//2)
        circle(x-degree,y+degree,degree//2)
        pygame.display.update()

def cantor(x,y,degree):
    if degree>=-1:
        pygame.draw.rect(display,(0,0,0),(x,y,degree,20))
        cantor(x,y-30,degree//2 - 1)
        cantor(x+degree//2+1,y-30,degree//2-1)
        pygame.display.update()

def wikiwand(x,y,degree):
    if degree>10:
        pygame.draw.line(display,(0,0,0),(x,y),(x-degree,y-degree),3)
        pygame.draw.line(display,(0,0,0),(x,y),(x+degree,y-degree),3)
        x = x-degree
        y = y-degree
        pygame.draw.line(display,(0,0,0),(x,y),(x,y-degree),3)
        pygame.draw.line(display,(0,0,0),(x,y),(x-degree,y-degree//4),3)
        pygame.display.update()


run = True
display = pygame.display.set_mode((1280,720))
display.fill((255,255,255))
myPoints = [[400,50],[600,200],[800,50]]
x,y = 600,700
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #pygame.draw.line(display,(0,0,0),(x,y),(x,y-200),3)
        pygame.display.update()
        #wikiwand(x,y-200,100)
        rect(30,600,50)
