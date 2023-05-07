class Ventana:
	__titulo = ""
	__vsix = 0
	__vsiy = 0
	__vidx = 0
	__vidy = 0

	def __init__ (self,titulo,vsix = 0,vsiy =0 ,vidx = 500,vidy = 500):
		self.__titulo = titulo
		self.__vsix = vsix
		self.__vsiy = vsiy
		self.__vidx = vidx
		self.__vidy = vidy

	def getTitulo(self):
		return self.__titulo

	def alto(self):
		return self.__vsix,self.__vsiy

	def ancho(self):
		return self.__vidx,self.__vidy

	def mostrar(self):
		print(self.__titulo)
		print('VSI x:{} --- VSI y:{} '.format(self.__vsix, self.__vsiy))
		print('VID x:{} --- VID y:{} '.format(self.__vidx, self.__vidy))

	def moverDerecha(self,num=1):
		self.__vidy = self.__vidy + num
		self.__vsiy = self.__vsiy + num


	def moverIzquierda(self,num=1):
		self.__vidy = self.__vidy - num
		self.__vsiy = self.__vsiy - num

	def subir(self,num=1):
		self.__vsix = self.__vsix + num
		self.__vidx = self.__vidx + num

	def bajar(self,num=1):
		self.__vsix = self.__vsix - num
		self.__vidx = self.__vidx - num
