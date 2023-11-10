import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

Link = pygame.image.load('puss.png') #load your spritesheet
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
landStun = 10
landTick = landStun+1
direction = 1

#animation variables variables
frameWidth = 249
frameHeight = 100
RowNum = 1 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
frameOrder = [1,2,1,0]

while not gameover:
	clock.tick(60) #FPS
	
	for event in pygame.event.get(): #quit game if x is pressed in top corner
		if event.type == pygame.QUIT:
			gameover = True
	  
		if event.type == pygame.KEYDOWN: #keyboard input
			if event.key == pygame.K_LEFT:
				keys[0]=True
			elif event.key == pygame.K_RIGHT:
				keys[1]=True
			elif event.key == pygame.K_UP:
				keys[2]=True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				keys[0]=False
			elif event.key == pygame.K_RIGHT:
				keys[1]=False
			elif event.key == pygame.K_UP:
				keys[2]=False

		  

	#LEFT MOVEMENT
	if keys[0]==True:
		whatdoing = "walk"
		if frameOrder[frameNum] == 1:
			vx=-2.7
		else:
			vx=-3.3
		direction = 1
		RowNum = 1
	#RIGHT MOVEMENT
	if keys[1] == True:
		whatdoing = "walk"
		if frameOrder[frameNum] == 1:
			vx = 2.7
		else:
			vx = 3.3
		direction = 0
		RowNum = 0
	if keys[2] == True:
		whatdoing = "jump"
		if ypos >= 500:
			ypos = 499
		vy=-5
	#turn off velocity
	if keys[0] == False and keys[1] == False and keys[2] == False:
		vx=0
	
		
	#UPDATE POSITION BASED ON VELOCITY
	if ypos < 500:
		vy +=0.4
	elif ypos >= 500:
		if abs(vy)<=0.15:
			vy = 0
		if vy > 0:
			vy = -vy*0.6
			print(vy)
			whatdoing = "land"

	xpos+=vx #update player xpos
	ypos+=vy
	#ANIMATION-------------------------------------------------------------------
		
	# Update Animation Information
	# Only animate when in motion
	if vx != 0: #left animation
		# Ticker is a spedometer. We don't want Link animating as fast as the
		# processor can process! Update Animation Frame each time ticker goes over
		ticker+=1
		if ticker%15==0: #only change frames every 10 ticks
				frameNum+=1
		if frameNum == 4:
			frameNum = 0
		   #If we are over the number of frames in our sprite, reset to 0.
		   #In this particular case, there are 10 frames (0 through 9)
  
	# RENDER--------------------------------------------------------------------------------
	# Once we've figured out what frame we're on and where we are, time to render.
			
	screen.fill((0,0,0)) #wipe screen so it doesn't smear
	if whatdoing == "land":
		screen.blit(Link, (xpos, ypos), (frameWidth*direction, 2*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "walk":
		screen.blit(Link, (xpos, ypos), (frameWidth*frameOrder[frameNum], RowNum*frameHeight, frameWidth, frameHeight))
	elif whatdoing == "jump":
		screen.blit(Link, (xpos, ypos), (frameWidth*3, RowNum*frameHeight, frameWidth, frameHeight))
	else:
		whatdoing = "walk"
	pygame.display.flip()#this actually puts the pixel on the screen
	
#end game loop------------------------------------------------------------------------------
pygame.quit()