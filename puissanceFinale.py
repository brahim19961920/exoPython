#!/usr/bin/python3

import math

def finale(a,n):
    if((math.pow(a,n)%pow(10,len(str(n))))==n):
        return True
    return False

def toutes_les_finales(N,a):

    print("la liste de toutes les puissances finales de {} inferieurs ou egalesà {}".format(a,N))

    for i in range(N):
        if(finale(a,i)):
            print("{} est une puissance finale de {}".format(i,a))


print("Ce programme renvoie la liste de toutes les puissances finales de a inferieurs ou egales à N")

a=int(input(("entrez a\n")))
N=int(input("entrez N\n"))

toutes_les_finales(N,a)        

