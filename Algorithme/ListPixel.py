from Algorithme import Pixel as pi

class ListPixel():
	#Initialise les pixels
	def __init__(self):
		self.listPixel = [] #Liste ou le spixels seront rangé par leur valeur
		self.number = 0
		for i in range(256):
			self.listPixel.append([])

	#Ajoute un pixel à la liste
	#@param pixel : Pixel
	def addPixel(self, pixel):
		self.number += 1
		self.listPixel[pixel.getLevel()].append(pixel)

	#Ajoute une liste de pixels
	#@param pixels : image (liste de liste)
	def addPixels(self, pixels):
		for x in range(len(pixels)):
			for y in range(len(pixels[x])):
				self.addPixel(pi.Pixel(x, y, pixels[x][y]))

	#Permet d'afficher tous les  pixels de la liste
	def displayList(self):
		for pixels in self.listPixel:
			for pixel in pixels:
				print(pixel.getLevel(), pixel.getX(), pixel.getY())

	#Permet de savoir le nombre de pixels qui sont à un niveau
	#@param level : int 
	#@return taille : int
	def getNumberOfPixelInLevel(self, level):
		return len(self.listPixel[level])

	#Permet d'obtenir tous les pixels appartenant à un niveau
	#@param level : int
	#@return liste de Pixels 
	def getPixelsByLevel(self, level):
		return self.listPixel[level]

	#Permet de savoir le niveau minimum de la liste
	#@return level min : int
	def getLevelMin(self):
		for i in range(256):
			if(len(self.listPixel[i]) != 0):
				return i

	#Permet de savoir le niveau max de la liste
	#@return level max : int
	def getLevelMax(self):
		for i in range(255, 0, -1):
			if(len(self.listPixel[i]) != 0):
				return i

	#Permet de savoir le nombre de pixels dans la liste
	#@return nombre : int
	def getNumberPixels(self):
		return self.number

	#Pour savoir si le pixel dans la liste
	#@param pixel : pixel
	#@return boolean
	def isIn(self, pixel):
		if(pixel in self.listPixel[pixel.getLevel()]):
			return True
		return False

	#Surcharge de l'opérateur in
	#@param objet : pixel
	#return boolean
	def __contains__(self, objet):
		for pixel in self.listPixel[objet.getLevel()]:
			if(pixel == objet):
				return True
		return False