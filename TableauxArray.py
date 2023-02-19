# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:20:14 2023

@author: PC
"""

#Listes

#tableau = array (NumRy)
#liste = list

l1 = [2,6,8,10,15,26]
l1


len(l1)

l1[0]
l1[-1]

l1[0:4]




l1[0] = 1 #changement element
l1
l1.append(31) #ajouter 3& à la fin (append = ajout à la fin)
 
l1.insert(1, 'txt') 
l1

l1.insert(1, 15) 
l1

# suppression 

del l1[1] # supprime la première la position
               

l1

l1.remove(15)# supprime la première valeur 
               #qui correspand en partant de gauche


a=l1.pop(1) #enlève l'indice 1 et le stock dans la variable a

a  #on voit l'indice 1 stocké dans cette variable
l1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

l1.insert(1,6) #on remet l'indice 1 à sa place
l1

#renverser

l1.reverse()

#trier

l1.sort()

l1.insert(2,'coucou')
l1
del l1[2]
sum(l1) # avec des nombre, elle fait les cumules, 
         #avec string elle retourn erreur

l1.extend([34,55])
l1.append([64,65])

l1

l2 = l1

del l1[-1]

l1
l2

l3 = l1.copy()

l1.insert(1,100)


l1
l3


l1
l2=[]

for v in l1:
    l2.append(v**2)

l2
 # Avec les listconprehension
l3 = [v**2 for v in l1]
l3

l4 = [v for v in l1]
l4


#=== exemple avec condition

l2=[]

for v in l1:
    if(v % 2 == 0):
       l2.append(v**2)

l2

 # Avec les listconprehension
 
l3 = []
l3 = [v**2 for v in l1 if(v %2 == 0)]

l3
#============================
l2 = []
for v in l1:
    if (v % 2 ==0):
        l2.append(v**2)
    else:
        l2.append(v**3)
        
l2



#ou
l3 = []
l3 = [v**2 if(v % 2 == 0) else v**3 for v in l1]

l3

#====================================

#verifier si un chiffre se trouve dans ma 
#liste
flag = 36 in l3
flag 


ind = l3.index(36)
ind

#savoir l'occurence d'un chiffre 
#dans la liste
l3.count(36)


#===============Les chaines de caractère===================

s1 = "bonjour le monde"

s1 

len(s1) #taille

c5 = s1[5]
c5

s2 = s1[:7]
s2


s1[0] = 'B' #erreur car str non mutable
#quelques fonctions associées

s1.upper()
s1.lower()
s1.capitalize()
s1.find("JO")#en majiscule il ne le trouve pas 

s1.find("jo")

s1.count("on")
s2=s1.replace("o", "a")

s2

#transform en list

l1 = list(s1)
l1

list_word = s1.split(" ")

list_word

s_remonte = " ".join(list_word)
s_remonte 

#============Dictionnaire

#structure en key values / clé valeur

d1 = {'Pierre': 17, 'Paul': 15, 'Jack': 16}

type(d1)

d1.keys() #que les clés (les prénoms) sous forme de liste
d1.values()#que les valeurs (l'age) sous forme de liste
d1.items()#il récupère les deux sous formes de tuples

#accès à une valeur à parir d'une clé

d1['Paul']
d1[0]#erreur car c'est un dictionaire on le parcoure pas avec des indices
     # mais avec des valeurs

#ou

d1.get('Paul') #equivalent à d1['Paul']


#modifier l'âge

d1['Jack'] = 18

d1['Mal'] = 23

d1

del d1['Mal']

d1

d1.update({'Monica':36, 'Bill':49, 'Henri':22})

d1

#autres types de clés et de values

d2={('Pierre', 56):['Directeur', 1245, True],('Paul', 55):['Employe', 100, False]}



d2.keys()

d2.values()


























t=()
type(t)