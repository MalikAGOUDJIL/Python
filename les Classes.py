# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:16:47 2023

@author: PC
"""





"""
# une classe:

classe est un type utilisateur

Classe est une fabrique d'objets (instancier un objet)


un objet est une variable de type classe  
"""

l1=[1,2,4] # instancier un objet de type liste
#Définition d'une classe Personne

class Personne : 
    """ classe Personne """
    # dans la class
    #constructeur (pour créer 
    #et initialiser un objet de la classe)
    def __init__(self):
        #self equivaut à this en Java
        #initialiser un objet c'est attribuer des valeurs aux attributs de l'objet
        #liste des attributs(certains les appelles les champs, d'autres les variables, d'autres les caractéristiques)
        self.nom = ""# si on met espace c'est comme si on a mis quelques chose 
        self.age = 0
        self.salaire = 0.0
        
    #la fin du constructeur 
    
    
#hors de la class