class coupure():
	"""Classe de gestion de la coupure sur l'image originale.
	L'objet prendra des valeurs par défaut à la création en attendant que l'utilisateur finisse le tracé de la coupure.
	
	"""
	
	def __init__(self):
		"""
		Constructeur de la classe coupure.
		Donne des valeurs par défaut à l'objet coupure.
		
		"""
		self.x = -1
		self.y = -1
		self.bX = False
		self.bY = False

	
	def setValues(self, x, y):
		"""
		Setter des valeurs du premier coin du rectangle
		
		:param x: coordonnée en abscisse du premier coin du rectangle tracé par l'utilisateur.
		:type x: int
		
		:param y: coordonnée en ordonnée du premier coin du rectangle tracé par l'utilisateur.
		:type y: int
		
		"""
		self.x = x
		self.y = y
		self.bX = True
		self.bY = True
		
	#Pour voir qu'elles sont les bonnes coordonnées du point
	#@param x : int
	#@param y : int
	#@return x, y
	def coordonnees(self, x, y):
		"""
		Fonction de verification des coordonnées d'un coin.
		
		:param x: coordonnée en abscisse du coin à ajouter.
		:type x: int
		
		:param y: coordonnée en ordonnée du coin à ajouter.
		:type y: int
		
		"""
		if(self.bX == False and self.bY == False):
			self.setValues(x, y)
			return x, y

		Xi = x-self.x
		Yi = y-self.y
		if(abs(Xi)>abs(Yi)):
			if(self.bX):
				self.bX = False
				self.x += Xi
			elif(self.bY):
				self.bY = False
				self.y += Yi
		else:
			if(self.bY):
				self.bY = False
				self.y += Yi
			elif(self.bX):
				self.bX = False
				self.x += Xi

		return self.x, self.y