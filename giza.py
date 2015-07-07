class Celda:
	def __init__(self,der,izq):
		self.son_der=der	#hijo derecho
		self.son_izq=izq	#hijo izquierdo
		self.var=0		#padre
	def padre(self,v):
		self.var=v
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
	def cadena(self):
		return str(self.var)
class base(Celda):
	def __init__(self):
		self.var=0
	def hacer(self):
		return False
	def listo(self): 
		return (self.var!=0)

base0=base()	#						5_0
base1=base()	#					4_0		4_1
base2=base()	#				3_0		3_1		3_2
base3=base()	#			2_0		2_1		2_2		2_3
base4=base()	#		1_0		1_1		1_2		1_3		1_4
base5=base()	#	base0		base1		base2		base3		base4		base5
celda1_0=Celda(base0,base1)
celda1_1=Celda(base1,base2)
celda1_2=Celda(base2,base3)
celda1_3=Celda(base3,base4)
celda1_4=Celda(base4,base5)
celda2_0=Celda(celda1_0,celda1_1)
celda2_1=Celda(celda1_1,celda1_2)
celda2_2=Celda(celda1_2,celda1_3)
celda2_3=Celda(celda1_3,celda1_4)
celda3_0=Celda(celda2_0,celda2_1)
celda3_1=Celda(celda2_1,celda2_2)
celda3_2=Celda(celda2_2,celda2_3)
celda4_0=Celda(celda3_0,celda3_1)
celda4_1=Celda(celda3_1,celda3_2)
celda5_0=Celda(celda4_0,celda4_1)

print ("Ingrese los valores desde la base de la pirámide de izq a der y hacia arriba (cero si la celda está vacía):")
print("Celda 0, base:")
base0.padre(int(input()))
print("Celda 1, base:")
base1.padre(int(input()))
print("Celda 2, base:")
base2.padre(int(input()))
print("Celda 3, base:")
base3.padre(int(input()))
print("Celda 4, base:")
base4.padre(int(input()))
print("Celda 5, base:")
base5.padre(int(input()))
print("Celda 0, primer piso:")
celda1_0.padre(int(input()))
print("Celda 1, primer piso:")
celda1_1.padre(int(input()))
print("Celda 2, primer piso:")
celda1_2.padre(int(input()))
print("Celda 3, primer piso:")
celda1_3.padre(int(input()))
print("Celda 4, primer piso:")
celda1_4.padre(int(input()))
print("Celda 0, segundo piso:")
celda2_0.padre(int(input()))
print("Celda 1, segundo piso:")
celda2_1.padre(int(input()))
print("Celda 2, segundo piso:")
celda2_2.padre(int(input()))
print("Celda 3, segundo piso:")
celda2_3.padre(int(input()))
print("Celda 0, tercer piso:")
celda2_0.padre(int(input()))
print("Celda 1, tercer piso:")
celda3_1.padre(int(input()))
print("Celda 2, tercer piso:")
celda3_2.padre(int(input()))
print("Celda 0, cuarto piso:")
celda4_0.padre(int(input()))
print("Celda 1, cuarto piso:")
celda4_1.padre(int(input()))
print("Celda 0, quinto piso:")
celda5_0.padre(int(input()))

if(celda5_0.listo()):
	print ("")
	print ("\t"+"\t"+"\t"+"\t"+"\t"+celda5_0.cadena()+"\t"+"\t"+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+"\t"+"\t"+celda4_0.cadena()+"\t"+"\t"+celda4_1.cadena()+"\t"+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+"\t"+celda3_0.cadena()+"\t"+"\t"+celda3_1.cadena()+"\t"+"\t"+celda3_2.cadena()+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+celda2_0.cadena()+"\t"+"\t"+celda2_1.cadena()+"\t"+"\t"+celda2_2.cadena()+"\t"+"\t"+celda2_3.cadena()+"\t"+"\t")
	print ("")
	print ("\t"+celda1_0.cadena()+"\t"+"\t"+celda1_1.cadena()+"\t"+"\t"+celda1_2.cadena()+"\t"+"\t"+celda1_3.cadena()+"\t"+"\t"+celda1_4.cadena()+"\t")
	print ("")
	print (base0.cadena()+"\t"+"\t"+base1.cadena()+"\t"+"\t"+base2.cadena()+"\t"+"\t"+base3.cadena()+"\t"+"\t"+base4.cadena()+"\t"+"\t"+base5.cadena())
