# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 14:00:20 2023

@author: PC
"""

# La boucle While

n = int(input("rentrer n ...."))

#initialisation

sumPaire = 0
sumImpaire = 0
i = 1
while (i <= n):
    if i < 100 : 
        print("break à cause de", i)
    #somme des valeurs paires
    if (i % 2 == 0):
        sumPaire = sumPaire + i
        
    else :
        sumImpaire = sumImpaire + i
    i = i + 1 # ou i=+
#hors boucle
print("sortie de boucle avec i = ", i)
Sumtotale = sumPaire + sumImpaire

print("somme des valeures paire = ", sumPaire)
print("somme des valeures impaire = ", sumImpaire)
print("somme des valeures totales = ", Sumtotale)


    





