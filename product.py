print 'you are now viewing file: product.py'

class product (object):
	def __init__(self,price,item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = 'for sale'
		# self.display_all()
	def display_all (self):
		print self.price
		print self.item_name
		print self.weight
		print self.brand
		print self.status
	def sold (self):
		self.status = 'sold'
		return self
	def add_taxes (self,tax):
		print self.price+(self.price*tax)
		return self.price+(self.price*tax)
	def returns (self,reason,box):
		if reason == 'defective':
			self.price = 0
			self.status = 'defective'
		if box == 'y':
			self.status = 'for sale'
		elif box == 'n':
			self.status = 'used'
			self.price = self.price*.8


chair = product(100,'livingroom chair','25lbs','kirkland')
chair.sold()
print chair.status
chair.returns('','n')
print chair.status
print chair.price



