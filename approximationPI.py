#!/usr/bin/python3
import random 
import math
def valeurDePi():
    s=0
    for i in range(10000000):
        y=random.random()
        x=random.random()
        if ((math.pow(x,2)+math.pow(y,2))<1):
            s+=1
    print(4*s/10000000)

valeurDePi()

