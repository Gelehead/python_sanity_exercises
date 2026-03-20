__version__ =   "TP4 - Exercice #2"
__author__  =   "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"


"""
Demandez une phrase à l'utilisateur. Comptez le nombre d'occurrences de chaque mot et 
affichez le résultat sous forme de dictionnaire.

Remarques :
- Le programme ne doit pas être sensible à la casse (tout mettre en minuscules).
- Retirez les points et les virgules avant le traitement.

## Exemple #1:
Veuillez entrer une phrase : Bonjour je je suis un un un homme
Résultat : {'bonjour': 1, 'je': 2, 'suis': 1, 'un': 3, 'homme': 1}

## Exemple #2:
Veuillez entrer une phrase : Ceci est une phrase tellement redondante que l'on pourrait dire que c'est une phrase redondante.
Résultat : {'ceci': 1, 'est': 1, 'une': 2, 'phrase': 2, 'tellement': 1, 'redondante': 2, 'que': 2, "l'on": 1, 'pourrait': 1, 'dire': 1, "c'est": 1}
"""

## TODO: Commencez votre code ici

# flemme d expliquer a chaque fois
sentence = input("Veuillez entrer une phrase : ").lower()
dic = {}

for word in [x.strip(",.!?") for x in sentence.split(" ")] :
    if word == "" : continue
    if word not in dic :
        dic[word] = 1 
    else :
        dic[word] += 1

print("Résultat :", dic)