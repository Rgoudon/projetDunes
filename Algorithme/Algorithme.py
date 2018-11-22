from Algorithme import MorphologiquesOperations as mp
from Algorithme import Contraintes as cn
from Algorithme import LPE as lpe
from Algorithme import Image as imge
from Algorithme import Transec as tr
from PIL import Image
import numpy as np
import cv2
import time

#Classe permet de lancer l'algorithme de Ligne de Partage des Eaux de Vincent&Soille et d'obtenir tous les résultats
class RunLPE():
	#Initialise toutes les variables nécessaires
	#@param image : image (liste de liste)
	#@param step : int
	def __init__(self, image, step):
		self.temps = time.clock()
		self.image = np.array(image.getImage()).tolist() #Image mis sous forme de liste
		self.imageOrig = image #Pour garder l'image originale
		self.hauteurImage = len(self.image) #Variables pour la hauteur
		self.largeurImage = len(self.image[0]) #Variables pour la largeur
		self.step = step #Nombre ajouté 
		self.lab = 0
		self.separation = 0

	#Fait le gradient de l'image, fait la contrainte de par contraste dessus, puis applique dessus la LPE
	#apres erosion pour trouver les zones
	def process(self):
		mop = mp.MorphologiquesOperations(False)
		gim = mop.gradient(self.image, 2)

		#gim = mop.median(self.image)

		#Se fait quand on veut ajouter un seuil
		if(self.step != 0):
			gim = cn.Contraintes().contraste(gim, self.step)

		self.image = gim

		lp = lpe.LPE(self.image)
		self.lab, self.separation = lp.runLPE()
		
		print(time.clock()-self.temps)

	#Permet d'obtenir l'image des labels 
	#@return label : image (liste de liste)
	def getLab(self):
		return self.lab.getImage()

	#Permet d'obtenir l'image des bordures en noir et blanc
	#@return bordure : image (liste de liste)
	def getBordure(self):
		return self.separation.getImage()

	#Permet d'obtenir l'image des bordures sur l'image de base
	#@return image : image (liste de liste)
	def getSepOnImage(self):
		im = np.array(self.imageOrig.getImage()).tolist()
		image = imge.Image()
		image.init1(im)
		for pixel in range(self.lab.getSurface()):
			vallab = self.lab.read2(pixel)
			newvallab = image.read2(pixel)
			if(vallab == 0):
				newvallab = 0
				image.write2(pixel, newvallab)

		return image.getImage()