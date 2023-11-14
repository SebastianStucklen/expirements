import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

possum = pygame.image.load('possumsprite6.png') #load your spritesheet
#Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
xpos = 508 #xpos of player
ypos = 500 #ypos of player
ground = 508
isOnGround = True
vx = 0 #x velocity of player
vy = 0
keys = [False, False, False, False, False] #this list holds whether each key has been pressed
whatdoing = "walk"
landTick = 0
direction = 1
#animation variables variables
frameWidth = 249
frameHeight = 100


RowNum = 1 #for left animation, this will need to change for other animations

frameNum = 0

ticker = 0


walkFrame = [2,1,0,1]
sprintFrame = [2,3,3]
crawlFrame = [0,1]

standFrame = [1,1,1,1,1,1,1,3]
standRow = [RowNum,RowNum,RowNum,RowNum+3,RowNum,RowNum,RowNum,RowNum+3]




while not gameover:
	clock.tick(60) #FPS
	
	if ypos < ground:
		isOnGround = False
	elif ypos >= ground:
		isOnGround = True
		if ypos > ground:
			ypos = ground

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			gameover = True
	  
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				keys[0]=True
			if event.key == pygame.K_RIGHT:
				keys[1]=True
			if event.key == pygame.K_UP or event.key == pygame.K_x or event.key == pygame.K_k or event.key == pygame.K_w:
				keys[2]=True
			if event.key == pygame.K_DOWN or event.key == pygame.K_z or event.key == pygame.K_l or event.key == pygame.K_s:
				keys[3] = True
			if event.key == pygame.K_LSHIFT or event.key == pygame.K_c or event.key == pygame.K_j:
				keys[4] = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				keys[0]=False
			if event.key == pygame.K_RIGHT:
				keys[1]=False
			if event.key == pygame.K_UP or event.key == pygame.K_x or event.key == pygame.K_k or event.key == pygame.K_w:
				keys[2]=False
			if event.key == pygame.K_DOWN or event.key == pygame.K_z or event.key == pygame.K_l or event.key == pygame.K_s:
				keys[3] = False
			if event.key == pygame.K_LSHIFT or event.key == pygame.K_c or event.key == pygame.K_j:
				keys[4] = False
		  

	if keys[3] == True:
		if isOnGround == True:
			whatdoing = "squat"

	elif keys[3] == False:
		if isOnGround == True and whatdoing != "walk" and whatdoing != "land":
			whatdoing = "stand"


	if keys[0]==True:
		if whatdoing != "squat" and isOnGround == True:
			whatdoing = "walk"
		elif whatdoing == "squat":
			whatdoing = "crawl"
		if keys[4] == True:
			if whatdoing != "jump":
				whatdoing = "sprint"
			if vx > -12:
				vx-=0.6
			else:
				vx = -12
		else:
			#whatdoing = "walk"
			if vx < -3:
				vx += 0.5
			else:
				vx= -3
		direction = 1

	elif keys[1] == True:
		if whatdoing != "squat" and isOnGround == True:
			whatdoing = "walk"
		elif whatdoing == "squat":
			whatdoing = "crawl"

		if keys[4] == True:
			if whatdoing != "jump":
				whatdoing = "sprint"
			if vx < 12:
				vx+=0.6
			else:
				vx = 12
		else:
			#whatdoing = "walk"
			if vx > 3:
				vx -= 0.5
			else:
				vx= 3
		direction = 0


	else:
		if whatdoing != "land" and whatdoing != "squat" and isOnGround == True:
			whatdoing = "stand"
		if isOnGround == False:
			if abs(vx) != 0:
				vx*=0.98
			if abs(vx)<=0.2:
				vx = 0

	if keys[2] == True:
		whatdoing = "jump"
		#vyscale*=1.01
	#print(vyscale)


	
		

	if isOnGround == False:
		whatdoing = "jump"
		vy += 0.4
	elif isOnGround == True:
		if vy > 0:
			if keys[0] == False and keys[1] == False and keys[2] == False:
				whatdoing = "land"
			else:
				if keys[4] == True:
					whatdoing = "sprint"
				else:
					whatdoing = "walk"
		vy = 0

	# LAND --------------------------------------------------------------------
	if whatdoing == "land":
		vyscale=8
		landTick += 1
		#print(vx)
		vx*=0.96
		if landTick == 60:
			landTick = 0
			whatdoing = "stand"
		ypos = ground
	# WALK --------------------------------------------------------------------
	if whatdoing == "walk":
		if direction == 1: #left
			RowNum = 1
		if direction == 0:
			RowNum = 0

		ticker+=1
		if ticker%15==0:
				ticker = 0
				frameNum+=1
		if frameNum >= 4:
			frameNum = 0
	# SPRINT ---------------------------------------------------------------
	if whatdoing == "sprint": 
		if direction == 1: #left
			RowNum = 1
		if direction == 0:
			RowNum = 0

		ticker+=1
		if ticker%12==0:
				ticker = 0
				frameNum+=1
		if frameNum >= 3:
			frameNum = 0
	# STAND --------------------------------------------------------------------
	if whatdoing == "stand":
		if direction == 1:
			RowNum = 1
		else:
			RowNum = 0
		ticker+=1
		if ticker%15==0:
				ticker = 0
				frameNum+=1
		if frameNum == 7:
			RowNum+=3
		if frameNum >= 8:
			frameNum = 0
		if abs(vx) != 0:
			vx*=0.90
		if abs(vx)<=0.2:
			vx = 0
	# JUMP --------------------------------------------------------------------
	if whatdoing == "jump":
		if direction == 1:
			RowNum = 1
		else:
			RowNum = 0
		if isOnGround == True:
			ypos = 499
			vy=-9

	if whatdoing == "squat":
		vx*=0.98
		if direction == 1:
			RowNum = 4
		else:
			RowNum = 3
	if whatdoing == "crawl":
		if direction == 1:
			RowNum = 4
		else:
			RowNum = 3

		ticker+=1
		if ticker%12==0:
				ticker = 0
				frameNum+=1
		if frameNum >= 2:
			frameNum = 0


	xpos+=vx 
	ypos+=vy
	#ANIMATION-------------------------------------------------------------------
	print(isOnGround)
	
	# RENDER--------------------------------------------------------------------------------
	# Once we've figured out what frame we're on and where we are, time to render.
			
	screen.fill((200,210,200)) #wipe screen so it doesn't smear
	pygame.draw.rect(screen, (180,190,180),(0,500+frameHeight,800,500-frameHeight))
	if whatdoing == "jump" or whatdoing == "leap":
		screen.blit(possum, (xpos, ypos), (frameWidth*3, RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "stand":
		screen.blit(possum, (xpos, ypos), (frameWidth*standFrame[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "walk":
		screen.blit(possum, (xpos, ypos), (frameWidth*walkFrame[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "sprint":
		screen.blit(possum, (xpos, ypos), (frameWidth*sprintFrame[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "land":
		screen.blit(possum, (xpos, ypos), (frameWidth*direction, 2*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "crawl":
		screen.blit(possum, (xpos, ypos), (frameWidth*crawlFrame[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "squat":
		screen.blit(possum, (xpos, ypos), (frameWidth, RowNum*frameHeight, frameWidth, frameHeight))

	else:
		whatdoing = "walk"
	pygame.display.flip()#this actually puts the pixel on the screen
	
#end game loop------------------------------------------------------------------------------
pygame.quit()