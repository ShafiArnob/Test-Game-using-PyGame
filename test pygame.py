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

class player(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isJump = False
		self.jumpCount = 10
		self.left = False
		self.right = False
		self.walkCount = 0
	
	def draw(self,win):
		if self.walkCount+1 >= 27:
			self.walkCount = 0
		if self.left:
			win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
			self.walkCount += 1
		elif self.right:
			win.blit(walkRight[self.walkCount//3], (self.x, self.y))
			self.walkCount += 1
		else:
			win.blit(char, (self.x, self.y))
# x,y,width,height,vel = 50,425,64,64,5
# isJump = False
# jumpCount = 10
# left = False
# right = False
# walkCount = 0


def redrawGameWindow():
	global walkCount
	win.blit(bg,(0,0))
	man.draw(win)	
	pg.display.update()


# MainLoop
man = player(300,410,64,64)
run = True
while run:
	clock.tick(27)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False

# Use Keyboar keys
	keys = pg.key.get_pressed()
	if keys[pg.K_LEFT] and man.x > man.vel-15:
		man.x -= man.vel
		man.left = True
		man.right = False
	elif keys[pg.K_RIGHT] and man.x < 510-man.width-man.vel:
		man.x += man.vel
		man.left = False
		man.right = True
	else:
		man.right = False
		man.left = False
		man.walkCount = 0

	if not(man.isJump):
		if keys[pg.K_SPACE]:
			man.isJump = True
			man.right = False
			man.left = False
			man.walkCount = 0
	else:
		if man.jumpCount >= -10:
			neg = 1
			if man.jumpCount < 0:
				neg = -1
			man.y -= (man.jumpCount**2)*0.5*neg
			man.jumpCount -= 1
		else:
			man.isJump = False
			man.jumpCount = 10
	redrawGameWindow()
pg.quit()
