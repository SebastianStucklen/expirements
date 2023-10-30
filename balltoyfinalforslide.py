import pygame
import math
from pygame.math import Vector2

#pygame
pygame.init()
pygame.display.set_caption("ball toy")

WIDTH = 900
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Ball:
	def __init__(self, startPos: Vector2):
		self.pos = startPos
		self.vel = Vector2(0,0)
		self.radius = 12
		self.clicked = 0 # value ranging from 0-2, depending on if the mouse has been clicked, and if the click was on the ball
		self.hasSet = False
		
		#gravity is additive
		self.grav = 150
		
		#these are multiplicative
		self.airRes = 2 #loss of xVel over time
		self.friction = 10
		self.bounce = 0.7 #loss of x/y vel when hitting a wall (x lost on l/r, y lost on t/b)
		self.velConv = 1 #loss of velocity after thrown

	def wallCollision(self):
		# i use absolute value here because, if the ball clips far enough to the wall, it wont get stuck in a loop of xVel swapping between Negative and Positive
		if self.pos.x - self.radius <= 0: #left wall collision
			self.vel.x = abs(self.vel.x * self.bounce) #sets ball X velocity to positive (rightwards)
		
		if self.pos.x + self.radius >= WIDTH: #right wall collision
			self.vel.x= -abs(self.vel.x * self.bounce) #sets ball X velocity to negative (leftwards)

		if self.pos.y - self.radius <= 0: #top ceiling collision
			self.vel.y = abs(self.vel.y * self.bounce) #sets ball Y velocity to positive (downwards)

		if self.pos.y + self.radius >= HEIGHT: #bottom floor collision
			self.vel.y = -abs(self.vel.y * self.bounce) #sets ball Y velocity to negative (upwards)

	def update(self, delta: float):
		if self.clicked != 2: #only applied gravity and air resistance when not held by mouse
			# if self.pos.x + self.radius < Width - 2 or self.pos.x - self.radius > 2: #doesn't apply airRes when ball is in contact with wall
			self.vel *= 1 - (self.airRes * delta)

			if self.pos.y + self.radius < HEIGHT: # only applies when not touching the floor
				self.vel.y += self.grav
			else: # applies ground friction when touching ground
				self.vel.x *= 1 - (self.friction * delta)
		
		#adding Velocity to Position so the ball moves
		self.pos += self.vel * delta

	def clickedon(self):
		self.clicked = 1

	def clickedoff(self, mouseVel: Vector2):
		if self.clicked == 2:
			self.vel = mouseVel * self.velConv
		self.hasSet = False
		self.clicked = 0

	def collide(self):
		if math.sqrt((mousePosOld.x-self.pos.x)**2 + (mousePosOld.y-self.pos.y)**2)<self.radius*3:
			if self.clicked != 0:
				#if self.hasSet == False:
				#	self.pos = mPosO
				#	self.hasSet = True
				self.vel = Vector2(0,0)

				self.vel = mouseVel
				self.clicked = 2
		else:
			self.clicked = 0


	def draw(self):
		pygame.draw.circle(screen, (255, 255, 240), self.pos, self.radius)


#ticks
time = pygame.time.Clock()

#game variables
bye = False
mousePosOld = Vector2(0,0)

toys: "list[Ball]" = []
totaltoys = 1

startpos = Vector2(WIDTH/2-(totaltoys*20),HEIGHT/2)

for i in range(totaltoys):
	toys.append(Ball(startpos))
	startpos.x+=50

everyFour = 0
mouseVels: list[Vector2] = []
while bye == False:

	delta = time.tick(240) / 1000
	everyFour+=1
	if everyFour == 4:
		mousePosNew = Vector2(pygame.mouse.get_pos())
		#pygame.mouse.get_pressed()
		mouseVel = (mousePosNew - mousePosOld) / delta

		# average out the last few mouse velocities
		if len(mouseVels) < 4:
			mouseVels.append(mouseVel)
		else:
			mouseVels.pop(0)
			mouseVels.append(mouseVel)

		avgVel = Vector2(0, 0)
		for vel in mouseVels:
			avgVel += vel
		avgVel /= len(mouseVels)

		
		for i in range(totaltoys):
			toys[i].collide()
		mousePosOld = mousePosNew


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				bye = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				for i in range(totaltoys):
					toys[i].clickedon()
				
			if event.type == pygame.MOUSEBUTTONUP:
				for i in range(totaltoys):
					toys[i].clickedoff(avgVel)


		for i in range(totaltoys):
			toys[i].wallCollision()
			toys[i].update(delta)
		everyFour = 0
	screen.fill((0,0,0))
	for i in range(totaltoys):
		toys[i].draw()

	
	pygame.display.flip()


pygame.quit()