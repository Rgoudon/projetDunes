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
		
		"""
		self.PointArrive = Point.Point(Xpoint, Ypoint)
			
	def getPointDepart(self):
		return self.PointDepart
	
	def getCoordonneesPointDepart(self):
		return self.PointDepart.getCoordonnees()
	
	def getPointArrive(self):
		return self.PointArrive
	
	def getCoordonneesPointArrive(self):
		return self.PointArrive.getCoordonnees()
	
	def getCoordonneesAxe(self):
		return self.getCoordonneesPointDepart(), self.getCoordonneesPointArrive()
	
	def VecteurXaxe(self):
		return self.PointArrive.getXpoint() - self.PointDepart.getXpoint()

	def VecteurYaxe(self):
		return self.PointArrive.getYpoint() - self.PointDepart.getYpoint()
	
	def VecteurAxe(self):
		return self.VecteurXaxe(), self.VecteurYaxe()
