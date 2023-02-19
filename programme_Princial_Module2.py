# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 10:13:42 2023

@author: PC
"""

from ModulePersonne import Personne

#instanciation

p=Personne()

p.saisie()

p.afficher()


#============= gestion d'une collection d'objet

l1 = []

#Nombre d'objet à créer 

n = 3
#saisie de la liste

for i in range(0,n):
    print("saisir le", i+1, "ème Personne")
    a=Personne()
    a.saisie()
    l1.append(a)
    
    
#Afficher les objets de la liste

for p in l1 :
    print("--------")
    p.afficher()
    
    

    
    
    
    
    
    
    
    
    