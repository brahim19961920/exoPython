#!/bin/python3
# ce script permet de retourner la représentation binaire d'un décimal
import math
entier=int(input("entrer un entier pour déterminer sa représentation binaire\n"))
ind_puiss=1 #cette variable désigne l'indice du multiple de 2 directement supérieur à l'entier traité

#cette boucle permert de déterminer ind_puiss
while entier>math.pow(2,ind_puiss):
    ind_puiss+=1

if (entier!=math.pow(2,ind_puiss)):
    ind_puiss-=1

#chaine de caractére pour contenir le résultat à afficher
resultat=str(entier)+"="
while(ind_puiss>=0):
       if(entier>=math.pow(2,ind_puiss)):
           entier-=math.pow(2,ind_puiss)
           resultat+=("2^"+str(ind_puiss)+"+")
       ind_puiss-=1


resultat=resultat[:len(resultat)-1]#ici on enleve le dernier + il est inutile 
print(resultat)# affichage du résultat
