# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:27:06 2023

@author: PC
"""

def modif_1(v):
    x=v
    print("x")
    # x est une variable locale
    
#appel

x = 10 # variable dans le PG principal

modif_1(99)
print(x) 


#============== exemple2

def modif_2(v):
    x=1
    x = x + v
    print(" Dans la function, x = ", x)
    
#appel PGP

x=10
modif_2(99)
print("in ProgrammePrincpal, x = ", x)




#=========exemple 3

def modif_3(v):
    global x
    x = x + v
    print(" Dans la function, x c'est ", x)
    
#appel PGP

x=10
modif_3(99)
print("in PGP, x = ", x)

#function locales et globales
def externe(a):
    #une autre function imbriquée dedans
    def interne(b):
        return 2.0 * b
    #on retourne dans la function externe
    return 3.0 * interne(a)
#Appel
x=10
print("in PGP", externe(x))


#=========exemple 4
def modif_3(v):
    global x
    x = x + v
    print(" Dans la function, x c'est ", x)
    
#appel PGP

x=10
modif_3(99)
print("in PGP, x = ", x)

#function locales et globales
def externe(a):
    #une autre function imbriquée dedans
    def interne_1(b):
        def interne_1(c):
            return 2.0 * c
        return 2.0 * super_interne_1(b)
def interne_2(b)
    #on retourne dans la function externe
    return 3.0 * interne(a)
#Appel
x=10
print("in PGP", externe(x))