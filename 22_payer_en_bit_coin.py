#! /usr/bin/env python3
# coding: utf-8

"""25 énigmes ludiques pour 'initier à la cryptographie
22 - payer en bitcoin
silanoc
25 février 2022

Returns:
le chiffre n
"""

class Hach():
	"""Class objet permettant de cherche le hach et de tester la divisibilité"""
	
	def __init__(self, mot):
		"""initialise en mettant dans des variables des calcul issu des méthodes de la classe"""
		self.mot = mot
		self.hache = self.hach()
		self.divisible = self.est_divisible()
	
	def hach(self):
		"""calcul du hach"""
		somme = 0
		for i in self.mot:
			somme += ord(i)
		return str(somme)

	def est_divisible(self):
		"""test la divisibilité"""
		if int(self.hache)%3 == 0 and int(self.hache)%5 == 0:
			return True
		else:
			return False

def test():
	"""juste des tests"""
	Pi314=Hach("Pi314")
	print(Pi314.hache, Pi314.divisible)

	alice = Hach("Alice")
	print(alice.hache, alice.divisible)

	bob = Hach("Bob")
	print(bob.hache, bob.divisible)

	multi = str(int(alice.hache) * int(bob.hache))
	multi_o = Hach(multi)
	print(multi_o.hache)

def resolution():
	"""initialise les variables connues et boucles 
 	jusqu'à ce que le double hach soit divisible
  	affiche le resultat cherché"""
	x, y, m, p = "A", "B", 5, 42
	xymp = x + y + str(m) + str(p)

	n = 0
	while True:
		xympn = xymp + str(n)
		H = Hach(xympn)
		HH = Hach(H.hache)
		if HH.divisible == True:
			break
		n += 1
		
	print(f"le nombre n recherché vaut {n}")
 
if __name__ == "__main__":
	#test()
	resolution()