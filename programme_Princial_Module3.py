# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:15:03 2023

@author: PC
"""

from ModulePersonne import Personne 

p1=Personne("mike",36,45000,"paris")




p1.afficher()

p4=Personne(ville="mars")
p4.afficher

p2 = Personne.copy(p1)
p2.afficher()


flag = p1==p2
print("ref. identique : %s" %(flag))



Employe.Nb_pers
Employe.Nb_emp


#=========
l =[]
for i in range(0,3):
    
    code = input("1 Pers, 2 Emp :____")
    if (code =="1"):
        m = Personne()
    else :
        m = Employe()
    l.append(m)
    
    
#saisie

for p in l:
    p.saisie()
    
#Afficher
for p in l:
    print("------------")
    p.afficher()
    

    