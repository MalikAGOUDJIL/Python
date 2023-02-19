# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:11:21 2023

@author: PC
"""

#function qui calcule le plus petit entre a et 6

def plusPetitproc(arg1, arg2):
    if(arg1 < arg2):
        print(" Le plus petit des nombres est:", arg1)
    else:
        
        print(" Le plus petit des nombres est:", arg2)
        

# programme principal

u = 10
v = 9

#var x pour récupérer le resultat de la fonction
x = plusPetit2(u, v)
print(" Proc Le plus petit des nombres est :", x)

#passage de valeur par position
plusPetitproc(115, 111)


#passage de valeur par nom
plusPetitproc(arg2= 105, arg1=99)

#passage par variable (références)

plusPetitproc(u, v)