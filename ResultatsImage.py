from TraitementImage import ImageDune, AlgorithmeImageComplete, ExportTXT
from Algorithme import Hauteur
from Algorithme import Transec as tr
from Algorithme import Image as mge
from Algorithme import Pixel as pi
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from scipy import array, shape
import numpy as np

import time
import copy

from Algorithme import Pixel as pi

import matplotlib.pyplot as plt

#Classe pour afficher l'image résultat après la lpe
class ResultatsImage(Frame):
	"""Classe de gestion de la fenetre des résultats. \n
	La classe ResultatsAxes hérite de la classe tkinter Frame. \n
	
	:param fenetre: Objet de la classe frame, fenetre affiché à l'utilisateur. 
	:type fenetre: Frame
	
	:param origine: ?
	:type origine: ?
	
	:param MonImage: ?
	:type MonImage: ?
	
	:param separation: ?
	:type separation: ?
	
	:param ImageAffiche: Objet de la classe PhotoImage issue de la bibliothèque Pillow, contenant l'image à afficher dans la fenetre principale.
	:type ImageAffiche: PhotoImage
	
	:param SeuilDetection: Entier correspondant au seuil de detection des petites dunes en cm.
	:type SeuilDetectionPetiteDune: int
	"""

	def __init__(self, fenetre, origine = None, MonImage = None, separation = None, ImageAffiche = [0], SeuilDetectionDune = 0):
		
				#ResultatsImage(fenTraitementImage, self.monImage, resultat, bordure, self.miniature, self.seuilDetection)
		self.temps = time.clock()
		self.MonImage = MonImage
		self.ImageAffichage = ImageAffiche
		self.DetectionDune = SeuilDetectionDune
		self.ImageAAfficher = 0 # variable ne pouvant être une variable locale, sinon l'image n'apparaît pas à l'affichage
		self.seuil = 0
		self.miniature = ImageAffiche
		self.image = 0
		self.separation = separation
		self.origine = origine
		
		# Création d'une sous frame pour placer correctement les divers éléments sur la moitié gauche de la fenêtre
		FrameMenu = Frame(fenetre)
		FrameMenu.pack(side=LEFT, fill = BOTH, expand = 1)

		# Création de nos widgets
		Button(FrameMenu, text='Export des résultats', command = lambda : self.ExportTxt()).pack(side=TOP)

		self.FrameTable = Frame(FrameMenu, height=255, width = 255, bd=1, relief=SUNKEN)
		self.FrameTable.pack(side=TOP, fill = BOTH, expand = 1)
		
		self.Table = ttk.Treeview(self.FrameTable, columns=('Nombre', 'LongOnde', 'HautDune'))
		self.VerticalBarreTable = ttk.Scrollbar(self.FrameTable, orient="vertical", command=self.Table.yview)
		self.Table.configure(yscrollcommand=self.VerticalBarreTable.set)
		
		self.Table['show'] = 'headings' # On n'utilise pas la colonne avec les + (on ne l'affiche pas)
		self.Table.pack(side=LEFT, fill = BOTH, expand = 1)
		self.VerticalBarreTable.pack(side=RIGHT, fill = Y)
		
		self.Table.column('Nombre', width=100, anchor='center')
		self.Table.heading('Nombre', text='Nb Dunes')
		self.Table.column('LongOnde', width=150, anchor='center')
		self.Table.heading('LongOnde', text="Longueur d'onde (m)")
		self.Table.column('HautDune', width=140, anchor='center')
		self.Table.heading('HautDune', text="Hauteur dune (cm)")
		

		img = np.array(MonImage)
		img = Image.fromarray(img)
		self.image = img

		self.Canevas = Canvas(fenetre)
		self.ImageAAfficher = ImageTk.PhotoImage(img)
		self.Canevas.create_image(0,0,anchor=NW,image = self.ImageAAfficher)
		self.Canevas.config(width=img.size[0], height=img.size[1])
		self.Canevas.configure(cursor="crosshair")
		self.Canevas.bind("<Button-1>", self.Hauteur)
		self.Canevas.pack(side=RIGHT, fill = BOTH, expand = 1) 
		
		self.RemplirTableauResultats()
		self.TableauAnalyseImage = [0,0,0,0,0]
		self.BilanDunesImage = [0,0,0]
		


	def ExportTxt(self):
		ExportTXT.ExportResultatsDunes(self.TableauAnalyseImage, self.MonImage, self.BilanDunesImage)
	
	def RemplirTableauResultats(self, ResultatsDunes = array([[0,0,0]])):
		NombreDunes = shape(ResultatsDunes)[0]
		for i in range (0, NombreDunes):
			self.Table.insert('', 'end', str(i), text='Axe ' + str(i), values = (str(ResultatsDunes[i][0]), str(ResultatsDunes[i][1]), str(ResultatsDunes[i][2])))

	#Méthode se lançant au moment où l'on appuie 
	#Calcul la hauteur de l'image
	def Hauteur(self, event):
		PositionX = event.x
		PositionY = event.y
		if(PositionX <  self.image.size[0] and PositionY < self.image.size[1]):
			hauteur = Hauteur.Hauteur(self.separation, self.origine.getImage(), self.MonImage)
			resolution = self.origine.getResolutionAltitude()
			hauteur.calculAll(resolution)

			im = mge.Image()
			im.init1(copy.deepcopy(self.MonImage))
			self.EraseFile("Graphique")
			for x in range(0, self.image.size[0],1):
				pixStart = pi.Pixel(x, 0, 0)
				pixEnd = pi.Pixel(x, self.image.size[1]-1, 0)
				transec = tr.Transec(pixStart, pixEnd, im)
				ligne = transec.calcul()
				plt.plot(ligne)
				axes = plt.gca()
				axes.set_ylim(-5, 260)
				plt.savefig("Graphique/ligne"+str(x)+".png")
				plt.close()

		print("temps ", time.clock() - self.temps)
		#self.RemplirTableauResultats()

	#Permet de supprimer tous les fichiers dans un répertoire
	#@param repertoire : string
	def EraseFile(self, repertoire):
		import os

		files=os.listdir(repertoire)
		for i in range(0,len(files)):
			os.remove(repertoire+'/'+files[i])