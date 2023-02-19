# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 13:40:14 2023

@author: PC
"""

#Collections : array, list, tuples, dictionnaires, str...


#tuples
#une liste de tuples: un ensemble d'éléments qu'on met entre parenthèses

t1=(2,7,8,10,15,26)
print(type(t1))

print("length : ", len(t1))

a = t1[0]#premier élément avec indice = 0
print(a)

b = t1[-1]# dernier élément avec indice = -1
print(b)

# meme chose avec cette manière b = t1[lent(t1)-1]# dernier élément avec indice = -1
#print(b)

#on peut pas modifier les elements car il est immutable




#afficher une plage de valeur

l1= t1[2:5] # jusqu'au 4e indice seulement le dernier indice indiqué n'est pas inclut
print(l1)


print(t1[2:5])

print(l1[2:len(t1)]) # de 2 jusqu'au dernier 

# ou 

print(t1[2:])


print(t1[0:4])

# ou

print(t1[:4]) 

print(t1[-3]) # il va dans le sens inverse et il cherche le troisième indice donc 10


print(t1[-9]) # il donne rien car  il sort de la liste 

print(t1[-3:]) # de 10 puis 15,26

print(t1[:-3]) # 2,7,8


#concaténer 
t2 = (7,9,13)

t3 = t1 + t2

print(t3)

t4 = t2 + t1
t4

#répliquer 
t5 = 3 * t2
t5


#tuple de tuples 
tt = ((2,3,4), (4,5,9), (1,8))

tt[1][2]

len(tt[1])

#question ? 
#comment obtenir un flatten_tt =(2,3,4,4,5,9,1,8)














