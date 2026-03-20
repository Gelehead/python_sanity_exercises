__version__ =   "TP4 - Exercice #5"
__author__  =   "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"


"""
Écrire un programme qui identifie la "distance" entre des éléments identiques.

- Demandez une liste de nombres et une valeur cible k.
- Cherchez s'il existe des nombres identiques dans la liste dont la somme de leurs indices 
  est strictement supérieure à k.
- S'il y a plus de deux occurrences, utilisez les deux plus grands indices.
- Affichez le premier nombre trouvé respectant cette condition.

### Exemple #1
Entrez la liste de nombres : 1 2 3 1
Entrez la valeur k : 2
Résultat : 1 (Indices de 1 : 0 et 3. Somme 3 > 2)

### Exemple #2
Entrez la liste de nombres : 1 2 3
Entrez la valeur k : 5
Résultat : Aucun duplicata ne respecte la condition.

### Exemple #3
Entrez la liste de nombres : 5 5 5
Entrez la valeur k : 1
Résultat : 5 (Deux plus grands indices : 1 et 2. Somme 3 > 1)
"""

# TODO : Commencez votre code ici

while True:
    try:
        nums = list(map(int, input("Entrez la liste de nombres : ").split()))
        if nums: break
    except ValueError: pass
    print("Erreur : veuillez entrer des nombres valides séparés par des espaces.")

while True:
    try: k = int(input("Entrez la valeur k : ")); break
    except ValueError: print("Erreur : veuillez entrer un nombre entier valide.")

idx = {}
for i, n in enumerate(nums): idx.setdefault(n, []).append(i)

res = next(((v, l[-2], l[-1]) for v, l in idx.items() if len(l) >= 2 and l[-2] + l[-1] > k), None)

print(f"Résultat : {res[0]} (Deux plus grands indices : {res[1]} et {res[2]}. Somme {res[1]+res[2]} > {k})" if res else "Résultat : Aucun duplicata ne respecte la condition.")