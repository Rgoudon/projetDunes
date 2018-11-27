from Algorithme import Algorithme, Suppression
from Algorithme import Image as imge
from Interfaces import ResultatsImage
from tkinter import *
import numpy as np

class CalculLPE(Frame):
	"""Classe de gestion de la fenetre des informations pour le calcul de la LPE. \n
	La classe ResultatsAxes hérite de la classe tkinter Frame. \n
	
	:param fenetre: Objet de la classe frame, fenetre affiché à l'utilisateur. 
	:type fenetre: Frame
	
	:param MonImage: Objet de la classe ImageDune contenant le fichier image.
	:type MonImage: ImageDune
	
	:param ImageAffiche: Objet de la classe PhotoImage issue de la bibliothèque Pillow, contenant l'image à afficher dans la fenetre principale.
	:type ImageAffiche: PhotoImage
	
	:param SeuilDetection: Entier correspondant au seuil de detection des petites dunes en cm.
	:type SeuilDetectionPetiteDune: int
	
	:param bCoupure: Booléen indiquant si une coupure sur l'image à été faite ou non
	:type bCoupure: bool
	"""
	
	def __init__(self, fenetre, monImage, imageAffiche, seuilDetection, bCoupure):
		self.monImage = monImage
		self.miniature = imageAffiche
		self.seuilDetection = seuilDetection
		self.b = bCoupure

		FrameMenu = Frame(fenetre)
		FrameMenu.pack(side=LEFT, fill = BOTH, expand = 1)
		
		FrameInfoImage = Frame(FrameMenu)
		FrameInfoImage.pack(side=TOP)
		Label(FrameInfoImage, text="Seuil : ").grid(row=0, column=0)
		self.saisi = Spinbox(FrameInfoImage, from_=0, to=255, width = 10)
		self.saisi.grid(row=0, column=1, sticky='ew')

		Label(FrameInfoImage, text="Haut : ").grid(row=1, column=0)
		self.haut = Spinbox(FrameInfoImage, from_=0, to=100, width = 10)
		self.haut.grid(row=1, column=1, sticky='ew')
		Label(FrameInfoImage, text=" pixels").grid(row=1, column=3)

		Label(FrameInfoImage, text="Bas : ").grid(row=2, column=0)
		self.bas = Spinbox(FrameInfoImage, from_=0, to=100, width = 10)
		self.bas.grid(row=2, column=1, sticky='ew')
		Label(FrameInfoImage, text=" pixels").grid(row=2, column=3)

		Label(FrameInfoImage, text="Gauche : ").grid(row=3, column=0)
		self.gauche = Spinbox(FrameInfoImage, from_=0, to=100, width = 10)
		self.gauche.grid(row=3, column=1, sticky='ew')
		Label(FrameInfoImage, text=" pixels").grid(row=3, column=3)

		Label(FrameInfoImage, text="Droite : ").grid(row=4, column=0)
		self.droite = Spinbox(FrameInfoImage, from_=0, to=100, width = 10)
		self.droite.grid(row=4, column=1, sticky='ew')
		Label(FrameInfoImage, text=" pixels").grid(row=4, column=3)
		Button(FrameMenu, text='Calcul de la LPE', 
			command = lambda : self.LPE()).pack(side=TOP)

		if(bCoupure):
			self.haut['state'] = 'disabled'
			self.bas['state'] = 'disabled'
			self.gauche['state'] = 'disabled'
			self.droite['state'] = 'disabled'
	
	def LPE(self):
		"""
		Fonction qui crée une nouvelle fenêtre où est affichée l'image résultat. \n
		La fonction est appelée par un bouton. \n
		La fonction utilise l'algorithme de la LPE pour calculer les résultats. cf. ci-après : :func:`AlgorithmeAxe.RunLPE`
		"""
		seuil = int(self.saisi.get())
		haut = int(self.haut.get())
		bas = int(self.bas.get())
		gauche = int(self.gauche.get())
		droite = int(self.droite.get())

		image = self.monImage.getImage()

		sp = Suppression.sup(image)
		img = sp.suppression(haut, bas, gauche, droite)

		imageSup = imge.Image()
		imageSup.init1(img)

		al = Algorithme.RunLPE(imageSup, seuil)
		al.process()

		resultat = al.getSepOnImage()
		bordure = al.getBordure()
		fenTraitementImage = Toplevel()
		
		if(self.b):
			fenTraitementImage.title("Résultat coupure image - Analyse dunes 2018")
		else:
			fenTraitementImage.title("Résultats image complète - Analyse dunes 2018")
		ResultatsImage.ResultatsImage(fenTraitementImage, self.monImage, resultat, bordure, self.miniature, self.seuilDetection)