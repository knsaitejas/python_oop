class Bike(object):
	miles = 0
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
	def displayInfo(self):
		print self.miles 
		# return self
	def ride(self):
		self.miles+=10
		print 'riding'
		return self
	def reverse(self):
		if self.miles > 5:
			self.miles -= 5
		else:
			self.miles = 0
		print 'reversing'
		return self
	

bike1 = Bike(100,1000)
bike2 = Bike(500,25)
bike3 = Bike('not expensive','not fast')

bike1.ride().ride().ride().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()