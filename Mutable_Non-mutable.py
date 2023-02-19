# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:35:08 2023

@author: PC
"""
#mutable et non mutable

def modifier_non_mutable(a,b):

    a = 2 * a
    b = 3 * b
    print(a,b)
#appel
x = 10
y = 15
modifier_non_mutable(x,y)

print(x, y)

def modifier_mutable(a,b):
    a.append(8)
    b[0] = 6
    print(a,b)
    
    
#Appel
lx = [10]
ly = [15]

lx2=lx.copy()

ly2=ly.copy()

print(ly[0])


modifier_mutable(lx,ly)

print(lx, ly)
print(lx2, ly2)

#function renvoyoie plusieurs valeurs 

def triAsc(a,b):
    if(a < b):
        return a,b
    else :
        return b, a
    
#appel

x = 10
y = 8

min, max = triAsc(x,y)

print("min : ", min , "-- max :" , max)



#Version avec liste

def triAsc(a,b):
    if(a < b):
        return [a,b]
    else :
        return [b, a]
    
#appel

x = 10
y = 8
listTriee = triAsc(x,y)
print(listTriee)
print("min : ",listTriee [0] , "-- max :" , listTriee [1])
    
    
    
    
    
    
    
    
    