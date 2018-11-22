from Algorithme import ListPixel as lp
import numpy as np

#Classe de l'image
class Image():
	#Initialisation de l'image
	def __init__(self):
		self.image = 0 #Pour garder l'image
		self.largeur = 0 #Largeur de l'image
		self.hauteur =  0 #Hauteur de l'image
		self.surface = 0 #Nombre de pixel (largeur*hauteur)
		self.listPixel = lp.ListPixel() #Liste des pixels

	#Initialisation avec l'image
	#@param image : image (liste de liste) 
	def init1(self, image):
		self.image = image[:]
		self.hauteur = len(image)
		self.largeur = len(image[0])
		self.surface = self.largeur * self.hauteur
		self.listPixel.addPixels(image)

	#Initialisation par la hauteur et la largeur
	#L'image est initialisée à 0, remplie de noir
	#@param h (hauteur) : int
	#@param w (largeur) : int
	def init2(self, h, w):
		self.largeur = w
		self.hauteur = h
		self.surface = w*h
		self.image = np.zeros((h, w)).tolist()

	#Initialisation par la hauteur et la largeur
	#L'image est initialisée à la valeur mise en paramètre
	#@param h (hauteur) : int
	#@param w (largeur) : int
	#@param value : int
	def init3(self, h, w, value):
		self.largeur = w
		self.hauteur = h
		self.surface = w*h
		self.image = np.full((h,w), value).tolist()

	#Obtenir la valeur d'un pixel via sa ligne et sa colonne
	#@param h (hauteur) : int
	#@param w (largeur) : int
	def read1(self, h, w):
		return self.image[h][w]

	#Changer la valeur d'un pixel via sa ligne et sa colonne
	#@param h (hauteur) : int
	#@param w (largeur) : int
	#@param value : int
	def write1(self, h, w, value):
		self.image[h][w] = value

	#Obtenir la valeur d'un pixel via sa position dans la surface
	#@param p (positon) : int
	def read2(self, p):
		return self.image[int(p/self.largeur)][int(p%self.largeur)]

	#Changer la valeur d'un pixel via sa position dans la surface
	#@param p (position) : int
	#@param value : int
	def write2(self, p, value):
		self.image[int(p/self.largeur)][int(p%self.largeur)] = value

	#Obtenir la hauteur
	#@return hauteur : int
	def getHeight(self):
		return self.hauteur

	#Obtenir la largeur
	#@return largeur : int
	def getWidth(self):
		return self.largeur

	#Obtenir la surface
	#@return surface : int
	def getSurface(self):
		return self.surface

	#Obtenir l'image
	#@return image : image (liste de liste)
	def getImage(self):
		return self.image

	#Obtenir la colonne via la position
	#@param p (position) : int
	#@return colonne : int
	def getColumnFromAbsolutePosition(self, p):
		return int(p%self.largeur)

	#Obtenir la ligne via la position
	#@param p (position) : int
	#@return ligne : int
	def getRowFromAbsolutePosition(self, p):
		return int(p/self.largeur)

	#Obtenir la position via la  ligne et la colonne
	#@param row (ligne) : int
	#@param column (colonne) : int
	#@return position : int 
	def getAbsolutePosition(self, row, column):
		return row*self.largeur+column

