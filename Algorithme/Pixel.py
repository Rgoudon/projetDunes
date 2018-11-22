#Classe où l'on range les informations des pixels
class Pixel():

	#Initialise le pixel avec ses coordonnées et le level dans lequel il se situe
	#@param xCoord : int
	#@param yCoord : int
	#@param level : int
	def __init__(self, xCoor, yCoor, level):
		self.xCoor = xCoor
		self.yCoor = yCoor
		self.level = level

	#Pour obtenir la coordonnée x
	#@return xCoord : int
	def getX(self):
		return self.xCoor

	#Pour obtenir la coordonnée y
	#@return yCoord : int
	def getY(self):
		return self.yCoor

	#Pour obtenir le level du pixel dans le processus
	#@return level : int
	def getLevel(self):
		return self.level

	#Surcharge de l'opérateur == 
	#@param objet : pixel
	#@return boolean
	def __eq__(self, objet):
		if(objet.getX() == self.getX() and objet.getY() == self.getY() and objet.getLevel() == self.getLevel()):
			return True
		return False