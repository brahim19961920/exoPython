#!/usr/bin/python3
"""Fichier comportant quelques fonctions pour manipuler une chaine de caractére"""

#Fonction retournant le nombre de mots d'une chaine de caractéres
def nb_mots(chaine):
    return(len(chaine.split()))

#Fonction affichant le mot d'indice passé en argument dans une phrase donnée  
def affiche_mot(indice,chaine):
        liste=chaine.split()
        if(indice<len(liste)):
            return (liste[indice])
        else:
            return"l'indice donnée dépasse le nombre de mots"

#Fonction verifiant si une chaine de caractere est carrée ou pas
#Par exemple papa est une chaine carree pa=pa
def chaine_carre(ch):
    return(ch[:int(len(ch)/2)]==ch[int(len(ch)/2):])

#Fonction retournant une liste contenant les mots carree d'une phrase
def liste_chaine_carre(phrase):
    liste=phrase.split()
    l=[]
    for mot in liste:
        if (chaine_carre(mot)):
            l.append(mot)
    return l
print(liste_chaine_carre("papa mama dhsjqk hdezjk jdks azaz"))

#Fonction verifiant si une chaine est paindrome ou pas
def palindrome(ch):
    inverse=ch[::-1]
    return(ch==inverse)

