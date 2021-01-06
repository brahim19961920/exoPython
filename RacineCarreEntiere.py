#!/usr/bin/python3
a=-9
while (a<0):
    a=int(input("entrer un entier positif. Ce programme déterminera la valeur entiere de la racine carée de cet entier\n"))
resultat=0
impaire=1
while(a>0):
    a=a-impaire
    impaire+=2
    resultat+=1
if (a==0):
    print(resultat)
else:
 print(resultat-1)















