import numpy as np

#Classe permettant de faire des opérations sur des matrices de grande taille
class Operation():
	#Ne fait rien
	def __init__(self):
		pass

	#Permet d'obtenir une matrice correspondant a matrice1-matrice2
	#avec tous les résultats supérieurs ou égaux à 0
	#@param im1 : image (liste de liste)
	#@param im2 : image (liste de liste)
	#@return image : image (liste de liste)
	def minus(self, im1, im2):
		i1 = np.array(im1)
		i2 = np.array(im2)
		im = i1 - i2
		i = im > 0
		im = im * i
		return im.tolist()

	#Permet d'ajouter une constante à toute les valeurs d'une matrice
	#@param image : image (liste de liste)
	#@param c : int
	#@return image : image (liste de liste)
	def plus(self, image, c):
		i = np.array(image)
		i = i+c
		return i.tolist()

	#Permet d'obtenir une matrice avec les maximums de chaque matrice
	#@param im1 : image (liste de liste)
	#@param im2 : image (liste de liste)
	#@return image : image (liste de liste)
	def maximum(self, im1, im2):
		i1 = np.array(im1)
		i2 = np.array(im2)
		i = i1>i2 
		i1 = i1 * i
		i = i2>=i1
		i2 = i2 * i
		image = i1 +i2
		return image.tolist()

	#Pour savoir si deux images sont les mêmes
	#@param im1 : image (liste de liste)
	#@param im2 : image (liste de liste)
	#@return boolean
	def egal(self, im1, im2):		
		if(im1 == im2):
			return True
		return False