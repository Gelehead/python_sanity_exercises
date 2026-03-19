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

# zzzzzzzzzzz
names = []
for i in int(input()) : 
    temp = input()
    while not (int(temp) >= 0 and int(temp) <= 20) :
        temp = input()
    