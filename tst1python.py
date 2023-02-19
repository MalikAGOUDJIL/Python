# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#ceci est un commentaire 
#pht = 10 #prix HT
pht = input("entrer le prix unitaire hors Taxe:....")

print(pht, "le type de la variable pht est", type(pht))
#taux TVA
#transtypage ou Cast
pht = float(pht)
print(type(pht))
ttva = 1.2

#Prix TTC

pttc = pht * ttva


#affiche le resultat 

print("prix TTC est égal à ", pttc , "Euros") 