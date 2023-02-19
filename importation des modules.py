# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:26:29 2023

@author: PC
"""

#importer des modules externes
#exemples: Math et Random
#import math, random 
from math import log, pow
from random import seed, random
#dir(math)

#dir(random)

# générer un nombre réel compris entre 0 et 1 selon une distribution 
random.seed(None)
value = random.random()
print(value)

#Calcul le carré de logarithme Neperien
logv = log(value)
abslogv = pow(logv, 2.0)

print(abslogv)

#la fonction log est une fonction du module math

#on peut faire des racourcis en faisant
#import math as m, random as r
#cela permet de gagner du temps 


