#!/usr/bin/python3

import random


#Fonction pour generer une liste d'entiers aleatoires entre 0 et 100
def init_jeu(N):
    liste=list()
    for i in range(N):
        liste.append(random.randint(-1,101))
    return(liste)

#Fonction permettant de saisir un entier valide
def indice(N):
    a=int(input("entrer un indice valide, c'est à dire un entier positif et inférieur à {}\n".format(N)))
    while (a<0 or a>N):
        a=int(input("Entree invalide!entrer un indice valide, c'est à dire un entier positif et inférieur à {}\n".format(N)))

#Fonction permettant de retourner le nombre de cases vides (nbr de 0 dans la liste)
def vide():
    nb=0
    liste=init_jeu(80)
    for i in range(len(liste)):
        if (nb==liste[i]):
            nb+=1
    return(nb)

#Fonction permettant de repartir le nombre se trouvant dans la case d'indice sur les élements suivants du tableau 
def repartirFin(ind,l):
    if(ind<len(l)):
          nb=l[ind]
          l[ind]=0
          while (nb>0 and ind<(len(l)-1)):
            ind+=1
            nb-=1
            l[ind]+=1

#Fonction ayant le meme principe que repartirFin sauf qu'on continue la repartition à partir du 1er element du tableau si on atteint la fin du tableau  
def repartirTout(ind,l):
    if (ind<len(l)):
        nb=l[ind]
        l[ind]=0
        while(nb>0):
            ind+=1
            nb-=1
            if(ind==len(l)):
                ind=0
            l[ind]+=1
            














