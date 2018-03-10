class Patient(object):
	def __init__(self,id_num,name,allergies,bed=0):
		self.id_num = id_num
		self.name = name
		self.allergies = allergies

class Hospital(object):
	def __init__(self,name,capacity):
		self.patients = []
		self.name = name
		self.capacity = capacity
	def admit(self,patient):
		if len(self.patients) < self.capacity:
			self.patients.append(patient)
			print 'confirm patient admission'
		else:
			print 'not able to admit'
		return self
	def discharge(self,name):
		for p in self.patients:
			if p.name == name:
				del p
				print 'deleted' 
		return self

Manipal = Hospital('Manipal',2)

# Manipal.admit(Patient('1','bob','none',50))
# Manipal.admit(Patient('1','amy','none',50))
# Manipal.discharge('bob')

bobby = Patient(321,'bobby','no allergies')
print bobby.name
print bobby.bed


