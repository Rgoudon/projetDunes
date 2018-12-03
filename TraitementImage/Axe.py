from TraitementImage import Point

class Axe():
	"""Classe de création d'objet axe.
	Contient les coordonnées en pixel du point de départ et d'arrivé de l'axe.
	
	:param XpointDepart: Coordonées en abscisse du point de départ de l'axe en pixel sur l'image.
	:type XpointDepart: int
	
	:param YpointDepart: Coordonées en ordonnée du point de départ de l'axe en pixel sur l'image.
	:type YpointDepart: int
	"""
	
	def __init__(self, XpointDepart, YpointDepart):
		
		self.PointDepart = Point.Point(XpointDepart, YpointDepart)
		self.PointArrive = None
		
	def AjoutPointArrive(self, Xpoint, Ypoint):
		"""
		Setter du point d'arrivé de l'axe.
			
		:param XPoint: coordonnée en abscisse du point d'arrivé à ajouter.
		:type Xpoint: int
			
		:param Ypoint: coordonnée en ordonnée du point d'arrivé à ajouter.
		:type Ypoint: int
			
		"""
		self.PointArrive = Point.Point(Xpoint, Ypoint)
			
	def getPointDepart(self):
		"""
		Getter du point de départ de l'axe.
		
		:return: Objet de la classe point correspondant au point de départ de l'axe.
		
		"""
		return self.PointDepart
	
	def getCoordonneesPointDepart(self):
		"""
			Getter des coordonnées du point de départ de l'axe.
			
			:return: couple de coordonnées (X,Y) du point de départ de l'axe.
		
		"""
		return self.PointDepart.getCoordonnees()
	
	def getPointArrive(self):
		"""
		Getter du point d'arrivée de l'axe.
			
		:return: Objet de la classe point correspondant au point d'arrivée de l'axe.
		
		"""
		return self.PointArrive
	
	def getCoordonneesPointArrive(self):
		"""
		Getter des coordonnées du point d'arrivée de l'axe.
			
		:return: couple de coordonnées (X,Y) du point d'arrivée de l'axe.
		
		"""
		return self.PointArrive.getCoordonnees()
	
	def getCoordonneesAxe(self):
		"""
		Getter des coordonnées des points de départ et d'arrivée de l'axe.
			
		:return: couple de coordonnées ((X,Y),(X,Y)) respectivement des points de départ et d'arrivé de l'axe.
		"""
		return self.getCoordonneesPointDepart(), self.getCoordonneesPointArrive()
	
	def VecteurXaxe(self):
		return self.PointArrive.getXpoint() - self.PointDepart.getXpoint()

	def VecteurYaxe(self):
		return self.PointArrive.getYpoint() - self.PointDepart.getYpoint()
	
	def VecteurAxe(self):
		return self.VecteurXaxe(), self.VecteurYaxe()
