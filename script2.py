# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:14:22 2023

@author: PC
"""

a = 1
print(a)
print(type(a))

a = a * 1.2

print(type(a))

b =1.
print(b)
print(type(b))


c = float(2)
print(c)
print(type(c))

e = c + 4

print(type(e))

del e
e = c / 4
 
print(e)

ch = "une chaines"
print(type(ch))
print(len(ch))
print(ch[0])

#typage automatique ou par inférence
a = 1.0

#typage explicite
a = float(1)

#affectation multiple 

#meme valeur pour plusieurs variables 
a, b = 2.5, 3.2
print(a)
print(b)

# les plus utilisées
a = 1
b = 5
c = a+b

#ou bien
a=1 ; b=5 ;c = a+b; 

#réaffectation 

a = 1
b = 5
a = a+b
print(a)

nom = "Ninja18"
solde = 150000
credit = float(input("saisir le credit ..."))
debit = float(input("saisir le débit..."))
solde = solde + credit - debit
print(solde)


credit = float(input("saisir le credit ..."))
debit = float(input("saisir le débit..."))
solde = solde + credit - debit
print(solde)



a = input("entrez la valeur....")
print(a)
print(type(a))

a = float(a)



#ou

a = float( input("entrez la valeur...."))
print(a)
print(type(a))


q=bool("TRUE")
print(q)

#ouf = "15"
f = str(15)

print(f, "-" )
p=bool(1)
print(p)



#=================================

#comparaison des numbers
# >,>=, <,<=, != /<> , ==

a = (12!=13)
print(a)

#=================================
#entrée standard = clavier =>
#INPUT()

#sortie standard = écran
#PRINT()

#=================================









