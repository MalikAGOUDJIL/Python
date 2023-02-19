# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 13:51:59 2023

@author: PC
"""

from ModulePersonne import Personne

p=Personne()

p.saisie()

p.afficher()

p.nom

#cration d'un dictionaire

d={"Nom":p.nom, "Age":p.age, "Salaire":p.salaire, "Ville_residence":p.Ville_residence }

print(d)


#sauvegarder sous JSON

import json
f=open("personne.json", "w")

#on serialize le fichier d dans le fichier f
json.dump(d,f)

#le fichier est créé dans le dossier

f.close()


#==========deuxième façon


p.__dict__

json.dump(p.__dict__, f)

#ces deux lignes remplace le reste qu'on a fait avant

f.close()

f=open("personne.json", "r")
print(f)

del p



#==========================


p1=Personne()

p1.afficher()

f=open("personne.json", "r")

#charger le contenu json dans un dict

d=json.load(f)

p1._dict_= d

p1.afficher()

f.close()

#=====changer le contenu json dans un dict

p1.poids = 20;
p1.poids

p1.__dict__








