# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:06:00 2023

@author: PC
"""
#Les fichier
#quand il s'agit d'une petit fichier il est
#automatiquement enregistré en mémoire


#ouverture du fechier

f=open("voiture.txt", "r")

#lecture

s=f.read()

#afficher 

print(s)

#afficher
print(s)

type(f)

len(s)

#fermeture

f.close()

#lecture par lignes

ls= f.readlines()
print(ls)


f.close()

f=open("voiture.txt", "r")

line= f.readline()
line

f.close()

#------

f=open("voiture.txt", "r")

while True :
    s=f.readline()
    if (s !=""):
        print(s)
    else:
        break 
    
f.close()

#ajouter un élément au fichier

f=open("voiture.txt", "a")

f.write('\n Alpine')

f.close()

# ouvrir un file en écriture

f=open("moto.txt", 'w')
ls = ("HD", "\nKWZK", "\nYamaha")
ls

#ecriture

f.writelines(ls)
f.close()

#afficher:
f=open("moto.txt", 'r')

s=f.read()
print(s)


#-------
f=open("moto.txt", 'r')

while True :
    s=f.readline()
    if (s !=""):
        print(s)
    else:
        break

f.close()

#---------------------

#lire les fichiers binaires

f=open("voiture.txt", "rb")

#afficher la position du curseur

print("position:", f.tell())

#repositionner le curseur
#f.seek(A,B) A c'est bouger 
#le cursur par unite, B c'est 
#bouger le crsur soit au début 0,
#soit position courant 1, soit à 
#la fin 2


#se positionner au tout début
f.seek(0,0)

#se positionner au tout à la fin
f.seek(-1,2)

f.tell()


#==utilisation de la clause With

with open("voiture.txt", 'r') as f:
    ls=f.readlines()
    for line in ls:
        print(line)
        
        
with open("voiture.txt", 'r+') as f:
    ls=f.readlines()
    for line in ls:
        f.write(line.replace("\n",","))        



#cette fonction ne remplace 
#pas le contenu mais il rajoute
#une autre liste sous forme de 
#phrase donc c'est un append


"""
====== à compléter car le fichier voiture3.txt est introuvable===
f_in= open("voiture.txt", 'r')
f_out= open("voiture.3.txt", 'w')


for line in f_in:
    f_out.write(line.replace("\n", ","))

f_in.close()
f_out.close()

f=open("voiture3.txt", "r")
print((f.read())
"""


#========= lire les fichier csv

import csv

f=open("Personne.csv", "r")



ls = csv.reader(f,delimiter=";")

for line in ls:
    print(line)
    
type(ls) 


f.close()

#====
import pandas as pd

dataset = pd.read_csv("Personne.csv",delimiter=";")
dataset.head(2)
dataset.tail(3)
dataset.info()
dataset.describe()


















