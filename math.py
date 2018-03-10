class MD(object):
	def __init__(self):
		self.rsum = 0
	def add(self,*num):
		self.rsum+=sum(num)
		return self
	def subtract(self,*num):
		self.rsum-=sum(num)
		return self
	def display(self):
		print self.rsum
		return self

md = MD()

print md.add(5,[5,5]).display()

# class MD(object):
# 	def __init__(self):
# 		self.rsum = 0
# 	def add(self,*num):
# 		for i in num:
# 			if isinstance(i,int):
# 				self.rsum+=i
# 			else:
# 				for num in i:
# 					self.rsum+=num
# 		return self
# 	def subtract(self,*num):
# 		for i in num:
# 			if isinstance(i,int):
# 				self.rsum-=i
# 			else:
# 				for num in i:
# 					self.rsum-=num
# 		return self
# 	def display_rsum(self):
# 		print self.rsum
# 		return self

# md = MD()

# print md.add(5,[10,5,1]).display_rsum().subtract(1,(5)).display_rsum()
	

