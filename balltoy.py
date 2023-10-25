import random
import pygame
import math
from pygame.math import Vector2
from winsound import Beep

#pygame
pygame.init()
pygame.display.set_caption("ball toy")

Width = 900
Height = 900

screen = pygame.display.set_mode((Width,Height))

#ticks
time = pygame.time.Clock()
ticks = 0

#game variables
bye = False
mPosN = Vector2(0,0)
mPosO = Vector2(0,0)
mXvel = 0
mYvel = 0

toys = []
totaltoys = 4

startpos = Vector2(450-(totaltoys*20),500)


class ball:

    def __init__(self,startpos):
        self.pos = Vector2(startpos)
        self.yVel = 0
        self.xVel = 0
        self.radius = 12
        self.clicked = 0 # value ranging from 0-2, depending on if the mouse has been clicked, and if the click was on the ball
        self.hasSet = False

        #gravity is additive
        self.grav = 0.4
        
        #these are multiplicative
        self.airRes = 0.6 #loss of xVel over time
        self.bml = 0.8 #loss of x/y vel when hitting a wall (x lost on l/r, y lost on t/b)
        self.velConv = 0.5 #loss of velocity after thrown

    def update(self):
        
        if self.pos.x-self.radius<=0: #left wall collision
            self.xVel = abs(self.xVel*self.bml) #sets ball X velocity to positive (rightwards)
            #i use absolute value here because, if the ball clips far enough to the wall, it wont get stuck in a loop of xVel swapping between Negative and Positive
        
        if self.pos.x+self.radius>=Width: #right wall collision
            self.xVel= -abs(self.xVel*self.bml) #sets ball X velocity to negative (leftwards)
        

        if self.pos.y-self.radius<=0: #top ceiling collision
            self.yVel = abs(self.yVel*self.bml) #sets ball Y velocity to positive (downwards)

        if self.pos.y+self.radius>=Height: #bottom floor collision
            self.yVel= -abs(self.yVel*self.bml) #sets ball Y velocity to negative (upwards)


        if self.clicked != 2: #only applied gravity and air resistance when not held by mouse

            if self.pos.x+self.radius <Width-2 or self.pos.x-self.radius > 2: #does apply airRes when ball is in contact with wall
                self.xVel*self.airRes

            if self.pos.y+self.radius < Height: #only applies when not touching the floor
                self.yVel+=self.grav

            if self.pos.y+self.radius>=Height and abs(self.pos.y)<=self.grav: #sets yVel to 0 when touching the floor and when abs yVel is less than grav
                self.yVel=0
        
        #adding Velocity to Position so the ball moves
        self.pos.x += self.xVel
        self.pos.y += self.yVel

    def clickedon(self):
        self.clicked = 1

    def clickedoff(self):
        if self.clicked == 2:
            self.xVel = mXvel*self.velConv
            self.yVel = mYvel*self.velConv
        self.hasSet = False
        self.clicked = 0

    def collide(self):
        if math.sqrt((mPosO.x-self.pos.x)**2 + (mPosO.y-self.pos.y)**2)<self.radius*3:
            if self.clicked != 0:
                if self.hasSet == False:
                    self.pos = mPosO
                    self.hasSet = True
                self.xVel = 0
                self.yVel = 0

                self.xVel = mXvel
                self.yVel = mYvel
                self.clicked = 2
        else:
            self.clicked = 0


    def draw(self):
        pygame.draw.circle(screen, (255,255,240),self.pos,self.radius)

for i in range(totaltoys):
    toys.append(ball(startpos))
    startpos.x+=50

tester = 0

while bye == False:

    time.tick(240)
    tester+=1
    if tester == 4:
        mPosN = Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        mXvel = mPosN.x - mPosO.x
        mYvel = mPosN.y - mPosO.y
        #print(f"X {mXvel}")
        #print(f"Y {mYvel}")
        for i in range(totaltoys):
            toys[i].collide()
        mPosO = mPosN


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bye = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(totaltoys):
                    toys[i].clickedon()
                
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(totaltoys):
                    toys[i].clickedoff()


        for i in range(totaltoys):
            toys[i].update()
        tester = 0
    screen.fill((0,0,0))
    for i in range(totaltoys):
        toys[i].draw()

    
    pygame.display.flip()


pygame.quit()