from Algorithme import Operation as ope
import numpy as np
import cv2

#Classe pour faire des opérations morphologiques (erode, dilate, gradient)
#Utilise les méthodes de la bibliothèque de numpy et cv2
class MorphologiquesOperations():

	#Initialisation où l'on va définir le masque
	#@param bool : boolean
	def __init__(self, bool):
		if(bool):
			self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
		else:
			self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

	#Pour dilater une image
	#@param image : image (liste de liste)
	#@return image dilatée : image (liste de liste)
	def dilate(self, image):
		img = np.array(image, dtype = np.uint8)
		return cv2.dilate(img, self.kernel, iterations = 1)

	#Pour eroder une image
	#@param image : image (liste de liste)
	#@return image erodée : image (liste de liste)
	def erode(self, image):
		img = np.array(image, dtype = np.uint8)
		return cv2.erode(img,self.kernel,iterations = 1)

	#Pour faire le gradient d'une image
	#@param image : image (liste de liste)
	#@param size (nombre de fois que les opérations se font) : int
	#@return image  : image (liste de liste)
	def gradient(self, image, size):
		dil = self.dilate(image)
		ero = self.erode(image)

		i = 1
		while i < size:
			dil = self.dilate(dil)
			ero = self.erode(ero)
			i += 1 
		return ope.Operation().minus(dil, ero)

	#Applique un filtre médian sur l'image
	#@param image : image
	#@return resultat : image
	def median(self,image):
		img = np.array(image, dtype = np.uint8)
		return cv2.medianBlur(img, 3)
