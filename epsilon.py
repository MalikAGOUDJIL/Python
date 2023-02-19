# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:38:28 2023

@author: PC
"""
import math #un modul Math qu'on apporte pour utiliser les opérations mathématiques et dans
# ce module il y a une fonction qui s'appelle fabs 
#on met le nom du module.la fonction 
# dans cet exemple ca sera math.fabs


#valeur absolue flottante

def ecart(a,b, epsilon = 0.1):
    d=math.fabs(a-b) #f pour le vlotant abs pour la valeur absolue
    if (d < epsilon):
        d=0
    print("in func: value epsilon = ", epsilon)
    return d
    
    
    #programme principal
    
diff = ecart(a=12.2, b=11.9, epsilon = 1)
print(diff)
    
diff = ecart(a=12.2, b=11.9)
print(diff)