__version__ =   "TP4 - Exercice #3"
__author__  =   "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"


"""
Vous travaillez pour une agence de voyage. Trois amis donnent chacun une liste de 
destinations rêvées (séparées par des espaces). Identifiez uniquement les destinations 
communes aux trois amis.

Contrainte : Vous devez utiliser les propriétés des ensembles (set).
L'affichage doit être en minuscules, trié par ordre alphabétique.

### Exemple 1
Ami 1 : Paris Rome Tokyo
Ami 2 : Paris Berlin Londres
Ami 3 : Paris Tokyo Madrid
Destinations communes : paris

### Exemple 2
Ami 1 : Lyon Alger
Ami 2 : Lyon Alger
Ami 3 : Alger Lyon
Destinations communes : alger lyon
"""

# TODO : Commencez votre code ici

# les exos commencent a etre vrm repetitifs
txt = []
for i in range(3):
    txt.append(input("Ami", i, ": ").lower().strip("%:&^@$#()+[]").split())

dest = sorted(list(set(txt[0]) & set(txt[1]) & set(txt[2])))

print("Destinations communes :", " ".join(dest) )