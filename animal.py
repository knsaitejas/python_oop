class Animal(object):
	def __init__(self,name,health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def display_health(self):
		print self.health
		return self


class Dog(Animal):
	def __init__(self,name):
		self.name = name
		self.health = 150
	def pet(self):
		self.health += 5
		return self

bobby = Dog('bobby')

# bobby.display_health()

bobby.walk().walk().pet().display_health()

print bobby






































# class Animal(object):
# 	def __init__(self,name,health):
# 		self.name = name
# 		self.health = health
# 	def walk (self):
# 		self.health -=1 
# 		return self
# 	def run (self):
# 		self.health +=5
# 		return self
# 	def display_health (self):
# 		print self.health
# 		return self

# bat = Animal('dogo',10)
# bird = Animal('kitty',10)

# # print bat.walk().walk().walk().run().run().display_health()

# class Dog(Animal):
# 	def __init__(self,name,health=150):
# 		super(Dog,self).__init__(name,health) 
# 		# self.health = 150
# 	def pet (self):
# 		self.health += 5
# 		return self

# # bobby = Dog('bobby')



# class Dragon(Animal):
# 	def __init__(self,name,health=170):
# 		super(Dragon,self).__init__(name,health)
# 	def fly (self):
# 		self.health += 10
# 		return self
# 	def display_health(self):
# 		super(Dragon,self).display_health()
# 		print 'I am a dragon'

# drago = Dragon('drago')
# drago.fly().fly()
# # print drago.health

# queen = Dragon('QUEEN')


