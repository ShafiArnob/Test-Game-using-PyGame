import pygame as pg
pg.init()

win = pg.display.set_mode((500,480))
pg.display.set_caption('First game')

walkRight = [pg.image.load('picture/R1.png'), pg.image.load('picture/R2.png'), pg.image.load('picture/R3.png'), pg.image.load('picture/R4.png'),pg.image.load('picture/R5.png'), pg.image.load('picture/R6.png'), pg.image.load('picture/R7.png'), pg.image.load('picture/R8.png'),pg.image.load('picture/R9.png')]
walkLeft = [pg.image.load('picture/L1.png'), pg.image.load('picture/L2.png'), pg.image.load('picture/L3.png'), pg.image.load('picture/L4.png'),pg.image.load('picture/L5.png'), pg.image.load('picture/L6.png'), pg.image.load('picture/L7.png'), pg.image.load('picture/L8.png'),pg.image.load('picture/L9.png')]
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
		self.standing = True
	
	def draw(self,win):
		if self.walkCount+1 >= 27:
			self.walkCount = 0
		if not(self.standing):
			if self.left:
				win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
			elif self.right:
				win.blit(walkRight[self.walkCount//3], (self.x, self.y))
				self.walkCount += 1
		else:
			if self.right:
				win.blit(walkRight[0],(self.x,self.y))
			else:
				win.blit(walkLeft[0],(self.x,self.y))

class projectlile(object):
	def __init__(self,x,y,radius,color,facing):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 10 * facing
	def draw(self,win):
		pg.draw.circle(win,self.color,(self.x,self.y),self.radius)

class enemy(object):
	walkRight = [pg.image.load('picture/R1E.png'), pg.image.load('picture/R2E.png'), pg.image.load('picture/R3E.png'), pg.image.load('picture/R4E.png'),pg.image.load('picture/R5E.png'), pg.image.load('picture/R6E.png'), pg.image.load('picture/R7E.png'), pg.image.load('picture/R8E.png'),pg.image.load('picture/R9E.png'), pg.image.load('picture/R10E.png'), pg.image.load('picture/R11E.png')]
	walkLeft = [pg.image.load('picture/L1E.png'), pg.image.load('picture/L2E.png'), pg.image.load('picture/L3E.png'),pg.image.load('picture/L4E.png'), pg.image.load('picture/L5E.png'), pg.image.load('picture/L6E.png'),pg.image.load('picture/L7E.png'), pg.image.load('picture/L8E.png'),pg.image.load('picture/L9E.png'),pg.image.load('picture/L10E.png'), pg.image.load('picture/L11E.png')]
	def __init__(self,x,y,width,height,end):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.end = end
		self.path = [self.x,self.y]
		self.walkCount = 0
		self.vel = 3

	def draw(self,win):
		self.move()
		if self.walkCount+1>=33: # BC 11 images of enemy
			self.walkCount = 0
		if self.vel>0:
			win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
			self.walkCount+=1
		else:
			win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
			self.walkCount+=1

	def move(self):
		if self.vel>0:
			if self.x+self.vel<self.path[1]:
				self.x+=self.vel
			else:
				self.vel = self.vel*-1
				self.walkCount = 0
		else:
			if self.x - self.vel>self.path[0]:
				self.x+=self.vel
			else:
				self.vel = self.vel*-1
				self.walkCount = 0

	
def redrawGameWindow():
	#global walkCount
	win.blit(bg,(0,0)) # Background
	man.draw(win)
	goblin.draw(win)
	for bullet in bullets: # Bullets
		bullet.draw(win)	
	pg.display.update()


# MainLoop
man = player(300,410,64,64)
goblin = enemy(100,410,64,64,450)
bullets = []
run = True
while run:
	clock.tick(27)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
	# Bullets 
	for bullet in bullets:
		if bullet.x<500 and bullet.x>0:
			bullet.x+=bullet.vel
		else:
			bullets.pop(bullets.index(bullet))
	# Use Keyboard keys
	keys = pg.key.get_pressed()
	if keys[pg.K_SPACE]:
		if man.left:
			facing = -1
		else:
			facing = 1

		if len(bullets)<5:
			bullets.append(projectlile(round(man.x+man.width//2),round(man.y+man.height//2),2,(0,0,0),facing))
	if keys[pg.K_LEFT] and man.x > man.vel-15:
		man.x -= man.vel
		man.left = True
		man.right = False
		man.standing = False
	elif keys[pg.K_RIGHT] and man.x < 510-man.width-man.vel:
		man.x += man.vel
		man.left = False
		man.right = True
		man.standing = False
	else:
		man.standing = True
		man.walkCount = 0

	if not(man.isJump):
		if keys[pg.K_UP]:
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
