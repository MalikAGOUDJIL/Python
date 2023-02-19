# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:43:28 2023

@author: PC
"""

#SQLITE? un mini sGBD embarqué dans  Python

import sqlite3

# créer une base de donnée

datafile ="C:/Users/PC/Desktop/Python/bd_test.sq3"

#créer une connexion sur la BD

conn = sqlite3.connect(datafile)

# créer un curseur

cur = conn.cursor()

# créer une table
cur.execute("CREATE TABLE MEMBRES (age INTEGER, nom TEXT, tail REAL)")

#consulter la liste des tables existantes
cur.execute("select name from sqlite_master where type='Table'")

#afficher le resultat

print(cur.fetchall())

#alimenter la table membres

cur.execute("insert into membres values(21,'dupont', 183)")
cur.execute("insert into membres values(21,'m', 196)")
cur.execute("insert into membres values(18,'oz', 190)")

#valider les transactions (inserts)

conn.commit()

#pour annuler, on utilise ROLLBACK
#se déconnecter

cur.close()
conn.closed()

#---- se reconnecter------
import sqlite3
conn = sqlite3.connect(datafile)
cur = conn.cursor()

#afficher la liste des membres
cur.execute("select * membres")
print(cur.fetchall())

# or avec une FOR
for line in cur :
    print(line)
    
#Or
cur.execute("select * from membres")
list(cur)

#
cur.execute("select * from membres")
list(cur)



#insérer à partir d'une liste Python
data = [(17, "Durand",170), (48, "Toto", 178), (85, "Charles", 185)]

for m in data:
    cur.execute("insert into membres (age, nom, tail) values (?,?,?)", m)
conn.commit()

#afficher le resultat

cur.execute("select * from membres where tail >= 180")
list(cur)

#Update
cur.execute("update membres set tail = 201 where nom = 'OZ'")
   
cur.execute("select * from membres")
list(cur)


#delete
cur.execute("where from membres where nom = 'OZ'")
conn.commit()  

 
cur.execute("select * from membres")
list(cur)
    
cur.close()
conn.close()

    
    
    
    
    
    
    
    