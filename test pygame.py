import pygame as pg
pg.init()

win = pg.display.set_mode((500,480))
pg.display.set_caption('First game')

walkRight = [pg.image.load('picture/R1.png'), pg.image.load('picture/R2.png'), pg.image.load('picture/R3.png'), pg.image.load('picture/R4.png'),
			 pg.image.load('picture/R5.png'), pg.image.load('picture/R6.png'), pg.image.load('picture/R7.png'), pg.image.load('picture/R8.png'),
             pg.image.load('picture/R9.png')]
walkLeft = [pg.image.load('picture/L1.png'), pg.image.load('picture/L2.png'), pg.image.load('picture/L3.png'), pg.image.load('picture/L4.png'),
            pg.image.load('picture/L5.png'), pg.image.load('picture/L6.png'), pg.image.load('picture/L7.png'), pg.image.load('picture/L8.png'),
            pg.image.load('picture/L9.png')]
bg = pg.image.load('picture/bg.jpg')
char = pg.image.load('picture/standing.png')

clock = pg.time.Clock()

x,y,width,height,vel = 50,425,64,64,5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0


def redrawGameWindow():
	global walkCount
	win.blit(bg,(0,0))

	if walkCount+1 >= 27:
		walkCount = 0
	if left:
		win.blit(walkLeft[walkCount//3], (x,y))
		walkCount+=1
	elif right:
		win.blit(walkRight[walkCount//3], (x, y))
		walkCount += 1
	else:
		win.blit(char,(x,y))
	pg.display.update()


# MainLoop
run = True
while run:
	clock.tick(27)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

# Use Keyboar keys
	keys = pg.key.get_pressed()
	if keys[pg.K_LEFT] and x>vel:
		x -= vel
		left = True
		right = False
	elif keys[pg.K_RIGHT] and x < 500-width-vel:
		x += vel
		left = False
		right = True
	else:
		right = False
		left = False
		walkCount = 0

	if not(isJump):
		if keys[pg.K_SPACE]:
			isJump = True
			right = False
			left = False
			walkCount = 0
	else:
		if jumpCount>=-10:
			neg = 1
			if jumpCount<0:
				neg = -1
			y-=(jumpCount**2)*0.5*neg
			jumpCount-=1
		else:
			isJump = False
			jumpCount = 10
	redrawGameWindow()
pg.quit()
