# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:17:38 2023

@author: PC

#exemple decorator
def make_pretty(func):
    #def func interne
    def inner():
        #do something
        print("I got decorator")
        
        #appel de la fun
        
        func()
    #retour
    return inner
    
    
# def func ordinaire

def ordinary():
    print("I am ordinary")
    
# decorateur

decorated_func = make_pretty(ordinary)

#appel

decorated_func()

"""
#======== exemple 2:
"""  
import math
def make_pretty(func):
    
        #def func interne
        def inner(a,b):
            #do something
            print("I got decorator")
            
            #appel de la fun
            
            print ("in inner()" math.fabs(round(func(a,b)))
            
        #retour
        return inner
        
        
    # def func ordinaire

def ordinary(a, b):
        print("I am ordinary")
        s=a* b
        print("in ordinary():", s)
        return s
    # decorateur
a=0.1587
b=-1.8

decorated_func = make_pretty(ordinary)

    #appel

decorated_func(a,b)
    
    
   """ 
    
#exemple ================================ 3
    
#exemple decorator

def make_pretty(func):
        #def func interne
    def inner(a,b):
            #do something
            print("I got decorator")
            
            
            #appel de la fun         
            print ("in inner():", math.fabs(func(a,b))
        #retour
    return 
#decorateur
@make_pretty  
# def func ordinaire
def ordinary():
    print("I am ordinary")
    s=a*b
    # decorateur
    print("in ordinary():", s)
    return s

 # decorateur
a=0.1587
b=-1.8
  #appel

ordinary(a,b)
    
    
    
    
    
    
    
    