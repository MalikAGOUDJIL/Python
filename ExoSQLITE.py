# -*- coding: utf-8 -*-

#EXO : Persister un objet Personne dans la BD 

import sqlite3

datafile ="C:/Users/PC/Desktop/Python/bd_test.sq3"

conn = sqlite3.connect(datafile)
cur = conn.cursor()
p1 = PERSONNE
p1.saisie()
p1.afficher() 
cur.execute("CREATE TABLE PERSONNE (nom TEXT, ville TEXT, age INTEGER, salaire REAL)") cur.execute("insert into personne (nom, ville, age, salaire) values (?,?,?,?)",tuple(p1.__dict__.values()))
conn.commit() cur.execute("select * from personne")
list(cur)

