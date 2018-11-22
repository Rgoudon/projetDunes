from Algorithme import Pixel as pi
from Algorithme import ListPixel as lp
from Algorithme import Image as imge 
from PIL import Image
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import decimal as dc
import numpy as np

#Classe pour calculer la hauteur d'une dune
class Hauteur():
	#Initialisation du calcul
	#@param separation (image des bordures) : image (liste de liste)
	#@param image (image originale) : image (liste de liste)
	def __init__(self, separation, image, sepOnImage):
		self.separation = separation
		self.image = np.asmatrix(image).tolist()
		self.largeur = len(self.image[0])
		self.hauteur = len(self.image)
		self.sepOnImage = sepOnImage

	#Calcul de la hauteur pour une dune dans une zone donnée
	#@param x : int
	#@param y : int
	#@param valeurPixel : int
	#@return hauteur : int
	def calcul(self, x, y, valeurPixel):
		pile = []
		done = lp.ListPixel()
		maximum = 0
		minimum = 0
		haut = bas = gauche = droite = 0
		if(self.separation[x][y] != 65535):
			maximum = self.image[x][y]
			minimum = self.image[x][y]
			pile.append(pi.Pixel(x, y, 0))
			done.addPixel(pi.Pixel(x, y, 0))
			haut = bas = x
			gauche = droite = y

		while(len(pile) != 0):
			pix = pile.pop(0)
			x = pix.getX()
			y = pix.getY()
			for i in range(-1, 2, 1):
				if(x+i < 0 or x+i >= self.hauteur):
					continue
				for j in range(-1, 2, 1):
					if(y+j < 0 or y+j >= self.largeur or (i+j)%2 == 0):
						continue
					pixel = pi.Pixel(x+i, y+j, 0)
					if(self.separation[x+i][y+j] != 65535 and pixel not in done):
						pile.append(pixel)
						done.addPixel(pixel)
						maximum = max(maximum, self.image[x+i][y+j])
						minimum = min(minimum, self.image[x+i][y+j])
						if(haut>x+i):
							haut = x+i
						if(bas<x+i):
							bas = x+i
						if(gauche>y+j):
							gauche = y+j
						if(droite<y+j):
							droite = y+j

		coord = [] #Coordonnée pour connaître le haut, le bas, la gauche et la droite
		coord.append(haut)
		coord.append(bas)
		coord.append(gauche)
		coord.append(droite)
		maximum = maximum * valeurPixel
		minimum = minimum * valeurPixel
		hauteur = maximum-minimum


		return hauteur, coord

	#Calcul la hauteur de chaque dune sur liiimage sélectionnée
	#@param valeurPixel : int
	def calculAll(self, valeurPixel):
		done = imge.Image()
		done.init2(self.hauteur, self.largeur)
		listHauteur = []
		for pixel in range(done.getSurface()):
			maximum = 0
			minimum = 255
			pile = []
			boolean = False
			moyLongueur = []
			moyLargeur = []

			x = done.getRowFromAbsolutePosition(pixel)
			y = done.getColumnFromAbsolutePosition(pixel)

			if(done.read2(pixel) == 0 and self.separation[x][y] != 65535):
				boolean = True
				pile.append(pixel)
				maximum = self.image[x][y]
				minimum = min(minimum, self.image[x][y])
				done.write2(pixel, 1)

			if(self.separation[x][y] == 65535):
				done.write2(pixel, -1)

			while(len(pile) != 0):
				pix = pile.pop(0)
				x = done.getRowFromAbsolutePosition(pix)
				y = done.getColumnFromAbsolutePosition(pix)
				for i in range(-1, 2, 1):
					if(x+i < 0 or x+i >= self.hauteur):
						continue
					for j in range(-1, 2, 1):
						if(y+j < 0 or y+j >= self.largeur or (i+j)%2 == 0 or done.read1(x+i, y+j) != 0):
							continue

						value = done.getAbsolutePosition(x+i, y+j)
						if(self.separation[x+i][y+j] != 65535):
							pile.append(value)
							done.write2(value, 1)
							maximum = max(maximum, self.image[x+i][y+j])
							minimum = min(minimum, self.image[x+i][y+j])
							moyLongueur.append(x+i)
							moyLargeur.append(y+j)


						else :
							done.write2(value, -1)

			if(boolean):
				if(len(moyLargeur) != 0 and len(moyLongueur) != 0):
					largeur = sum(moyLargeur)/len(moyLargeur)
					longueur = sum(moyLongueur)/len(moyLongueur)
					result = dc.Decimal((maximum-minimum)*valeurPixel)
					resultat = result.quantize(dc.Decimal('.01'), rounding=dc.ROUND_HALF_UP)
					listHauteur.append([largeur, longueur, resultat])

		font = ImageFont.load_default()

		image = np.array(self.sepOnImage)
		image = Image.fromarray(image)

		draw = ImageDraw.Draw(image)

		for obj in listHauteur:
			x = obj[0]
			y = obj[1]
			text = obj[2]
			draw.text((x,y), str(text), font=font)#Ecrit sur l'image

		#Permet d'afficher l'image avec les hauteur dans les zones de dune
		#Cette image ne peut pas être enregistrée, si on le fait l'image dans le dossier est entièrement noire 
		image.show()
		image.close()
		#image.save("hauteur.png")
