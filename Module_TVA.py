# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:14:36 2023

@author: PC

Module pour calculer des prix TTC application
de différents taux TVA
"""

# taxe à 10%

def pttc_reduit(p):
    """
    TVA intérmédiaire - ex ;; travaux aménagement
    """
    return p *1.1


# taxe à 20%

def pttc_normal(p):
    """
    TVA normal
    """
    return p * 1.2


# taxe à 5.5%

def pttc_alimentaire(p):
    """
    TVA alimentaire: repas etc
    """
    return p * 1.055

#Nous venons de créer un nouveau module


