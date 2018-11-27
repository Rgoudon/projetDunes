from tkinter import *
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import numpy as np
from TraitementImage import Coupure, Point, GestionAxes, ImageDune
from Interfaces import CalculLPE

class ImageCoupure(Frame):
	"""Classe de gestion de la coupure sur l'image. \n
	La classe ResultatsAxes hérite de la classe tkinter Frame. \n
	
	:param fenetre: Objet de la classe frame, fenetre affiché à l'utilisateur. 
	:type fenetre: Frame
	
	:param MonImage: Objet de la classe ImageDune contenant le fichier image.
	:type MonImage: ImageDune
	
	:param ImageAffiche: Objet de la classe PhotoImage issue de la bibliothèque Pillow, contenant l'image à afficher dans la fenetre principale.
	:type ImageAffiche: PhotoImage
	
	:param SeuilDetection: Entier correspondant au seuil de detection des petites dunes en cm.
	:type SeuilDetectionPetiteDune: int
	"""
	
	def __init__(self, fenetre, monImage, imageAffiche, seuilDetection):
		self.monImage = monImage.getImage()
		self.resolution = monImage.getResolutionAltitude()
		self.monImageListe = np.asmatrix(self.monImage).tolist()
		self.miniature = imageAffiche
		self.seuilDetection = seuilDetection

		img = np.array(self.monImage)
		img = Image.fromarray(img)

		self.LesAxes = GestionAxes.GestionAxes()

		self.DessinPoint = []
		self.b = True

		self.PointsCanvas = []
		self.LignesCanvas = []

		self.coupure = Coupure.coupure()

		FrameMenu = Frame(fenetre)
		FrameMenu.pack(side=LEFT, fill = BOTH, expand = 1)

		self.Canevas = Canvas(fenetre)
		self.ImageAAfficher = ImageTk.PhotoImage(img)
		self.Canevas.create_image(0,0,anchor=NW,image = self.ImageAAfficher)
		self.Canevas.config(width=img.size[0], height=img.size[1])
		self.Canevas.configure(cursor="crosshair")
		self.Canevas.bind("<Button-1>", self.Calcul)
		self.Canevas.pack()

		Button(FrameMenu, text='Reset', command = lambda : self.reset()).pack(side=TOP)

	#Place un point à l'endroit on l'on appuie. Si quatre points sont placés lance la calcul de la LPE
	def Calcul(self, event):
		"""
		Fonction de tracé de la coupure(rectangle) dans l'image.
		
		.. warning:: 
			20/10/2018 : bug détecté, l'utilisateur peut toujours tracer des points après que la coupure ait été tracée.
			Le bug ne gène pas la fonction qui lance l'algorithme de la LPE avec le premier rectangle tracé.
		"""
		PositionX = event.x
		PositionY = event.y

		x,y = self.coupure.coordonnees(PositionX, PositionY)
		self.DessinPoint.append(Point.Point(x, y))

		self.PointsCanvas.append(
			self.Canevas.create_oval(x-1, y-1, x+1, y+1, fill="red"))
		
		size = len(self.DessinPoint)
		if(size>1):
			self.LignesCanvas.append(
				self.Canevas.create_line(self.DessinPoint[size-2].getCoordonnees(), self.DessinPoint[size-1].getCoordonnees(), fill="red"))
		if(size == 2):
			xTemp1, yTemp1 = self.DessinPoint[0].getCoordonnees()
			xTemp2, yTemp2 = self.DessinPoint[1].getCoordonnees()
			if(xTemp1 == xTemp2):
				self.b = True
			else:
				self.b = False

		if(size == 3):
			x1, y1 = self.DessinPoint[0].getCoordonnees()
			x2, y2 = self.DessinPoint[2].getCoordonnees()

			if(self.b):
				self.DessinPoint.append(Point.Point(x2, y1))
				self.PointsCanvas.append(self.Canevas.create_oval(x2-1, y1-1, x2+1, y1+1, fill="red"))
			else:
				self.DessinPoint.append(Point.Point(x1, y2))
				self.PointsCanvas.append(
					self.Canevas.create_oval(x1-1, y2-1, x1+1, y2+1, fill="red"))
			self.LignesCanvas.append(
				self.Canevas.create_line(self.DessinPoint[3].getCoordonnees(), self.DessinPoint[0].getCoordonnees(), fill="red"))
			self.LignesCanvas.append(
				self.Canevas.create_line(self.DessinPoint[2].getCoordonnees(), self.DessinPoint[3].getCoordonnees(), fill="red"))
			imageResultat = []

			xMin = 0
			xMax = 0
			yMin = 0
			yMax = 0
			
			if(y1<y2):
				yMin = y1
				yMax = y2
			else : 
				yMin = y2
				yMax = y1

			#print(x1, x2, yMin, yMax)

			while(yMin<=yMax):
				imageResultat.append([])
				size = len(imageResultat)
				if(x1<x2):
					xMin = x1
					xMax = x2
				else : 
					xMin = x2
					xMax = x1
				while(xMin<=xMax):
					imageResultat[size-1].append(self.monImageListe[yMin][xMin])
					xMin += 1
				yMin += 1

			ImageAEnvoyee = ImageDune.ImageDune()
			ImageAEnvoyee.setImage(imageResultat)
			ImageAEnvoyee.setResolution(self.resolution)
			fenTraitementImage = Toplevel()
			fenTraitementImage.title("Demande des données - Analyse dunes 2018")
			CalculLPE.CalculLPE(fenTraitementImage, ImageAEnvoyee, self.miniature, self.seuilDetection, True)

	#Efface tous points et traits sur l'image. 
	def reset(self):
		"""
		Fonction qui efface lous les points tracés sur l'image.
		"""
		self.DessinPoint[:] = []
		for ligne in self.LignesCanvas : 
			self.Canevas.delete(ligne)
		self.LignesCanvas[:] = []

		for point in self.PointsCanvas:
			self.Canevas.delete(point)
		self.PointsCanvas[:] = []

		self.coupure = Coupure.coupure()