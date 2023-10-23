import random
import pygame
import math
from pygame.math import Vector2
from winsound import Beep

#pygame
pygame.init()
pygame.display.set_caption("ball toy")
screen = pygame.display.set_mode((900,900))

#ticks
time = pygame.time.Clock()
ticks = 0

bye = False
mPosN = Vector2(0,0)
mPosO = Vector2(0,0)
mXvel = 0
mYvel = 0
startpos = Vector2(450,800)


class ball:

    def __init__(self,startpos,radius):
        self.pos = Vector2(startpos)
        self.yVel = 0
        self.xVel = 0
        self.radius = radius
        self.clicked = False

    def update(self):
        self.pos.x -= self.xVel
        self.pos.y -= self.yVel
    
        if self.pos.x+self.radius >= 900 and self.pos.y > 0+self.radius and self.pos.y < 900-self.radius:
            self.xVel= -self.xVel


        #top
        if self.pos.y-self.radius <= 0 and self.pos.x >= 0+self.radius and self.pos.x <= 900-self.radius:
            self.yVel= -self.yVel

        #left
        if self.pos.x-self.radius <= 0 and self.pos.y > 0+self.radius and self.pos.y < 900-self.radius:
            self.xVel= -self.xVel 


        #bottom
        if self.pos.y+self.radius >= 900 and self.pos.x > 0+self.radius and self.pos.x < 900-self.radius:
            self.yVel= -self.yVel
    def clickedon(self):
        self.clicked = True
    def clickedoff(self):
        self.clicked = False
    def collide(self,mouseX,mouseY):
        if math.sqrt((mouseX-self.pos.x)**2 + (mouseY-self.pos.y)**2)<self.radius*1.5:
            if self.clicked == True:
                self.pos.x = mouseX
                self.pos.y = mouseY

    def draw(self):
        pygame.draw.circle(screen, (255,255,255),self.pos,self.radius)

toy = ball(startpos,10)

while bye == False:

    time.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bye = True

        if event.type == pygame.MOUSEMOTION: #check if mouse moved
            mPosN = Vector2(event.pos)
            mXvel = mPosN.x - mPosO.x
            mYvel = mPosN.y - mPosO.y
            print(f"X {mXvel}")
            print(f"Y {mYvel}")
            mPosO = mPosN
            toy.collide(mPosN.x,mPosN.y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            toy.clickedon()
        if event.type == pygame.MOUSEBUTTONUP:
            toy.clickedoff()

    print("test")
    toy.update()
    toy.draw()

    
    pygame.display.flip()


pygame.quit()