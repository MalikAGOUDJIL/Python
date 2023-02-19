# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:24:53 2023

@author: PC
"""

#structure algorithmique
#structure de branchement
#If..... then .....Else

#if condition:
      #blocs d'instructions
#else : 
   # bloc d'instructions 
    
#exemple:
    
 #saisir à la console d'un prix HT
    
pht = float(input("saisir le prix HT"))
    
#code produit
    
code = int(input("entrez le code du produit:"))


#PTTC en fonction du code produit
match code:  

   case 1:
      taxe = pht * 0.055
    
   case 2:
      taxe = pht * 0.10
    
   case 3:
      taxe = pht * 0.20

   case 4:
      taxe = pht * 0.085
   
   case : 
      taxe = pht * 0.0
    
    
pttc = pht + taxe
    
#affichage avec transtypage 
print("prix TTC : "+str(pttc))

