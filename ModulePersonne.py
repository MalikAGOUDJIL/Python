# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 09:45:19 2023

@author: PC
"""

#l1=[1,2,4] # instancier un objet de type liste

#Définition d'une classe Personne



class Personne :
    """ Classer Personne définie par:
        
        - nom
        -age
        -salaire
        -ville_residence
        """

    """ classe Personne """
    # dans la class
    
    
    Nb_pers = 0
    
    
    #constructeur pour créer et intialiser un objet de classe 
    def __init__(self, name="", ag=0, sal=0, ville=""):
        #self equivaut à this en Java
        #initialiser un objet c'est attribuer des valeurs aux attributs de l'objet
        #liste des attributs(certains les appelles les champs, d'autres les variables, d'autres les caractéristiques)
        self.nom = name# si on met espace c'est comme si on a mis quelques chose 
        self.age = ag
        self.salaire = float(sal)
        self.ville_residence = ville
        
        Personne.Nb_pers +=1
    #la fin du constructeur 
    
    #Supprimer un objet
    
    def __del__(self):
        """Destructeur d'objet  """
        Personne.Nb_pers -=1
        print("___trace objet supprimé__")
    
    
    
    #Setter
    def _set_nom(self, name):
        print("trace_set-nom")
        self._nom=name.upper()#rendre le nom tout en majiscule on a besoin de le mettre seulement ici
        
    def _set_age(self, ag):
        print("trace_set-age")
        if isinstance(ag, int):
            self._age= ag
        else :
            self._age = 0
            print("attention, valeur non numérique, age initialisé à 0")
        
    
    
    def _set_salaire(self, sal):
        print("trace_set-salaire")
        if isinstance(sal, float):
           self._salaire= sal
        else :
            self._salaire = 0
            print("attention, valeur non numérique, salaire initialisé à 0")
    
    def _set_ville(self, ville):
        print("trace_set-ville")
        self._ville_residence = ville.capitalize() #rendre la première lettre du nom tout en majiscule on a besoin de le mettre seulement ici
  
    
    #Getter
    
    def _get_nom(self):
        print("trace_get-nom")
        return self._nom
    
    def _get_age(self):
        print("trace _get_age")
        return self._age
    
    def _get_salaire(self):
        print("trace _get_salaire")
        return self._salaire
    
    def _get_ville(self):
        print("trace_get-ville")
        return self._ville_residence
    
    
    
    
    #saisir infos 
    def saisie(self): 
        """ 
        Fonction de saisie des infos de Personne
        """
        self.nom = input("entrer le nom...." )
        self.Ville_residence = input("entrer ville")
        #on ajoute un contôle du format des saisie
        while(1):
            try:
                
                self.age = int(input("Entrer l'âge...."))
                self.salaire = float(input("entrer salaire..."))
                break
            except ValueError:
                print("Merci de fournir un int pour l'age et un floatant pour le salaire")
        
    #Affichage des infos de l'objet
    
    def afficher(self):
        """ 
        Fonction d'affichage des infos de Personne
        """
        print("son nom est ", self.nom)
        print("son age est ", self.age)
        print("son salaire est ", self.salaire)
        print("Sa ville de résidence est", self.ville_residence)
        
        
        
        
        
        
    def AfficheNbPers():
        print("Nombre d'objets Personne crées est de :", Personne.Nb_pers)
              
        
    def copy(p):
        """copier un objet Personne
        """
        q=Personne(p.nom,p.age, p.salaire)
        return q
    
    ville_residence = property(_get_ville,_set_ville)
    nom = property(_get_nom,_set_nom)
    age = property(_get_age,_set_age)
    salaire = property(_get_salaire,_set_salaire)
   
    
   
 #fin classe Personne
 
 
 #Début CLASS EMPLOYE
 #elle hérité de la classe personne
class Employe(Personne):

    """
    Classe employe hérite de la classe Personne
    un employee est défini par:
    nom, age, salaire, ville de résidence, prime, fonction
  
    """
    Nb_emp = 0

  #constructeur de la classe employe
    def __init__(self, name="",ag=0,sal=0,ville="",bonus=0, job=""):
         Personne.__init__(self, name, ag, sal,ville) #Appel constructeur du Parent
         self.prime = 0.0
         self.fonction = ""
         
         Employe.Nb_emp +=1
         #Employe.Nb_emp +=1
      
     
  #saisie
  
    def saisie(self):
         Personne.saisie(self)
         self.prime = float(input("entrer la valeur de la prime..."))
         self.fonction = input("Entrer la fonction ...")
      
      
  #afficher
    def afficher(self):
         Personne.afficher(self)
         print("Sa prime : ", self.prime)
         print("sa fonction : ", self.fonction)
         print("salaire total : ", self.salaire + self.prime)
  
  
  
  
  
     
     
     
     
     
     
     
    
    
        
        
        
        
        