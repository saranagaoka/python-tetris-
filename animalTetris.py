class Box(Sprite):
	def __init__(self):
		self.image=random.randint(0,11)
	
		self.color=Color(204,204,255)
		self.size=20
		self.position=Vector(random.randint(-5,4)*self.size+self.size/2,100)
		self.isDead=False
		self.time=0
	
	def update(self):
		if (self.position.y<=-90 or self.collide(deadBoxes)):
			if (self.isDead==False):
				self.position.y+=5
				self.isDead=True
				self.color=Color(255,51,204)
				game.add(Box())
				deadBoxes.append(self)
			
		else:
			self.position.y-=2
			if(game.key("down")):
				self.position.y-=2
			self.time+=1
			if (self.time%10==0):
				self.position.y-=self.size
				if(game.key("left")):
					self.position.x-=self.size
				if(game.key("right")):
					self.position.x+=self.size
					
		RemoveBoxes()
	
def RemoveBoxes():
	deadBoxCounter=0
	for box in deadBoxes:
		if (box.position.y<-80):
			deadBoxCounter+=1
	if deadBoxCounter==10:
		for box in deadBoxes:
			if (box.position.y<-80):
				game.remove(box)
				deadBoxes.remove(box)
			else:
				box.position.y-=box.size
	
deadBoxes=[]
game.background=Color(0,0,51)

game.add(Box())
game.start()
