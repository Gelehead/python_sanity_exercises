__version__ =   "TP4 - Exercice #1"
__author__  =   "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"


"""
Une écurie de course veut classer ses pilotes selon leur temps de qualification.

- Demandez le nombre de pilotes (doit être un entier > 0).
- Pour chaque pilote, demandez son nom et son score (entre 0 et 20).
- Stockez chaque entrée dans un tuple (Nom, Score).
- Affichez les pilotes triés par score croissant en utilisant une fonction lambda

### Exemple #1
Veuillez entrer le nombre de pilotes : 2
Nom du pilote : Lewis
Score : 18
Nom du pilote : Max
Score : 19
Classement : 
('Lewis', 18)
('Max', 19)

### Exemple #2
Veuillez entrer le nombre de pilotes : 3
Nom du pilote : Charles
Score : 15
Nom du pilote : Lando
Score : 10
Nom du pilote : Carlos
Score : 12
Classement : 
('Lando', 10)
('Carlos', 12)
('Charles', 15)
"""

# TODO : Commencez votre code ici

#consigne pas claire : "entre 0 et 20", inclus? 

while True : 
    nb_pilots = input("Veuillez entrer le nombre de pilotes : ")
    if nb_pilots.isnumeric() and int(nb_pilots) > 0 :
        break

nb_pilots = int(nb_pilots)

tuples = []
for i in range(nb_pilots) :
    name = input("Nom du pilote : ")
    while True :
        temp_score = input("Score : ")
        if temp_score.isnumeric() and (int(temp_score) >= 0) and int(temp_score) <= 20 :
            break
    tuples.append((name, int(temp_score)))

tuples.sort(key=lambda x : x[1])
print("Classement :")
for tuple in tuples : 
    print(tuple)