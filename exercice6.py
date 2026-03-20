__version__ =   "TP4 - Exercice #1"
__author__  =   "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"


"""
Vous devez écrire un programme permettant de trouver les diviseurs d'une liste de 
nombres.

Précisions sur le programme demandé :
1.	La liste de nombre doit être construite en demandant à l'utilisateur d'entrer 
    les nombres un à un, jusqu'à ce que l'utilisateur entre le mot 'stop'. Vous 
    n'avez pas besoin de faire la validation d'entrée sur les nombres.
2.	Votre programme doit ensuite trouver la liste de tous les diviseurs de chacun 
    des nombres de la liste
3.	Le programme doit retourner le résultat sous la forme d'un dictionnaire où les 
    clés sont les nombres entrés par l'utilisateur et les valeurs sont les listes 
    des diviseurs.

### Exemple #1
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 22
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 55
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 44
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 12
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 52
Veuillez entrer un nombre (ou 'stop' pour arrêter) : stop
Résultat : 
{22: [1, 2, 11, 22], 55: [1, 5, 11, 55], 44: [1, 2, 4, 11, 22, 44], 12: [1, 2, 3, 4, 6, 12], 52: [1, 2, 4, 13, 26, 52]}

### Exemple #2
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 24
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 48
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 12
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 4
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 2
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 1
Veuillez entrer un nombre (ou 'stop' pour arrêter) : stop
Résultat : 
{24: [1, 2, 3, 4, 6, 8, 12, 24], 48: [1, 2, 3, 4, 6, 8, 12, 16, 24, 48], 12: [1, 2, 3, 4, 6, 12], 4: [1, 2, 4], 2: [1, 2], 1: [1]}

### Exemple #3
Veuillez entrer un nombre (ou 'stop' pour arrêter) : stop
Résultat : 
{}

### Exemple #4
Veuillez entrer un nombre (ou 'stop' pour arrêter) : 0
Veuillez entrer un nombre (ou 'stop' pour arrêter) : stop
Résultat :
{0: []}
"""
#TODO commencer votre programme

dictionnaire = {}
while True:
    nombre = input("Veuillez entrer un nombre (ou 'stop' pour arrêter) : ")
    if nombre == "stop":
        break
    else:
        nombre = int(nombre)
        diviseurs = []
        for i in range(1, abs(nombre) + 1):
            if nombre % i == 0:
                diviseurs.append(i)
        dictionnaire[nombre] = diviseurs

#il faut que ça marche avec des nombres negatifs aussi, donc on peut utiliser la valeur absolue du nombre pour trouver les diviseurs
print("Résultat : ")
print(dictionnaire)