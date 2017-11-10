""" kevinjc -- spillebrett.py """


from random import randint
from celle import Celle



"""Dette er spillbrett klassen"""
class Spillebrett:
	def __init__(self, rader, kolonner):
		"""Init metoden"""
		self._rader = rader
		self._kolonner = kolonner
		self._rutenett = []	#ikke nodvendig, men den er der i eksempelfilen, derfor lar den vare der

		#genererer et objekter i en nøstet 2d liste med dimensjoner radar x kolonner
		self._rutenett = [[Celle() for j in range(self._kolonner)] for i in range(self._rader)]
		self.generer()
		self._generasjon = 0
	


	def tegnBrett(self):
		"""Opprette et titalls blanke linjer før utskrift"""
		newlines = 0
		while newlines < 50:
			print()
			newlines += 1
		"""Skrive ut hvert objekt i rutenettet som 'O' eller '.'."""
		for i in range(len(self._rutenett)):
			for j in range(len(self._rutenett[i])):
				print(self._rutenett[i][j].hentStatusTegn(), end="")
			print()


	def oppdatering(self):
		"""Folger reglene gitt i oppgaven for aa oppdatere celle-objektene i rutenettet"""
		skalDoed = []
		skalLeve = []
		
		for x in range(self._rader):
			for y in range(self._kolonner):
				nabo = 0 #antall naboer rundt cellen med koordinater (x,y)
				for i in range(len(self.finnNabo(x,y))):
					if self.finnNabo(x,y)[i].erLevende() == True:
						nabo +=1
				#-------------------------------Regler--------------------
				if (self._rutenett[x][y].erLevende()) == True and (nabo <2): #underpopulasjon
					skalDoed.append(self._rutenett[x][y])

				elif (self._rutenett[x][y].erLevende()) == True and (nabo >3): #overpopulasjon
					skalDoed.append(self._rutenett[x][y])

				elif (self._rutenett[x][y].erLevende()) == False and (nabo == 3): #reproduksjon
					skalLeve.append(self._rutenett[x][y])

		""" Gjor om objektene i rutenettet, enten til doed eller levende, eller ingen endring"""
		for k in range(self._rader):
			for l in range(self._kolonner):
				if self._rutenett[k][l] in skalDoed:
					self._rutenett[k][l].settDoed()
				elif self._rutenett[k][l] in skalLeve:
					self._rutenett[k][l].settLevende()			
		
		self._generasjon += 1 #Endrer generasjonen 
		

	def finnAntallLevende(self):
		"""Finner antall levende celler paa spillebrettet"""
		antallLevende = 0
		for q in range(self._rader):
			for r in range(self._kolonner):
				if self._rutenett[q][r].erLevende() == True:
					antallLevende +=1
		return antallLevende


	def generer(self):
		"""genererer Celle objekter"""
		for i in range(self._rader):
			for j in range(self._kolonner):
				rand = randint(0,3)
				if rand == 3:
					self._rutenett[i][j].settLevende()
				else:
					self._rutenett[i][j].settDoed()


	def finnNabo(self, rad, kolonne):
		"""Lager en liste av Celle-objekt naboer til et Celle-objekt paa posisjon [i][j] i rutenettet"""
		naboliste = []
		for i in range (-1,2):
			for j in range(-1,2):
				naboRad = rad + i
				naboKolonne = kolonne + j
				if (naboRad == rad and naboKolonne == kolonne) != True:
					if (naboRad < 0 or naboKolonne < 0 or naboRad >self._rader - 1 or naboKolonne > self._kolonner - 1) != True:
						naboliste.append(self._rutenett[naboRad][naboKolonne])
		return naboliste
	

	def generasjon(self):
		"""Funksjon som returnerer generasjonsnummeret"""
		return self._generasjon
