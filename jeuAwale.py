#!/usr/bin/python3
import random
def init_jeu(N):
    liste=list()
    for i in range(N):
        liste.append(random.randint(-1,101))
    return(liste)
def indice(N):
    a=int(input("entrer un indice valide, c'est à dire un entier positif et inférieur à {}\n".format(N)))
    while (a<0 or a>N):
        a=int(input("Entree invalide!entrer un indice valide, c'est à dire un entier positif et inférieur à {}\n".format(N)))


def vide():
    nb=0
    liste=init_jeu(80)
    for i in range(len(liste)):
        if (nb==liste[i]):
            nb+=1
    print(liste)
    print(nb)

def repartirFin(ind,l):
    if (ind<len(l)):
        nb=l[ind]
        l[ind]=0
        for i in range(ind+1,len(l)):
            l[i]+=1
        return l


print(repartirFin(5,[1,2,3,4,5,6,7,8,9,10]))

    



#liste=init_jeu(120)
#print(liste)











