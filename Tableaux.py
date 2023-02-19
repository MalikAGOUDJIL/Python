# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:19:05 2023

@author: PC
"""
#nous importons notre module
import Module_TVA as tva

dir(tva)

help(tva)


pht = int(input("entrez le prix hors taxe:...."))

#afficher le prix TTC

pttc = tva.pttc_normal(pht)

print("le prix TTC = ", pttc)

 #=====================================
 #on import l'os
import os
#on affiche le répértoire courant
os.getcwd()
 #changer le répértoire courant 
 #os.chdir()
