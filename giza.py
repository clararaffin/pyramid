class celda:
	def __init__(self,der,izq):
		self.son_der=der	#hijo derecho
		self.son_izq=izq	#hijo izquierdo
		self.var=0		#padre
	def hacer(self):
		bandera=0
		if(self.var==0):
			if( (self.son_der.var!=0) and (self.son_izq.var!=0) ):		#si los hijos tienen números,
				self.var=self.son_der.var+self.son_izq.val		#guardar en el padre la suma de ellos.
				bandera=1
		else:
			if( (self.son_der.var==0) and (self.son_izq.var!=0) ):		#si el hijo derecho está vacío,
				self.son_der.var=self.var-self.son_izq.var		#se guarda en él la resta entre el padre
				bandera=1						#y el hijo izquierdo.
			
			if( (self.son_der.var!=0) and (self.son_izq.val==0) ):		#si el hijo izquierdo está vacío,
				self.son_izq.var=self.var-self.son_der.var		#se guarda en él la resta entre el padre
				bandera=1						#y el hijo derecho.
		
		bandera=bandera or self.son_der.hacer() or self.son_izq.hacer()		
		return bandera
	def listo(self):
		bandera=1
		if(self.var==0):
			bandera=0
		bandera=bandera or self.son_der.listo() or self.son_izq.listo()		
		return bandera

#falta el tema de la base de la pirámide y mostrar todo
