import numpy.fft as npf
import numpy as np
import random as rd
from collections import deque
import statistics as stats
 
"""
	Module de filtrage de signaux.
	Utilisé pour lisser la courbe de profil d'un axe.
"""


def deriv(signal):
	"""Fonction qui dérive les valeurs du signal
	
	:param signal: Valeurs du signal.
	:type signal: liste
	"""
	long=len(signal)
	y=[signal[0]]
	for i in range(1,long):
		y.append(signal[i]-signal[i-1])
	return y


def ampli(signal,A=0):
	"""Fonction d'amplification des valeurs du signal par A.
	
	:param signal: Valeurs du signal.
	:type signal: liste
	
	:param A: Valeur d'amplification du signal.
	:type A: int
	"""
	return [A*x for x in signal]
	
# Décaler
def decal(signal,D=0):
	"""Fonction de décalage des valeurs du signal par D.
	
	:param signal: Valeurs du signal.
	:type signal: liste
	
	:param D: Valeur de décalage du signal.
	:type D: int
	"""
	return [x+D for x in signal]

def moyenneOLD(signal):
	"""Fonction qui va moyenner le signal sur 4 valeurs glissantes
	
	:param signal: Valeurs du signal.
	:type signal: liste
	"""
	long=len(signal)
	
	y=[signal[0],(signal[0]+signal[1])/2,(signal[0]+signal[1]+signal[2])/3]
	for i in range(3,long):
		y.append((signal[i]+signal[i-1]+signal[i-2]+signal[i-3])/4)
	return y

def moyenne(signal,n=4):
	"""Fonction qui va moyenner le signal sur n valeurs glissantes
	
	:param signal: Valeurs du signal.
	:type signal: liste
	
	:param n: Nombre de valeurs glissantes
	:type n: int
	"""
	print(n)
	init=[]
	l=len(signal)
	y=[]
	for i in range(0,n):
		init.append(signal[i])
	fifo = deque(init, maxlen=n)
	y.append(stats.mean(fifo))	
	for i in range(1,l):
		fifo.extend([signal[i]])
		y.append(stats.mean(fifo))
	return y
	
	
def mediane(signal):
	"""Fonction qui extrait la médiane de 5 valeurs.
	
	:param signal: Valeurs du signal.
	:type signal: liste
	"""
	N=len(signal)
	x=[]
	for i in range(N-5):
		x.append(np.median(signal[i:i+5]))
	for i in range(5):
		x.append(np.median(signal[N-6+i:N-1]))    
	return x


def passe_bas(signal,Fc=1):
	"""Fonction de filtrage passe bas (premier ordre analogique)
	
	:param signal: Valeurs du signal.
	:type signal: liste
	
	:param Fc: fréquence de coupure en Mhz
	:type Fc: int
	"""
	long=len(signal)
	t=np.linspace(0,long,long)
	y=[(signal[0]*2*np.pi*Fc*t[1]+signal[0])/(1+2*np.pi*Fc*t[1])]
	for n in range(1,long):
		y.append((signal[n]*2*np.pi*Fc*t[1]+y[n-1])/(1+2*np.pi*Fc*t[1]))
	return y




