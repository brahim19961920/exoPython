#!/usr/bin/python3
print("Ce programme permet de donner le résultat de la multiplication de deux entiers.\nOn utilisera l'algorithme de la divison egyptienne.")

erreur_de_saisie=True #variable permettant de controler la saisie des deux entres

#on boucle tant qu'au moins une des variables n'est pas entiere
while (erreur_de_saisie):
 try:
    x=int(input("Entrez le premier entier\n"))
    y=int(input("Entrez le deuxiéme entier\n"))
 except ValueError:
    print("Erreur de saisie. Refaites la saise")
 else:
  erreur_de_saisie=False


resultat=0#variable pour stocker le produit des deux variables
x1=x
y1=y

#boucle while mettant en place l'algorithme de la division egyptienne
while(y1):
    if(y1%2):
        y1-=1
        resultat+=x1
    else:
        x1*=2
        y1=int(y1/2)

print("{}*{}={}".format(x,y,resultat))#Affichage du résultat
