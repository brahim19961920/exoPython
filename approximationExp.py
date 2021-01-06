#!/usr/bin/python3

#programme permettant de donner une valeur approximée de e(exp(1))

e=1
prod=1
for i in range(1,10000):
    prod*=i
    e+=(1/prod)

print("exp(1)={}".format(e))
