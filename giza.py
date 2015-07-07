#Todos los nombres están en coreano porque lo estoy estudiando y quería matar dos pájaros de un tiro

class Sel:
	def __init__(self,oenjjog,gwonli):
		self.son_gwonli=gwonli		#hijo derecho
		self.son_oenjjog=oenjjog	#hijo izquierdo
		self.gabs=0			#padre
	def Abeoji(self,v):
		self.gabs=v
	def Hal(self):
		bangwonlia=False
		if(self.gabs==0):
			if( (self.son_oenjjog.gabs!=0) and (self.son_gwonli.gabs!=0) ):		#si los hijos tienen números,
				self.gabs=self.son_gwonli.gabs+self.son_oenjjog.gabs		#guardar en el padre la suma de ellos.
				bangwonlia=True
		else:
			if( (self.son_oenjjog.gabs==0) and (self.son_gwonli.gabs!=0) ):		#si el hijo izquierdo está vacío,
				self.son_oenjjog.gabs=self.gabs-self.son_gwonli.gabs		#se guarda en él la resta entre el padre
				bangwonlia=True							#y el hijo derecho.
			
			if( (self.son_gwonli.gabs!=0) and (self.son_gwonli.gabs==0) ):		#si el hijo derecho está vacío,
				self.son_gwonli.gabs=self.gabs-self.son_oenjjog.gabs		#se guarda en él la resta entre el padre
				bangwonlia=True							#y el hijo izquierdo.
		
		bangwonlia=bangwonlia or self.son_gwonli.Hal() or self.son_oenjjog.Hal()		
		return bangwonlia
	def Wanlyo(self):
		bangwonlia=True
		if(self.gabs==0):
			bangwonlia=False
		bangwonlia=bangwonlia or self.son_gwonli.Wanlyo() or self.son_oenjjog.Wanlyo()		
		return bangwonlia
	def chein(self):
		return str(self.gabs)
class Beiseu(Sel):
	def __init__(self):
		self.gabs=0
	def Hal(self):
		return False
	def Wanlyo(self): 
		return (self.gabs!=0)

Beiseu0=Beiseu()	#						5_0
Beiseu1=Beiseu()	#					4_0		4_1
Beiseu2=Beiseu()	#				3_0		3_1		3_2
Beiseu3=Beiseu()	#			2_0		2_1		2_2		2_3
Beiseu4=Beiseu()	#		1_0		1_1		1_2		1_3		1_4
Beiseu5=Beiseu()	#	Beiseu0		Beiseu1		Beiseu2		Beiseu3		Beiseu4		Beiseu5
Sel1_0=Sel(Beiseu0,Beiseu1)
Sel1_1=Sel(Beiseu1,Beiseu2)
Sel1_2=Sel(Beiseu2,Beiseu3)
Sel1_3=Sel(Beiseu3,Beiseu4)
Sel1_4=Sel(Beiseu4,Beiseu5)
Sel2_0=Sel(Sel1_0,Sel1_1)
Sel2_1=Sel(Sel1_1,Sel1_2)
Sel2_2=Sel(Sel1_2,Sel1_3)
Sel2_3=Sel(Sel1_3,Sel1_4)
Sel3_0=Sel(Sel2_0,Sel2_1)
Sel3_1=Sel(Sel2_1,Sel2_2)
Sel3_2=Sel(Sel2_2,Sel2_3)
Sel4_0=Sel(Sel3_0,Sel3_1)
Sel4_1=Sel(Sel3_1,Sel3_2)
Sel5_0=Sel(Sel4_0,Sel4_1)

print ("Ingrese los valores de las celdas desde la punta de la pirámide de izq a der y hacia abajo (cero si la celda está vacía):")
print("Celda 1, quinto piso:")
Sel5_0.Abeoji(int(input()))
print("Celda 1, cuarto piso:")
Sel4_0.Abeoji(int(input()))
print("Celda 2, cuarto piso:")
Sel4_1.Abeoji(int(input()))
print("Celda 1, tercer piso:")
Sel3_0.Abeoji(int(input()))
print("Celda 2, tercer piso:")
Sel3_1.Abeoji(int(input()))
print("Celda 3, tercer piso:")
Sel3_2.Abeoji(int(input()))
print("Celda 1, segundo piso:")
Sel2_0.Abeoji(int(input()))
print("Celda 2, segundo piso:")
Sel2_1.Abeoji(int(input()))
print("Celda 3, segundo piso:")
Sel2_2.Abeoji(int(input()))
print("Celda 4, segundo piso:")
Sel2_3.Abeoji(int(input()))
print("Celda 1, primer piso:")
Sel1_0.Abeoji(int(input()))
print("Celda 2, primer piso:")
Sel1_1.Abeoji(int(input()))
print("Celda 3, primer piso:")
Sel1_2.Abeoji(int(input()))
print("Celda 4, primer piso:")
Sel1_3.Abeoji(int(input()))
print("Celda 5, primer piso:")
Sel1_4.Abeoji(int(input()))
print("Celda 1, base:")
Beiseu0.Abeoji(int(input()))
print("Celda 2, base:")
Beiseu1.Abeoji(int(input()))
print("Celda 3, base:")
Beiseu2.Abeoji(int(input()))
print("Celda 4, base:")
Beiseu3.Abeoji(int(input()))
print("Celda 5, base:")
Beiseu4.Abeoji(int(input()))
print("Celda 6, base:")
Beiseu5.Abeoji(int(input()))

haegyeol_eobsi=True
while(haegyeol_eobsi):
  haegyeol_eobsi=Sel5_0.Hal()

if(Sel5_0.Wanlyo()):
	print ("")
	print ("\t"+"\t"+"\t"+"\t"+"\t"+Sel5_0.chein()+"\t"+"\t"+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+"\t"+"\t"+Sel4_0.chein()+"\t"+"\t"+Sel4_1.chein()+"\t"+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+"\t"+Sel3_0.chein()+"\t"+"\t"+Sel3_1.chein()+"\t"+"\t"+Sel3_2.chein()+"\t"+"\t"+"\t")
	print ("")
	print ("\t"+"\t"+Sel2_0.chein()+"\t"+"\t"+Sel2_1.chein()+"\t"+"\t"+Sel2_2.chein()+"\t"+"\t"+Sel2_3.chein()+"\t"+"\t")
	print ("")
	print ("\t"+Sel1_0.chein()+"\t"+"\t"+Sel1_1.chein()+"\t"+"\t"+Sel1_2.chein()+"\t"+"\t"+Sel1_3.chein()+"\t"+"\t"+Sel1_4.chein()+"\t")
	print ("")
	print (Beiseu0.chein()+"\t"+"\t"+Beiseu1.chein()+"\t"+"\t"+Beiseu2.chein()+"\t"+"\t"+Beiseu3.chein()+"\t"+"\t"+Beiseu4.chein()+"\t"+"\t"+Beiseu5.chein())
