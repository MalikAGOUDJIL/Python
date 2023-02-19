# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:46:24 2023

@author: PC
"""

from ModulePersonne import Personne
#instanciation

p=Personne()

print(p)

help(p)

dir(p)

#affectation des valeurs 
  #aux attributs 

print(p.nom)

print(p.age)

p.nom = "Jacques"

p.nom

p.age = 25
p.salaire = 147522.

#afficher 

print("les infos de Personne P sont:", p.nom, p.age, p.salaire)























