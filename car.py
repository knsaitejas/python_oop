class makeCar (object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel 
		self.mileage = mileage 
		self.tax()
		self.display_all()
	def tax (self):
		if self.price > 10000:
			self.tax = '.15'
		else:
			self.tax = ".12"
		return self
	def display_all(self):
		print 'price: {}'.format(self.price)
		print 'speed: {}'.format(self.speed)
		print 'fuel: {}'.format(self.fuel)
		print 'mileage: {}'.format(self.mileage)
		print 'tax: {}'.format(self.tax)

civic = makeCar(10000,100,'Full','25mpg') 
tesla = makeCar(75000,200,'Full','350 per charge')
tesla1 = makeCar(75000,200,'Full','350 per charge')
tesla2 = makeCar(75000,200,'Full','350 per charge')
tesla3 = makeCar(75000,200,'Full','350 per charge')
tesla4 = makeCar(75000,200,'Full','350 per charge')

