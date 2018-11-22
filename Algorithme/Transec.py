import math as mt

#Classe pour récupérer la ligne
class Transec():
	#Initialisation
	#@param pointDepart : pixel
	#@param pointArrive : pixel
	#@param image : image
	def __init__(self, pointDepart, pointArrive, image):
		self.pointDepart = pointDepart
		self.pointArrive = pointArrive
		self.image = image

	#Reccupère les données de la ligne
	def calcul(self):
		xStart = self.pointDepart.getX()
		xEnd = self.pointArrive.getX()
		yStart = self.pointDepart.getY()
		yEnd = self.pointArrive.getY()	

		xStep = yStep = 0

		if(xStart <= xEnd):
			xStep = 1
		else : 
			xStep = -1

		if(yStart <= yEnd):
			yStep = 1
		else : 
			yStep = -1

		ligne = []

		x = xStart
		y = yStart

		xDist = abs(xStart - xEnd)
		yDist = abs(yStart - yEnd)

		xDiv = yDiv = 0

		#sprint(xEnd, yEnd)
		while x <= xEnd and y <= yEnd:
			if(xDist == yDist):
				ligne.append(self.image.read1(x, y))
				x += xStep
				y += yStep
			else:
				if(yDist == 0):
					ligne.append(self.image.read1(x, y))
					x += xStep
				elif(xDist == 0):
					ligne.append(self.image.read1(x, y))
					y += yStep
					#print(y)
				else:

					xDiv = xDist/yDist
					yDiv = yDist/xDist
					if(xDiv>yDiv):
						xDiv = mt.ceil(xDiv)
						for i in range(xDiv):
							ligne.append(self.image.read1(x, y))
							x += xStep
						y += yStep
					else : 
						yDiv = mt.ceil(yDiv)
						for i in range(yDiv):
							ligne.append(self.image.read1(x, y))
							y += yStep
						x += xStep

		return ligne