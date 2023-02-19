# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:50:12 2023

@author: PC
"""

n = 3
#dic
dic = {} #init un dic vide

#saisie 

for i in range(0,n+1):
     cle =input("Saisir la clé....")
     valeur = float(input("Saisir la valeur..."))
     dic[cle] = valeur

dic

dic.keys()
dic.values()
dic.items()

#Afficher 

for(k, v) in dic.items():
    print(k,v)
    
ldic = list(dic.items()) #on transforme en liste pour mieux 
                         #les gérer car dic.items est un ittérable qui pert certains éléments qui le rend compliqué à gérer
ldic[1][1]
