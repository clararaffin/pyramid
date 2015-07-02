v = []

class Cell:
	def __init__(self,pos):
		self.pos = pos
		v[self.pos] = int(raw_input("Ingresa valor de celda " + str(num) + ": "))
		self.hijo_der = self.set_hijo_der()
		self.hijo_izq = self.set_hijo_izq()
	#	self.padre_izq = self.set_Padre_izq()
	#	self.padre_der = self.set_Padre_der()

	def set_hijo_izq(self):
		if (self.pos >= 16 and self.pos <= 21):
			return -1
		else:
			self.v = self.pos + self.subir()
			return self.v


	def set_hijo_der(self):
		if (self.pos >= 16 and self.pos <= 21):
			return -1
		else:
			self.v = self.pos + self.subir() + 1
			return self.v
			
	def subir(self):
		if (self.pos == 1):
			return 1
		elif(self.pos == 2 or self.pos == 3):
			return 2
		elif (self.pos >= 4 and self.pos <= 6):
			return 3
		elif(self.pos >= 7 and self.pos <= 10):
			return 4
		elif(self.pos >= 11 and self.pos <= 15):
			return 5
		else:
			return 6
