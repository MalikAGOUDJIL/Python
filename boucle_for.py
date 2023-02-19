# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:01:11 2023

@author: PC
"""

# les boucles:
    
   
#valeur limite
n = int(input("rentrer n ...."))

#initialisation

sumPaire = 0
sumImpaire = 0
for i in range(1, n+1):
    #somme des valeurs paires
    if (i % 2 == 0):
        sumPaire = sumPaire + i
        
    else :
        sumImpaire = sumImpaire + i
        
#hors boucle
Sumtotale = sumPaire + sumImpaire

print("somme des valeures paire = ", sumPaire)
print("somme des valeures impaire = ", sumImpaire)
print("somme des valeures totales = ", Sumtotale)

