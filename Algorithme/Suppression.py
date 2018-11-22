import numpy as np

#Classe pour faire la suppression des berges
class sup():
	#Initialisation
	#@param image : image (liste de liste)
	def __init__(self, image):
		self.image = np.asmatrix(image).tolist()
		self.largeur = len(self.image[0])
		self.hauteur = len(self.image)

	#Pour faire la suppression des berges par tous les côtés
	#Nombre de pixels à retirer par bords
	#@param haut : int
	#@param bas : int
	#@param gauche : int
	#@param droite : int
	#@return image : image (liste de liste)
	def suppression(self, haut, bas, gauche, droite):
		img = np.array(self.image)
		i = img == 255

		i = i.tolist()
		for y in range(self.largeur):
			x = 0
			start = False
			while(x < self.hauteur and i[x][y]):
				x += 1
				start = True

			if(start):
				for k in range(haut):
					if(x+k >= self.hauteur):
						continue
					i[x+k][y] = True

			x = self.hauteur-1
			start = False
			while(x >=0 and i[x][y]):
				x -= 1
				start = True

			if(start):
				for k in range(bas):
					if(x-k < 0):
						continue
					i[x-k][y] = True

		for x in range(self.hauteur):
			y = 0
			start = False
			while(y < self.largeur and i[x][y]):
				y += 1
				start = True

			if(start):
				for k in range(gauche):
					if(y+k >= self.largeur):
						continue
					i[x][y+k] = True

			y = self.largeur-1
			start = False
			while(y >=0 and i[x][y]):
				y -= 1
				start = True

			if(start):
				for k in range(droite):
					if(y-k < 0):
						continue
					i[x][y-k] = True

		berge  = np.full((self.hauteur,self.largeur), 255)
		berge = i * berge
		i = np.logical_not(i)
		img = i * img
		img = img + berge
		return img.tolist()

	#Supprime le même nombre de pixel sur chaque côté
	#@param value : int
	#@return image : image (liste de liste)
	def supEgale(self, value):
		return self.sup(value, value, value, value)

	#Supprime les pixels à partir du haut et du bas de l'image
	#@param haut : int
	#@param bas : int
	#@return image : image (liste de liste)
	def supHautBas(self, haut, bas):
		return self.sup(haut, bas, 0, 0)

	#Supprimee les pixels à partir de gauche et de droite
	#@param gauche : int
	#@param droite : int
	#@return image : image (liste de liste)
	def supGaucheDroite(self, gauche, droite):
		return self.sup(0, 0, gauche, droite)