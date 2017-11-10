"""Kevinjc -- Main.py"""
from spillebrett import Spillebrett

def main():
	"""Brukes for aa kjoere Conways game of life"""

	print("Skriv inn dimensjoner")
	rader = int(input("\nRad:"))
	kolonner = int(input("\nKolonner:"))

	brett = Spillebrett(rader,kolonner)

	brett.tegnBrett()
	print("Generasjon:", brett.generasjon(), " - Antall Levende:", brett.finnAntallLevende())

	UserInput = str(input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte:"))

	while UserInput != "q":
		brett.oppdatering()
		brett.tegnBrett()
		print("Generasjon:", brett.generasjon(), " - Antall Levende:", brett.finnAntallLevende())
		UserInput = str(input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte:")) 


main()
