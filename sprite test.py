import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

Link = pygame.image.load('possumsprite4.png') #load your spritesheet
#Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
xpos = 500 #xpos of player
ypos = 500 #ypos of player
ground = 500
isOnGround = True
vx = 0 #x velocity of player
vy = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed
whatdoing = "walk"
landTick = 0
direction = 1

#animation variables variables
frameWidth = 249
frameHeight = 100
RowNum = 1 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
frameOrder = [2,1,0,1]

while not gameover:
	clock.tick(60) #FPS
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			gameover = True
	  
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				keys[0]=True
			if event.key == pygame.K_RIGHT:
				keys[1]=True
			if event.key == pygame.K_UP or event.key == pygame.K_x:
				keys[2]=True
			if event.key == pygame.K_DOWN or event.key == pygame.K_z:
				keys[3] = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				keys[0]=False
			if event.key == pygame.K_RIGHT:
				keys[1]=False
			if event.key == pygame.K_UP or event.key == pygame.K_x:
				keys[2]=False
			if event.key == pygame.K_DOWN or event.key == pygame.K_z:
				keys[3] = False

		  

	if keys[3] == True:
		whatdoing = "squat"
	if keys[0]==True:
		if whatdoing != "squat" and isOnGround == True:
			whatdoing = "walk"
		elif whatdoing == "squat":
			whatdoing = "crawl"
		direction = 1
		vx = -3.8
	elif keys[1] == True:
		if whatdoing != "squat" and isOnGround == True:
			whatdoing = "walk"
		elif whatdoing == "squat":
			whatdoing = "crawl"
		direction = 0
		vx = 3.8
	else:
		if whatdoing != "land" and isOnGround == True:
			whatdoing = "stand"
	if keys[2] == True:
		whatdoing = "jump"

	
		

	if ypos < 500:
		isOnGround = False
		vy +=0.4
	elif ypos >= 500:
		isOnGround = True
		if vy > 0:
			if keys[0] == False and keys[1] == False:
				whatdoing = "land"
			else:
				whatdoing = "walk"
		vy = 0

	
	if whatdoing == "land":
		landTick += 1
		print(vx)
		vx*=0.96
		if landTick == 60:
			landTick = 0
			whatdoing = "stand"
	
	if whatdoing == "walk":
		if direction == 1: #left
			RowNum = 1
			vx = -3.8
		if direction == 0:
			RowNum = 0
			vx = 3.8

		ticker+=1
		if ticker%15==0:
				frameNum+=1
		if frameNum == 4:
			frameNum = 0
		
	if whatdoing == "stand":
		if direction == 1:
			RowNum = 1
		else:
			RowNum = 0
		vx = 0

	if whatdoing == "jump":
		if isOnGround == True:
			ypos = 499
			vy=-8
		if vx > 0:
			vx = 3.5
		if vx < 0:
			vx = -3.5

	xpos+=vx 
	ypos+=vy
	#ANIMATION-------------------------------------------------------------------
		

	
	# RENDER--------------------------------------------------------------------------------
	# Once we've figured out what frame we're on and where we are, time to render.
			
	screen.fill((0,0,0)) #wipe screen so it doesn't smear
	if whatdoing == "jump":
		screen.blit(Link, (xpos, ypos), (frameWidth*3, RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "stand":
		screen.blit(Link, (xpos, ypos), (frameWidth*frameOrder[3], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "walk":
		screen.blit(Link, (xpos, ypos), (frameWidth*frameOrder[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "land":
		screen.blit(Link, (xpos, ypos), (frameWidth*direction, 2*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "crawl":
		screen.blit(Link, (xpos, ypos), (frameWidth*direction, 3*frameHeight, frameWidth, frameHeight))
	else:
		whatdoing = "walk"
	pygame.display.flip()#this actually puts the pixel on the screen
	
#end game loop------------------------------------------------------------------------------
pygame.quit()