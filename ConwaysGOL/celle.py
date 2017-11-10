""" Kevinjc -- celle.py"""

class Celle:
	"""
	Klassen beskriver en celle i simularingen.
	En celle skal ha en variabel som beskriver status utgangspunkt doed eller levende.
	"""
	#constructor
	def __init_(self, status = 0):
		"""
		Status:
		doed = 0
		levende = 1
		"""	
		self._status = status

	#Endre status
	def settDoed(self):
		"""sett doed"""
		self._status = 0

	def settLevende(self):
		"""sett Levende"""
		self._status = 1

	#Hente status
	def erLevende(self):
		"""Er Celle-objektet levende?"""
		if self._status == 1:
			return True
		else:
			return False

	def hentStatusTegn(self):
		"""Hent status tegn"""
		if self._status == 1:
			return "O"
		elif self._status == 0:
			return "."
