__version__ =   "TP4 - Exercice #1"
__author__  =   "Nom eleve 1 (matricule 1), nom eleve 2 (matricule 2)"


"""
Écrire un programme qui demande une phrase à l'utilisateur puis affiche un dictionnaire 
contenant chaque lettre de l'alphabet présente dans la phrase comme clé, et la liste des 
mots (en minuscules, ordre alphabétique, sans doublons) contenant cette lettre comme valeur.

### Exemple #1:
Veuillez entrer une phrase : Un chat chasse.
Résultat : {'a': ['chat', 'chasse'], 'c': ['chat', 'chasse'], 'e': ['chasse'], 'h': ['chat', 'chasse'], 'n': ['un'], 's': ['chasse'], 't': ['chat'], 'u': ['un']}

### Exemple #2:
Veuillez entrer une phrase : Allo allo
Résultat : {'a': ['allo'], 'l': ['allo'], 'o': ['allo']}
"""
# TODO: Commencez votre programme ici

sentence = input("Veuillez entrer une phrase : ").lower().strip(".,?!")

dic = {}

# pour chaque mot dans la phrase
for word in sentence.split(" ") :
    # pour chaque _lettre_ minuscule dans mor 
    for letter in [''.join(e for e in x if e.isalpha()) for x in word] : 
        # ajouter le mot si : pas dans dic, pas vide, pas deja associe a une lettre
        if letter == "" : continue
        if letter not in dic :
            dic[letter] = [word] 
        else :
            if word in dic[letter] :
                continue
            else : 
                dic[letter].append(word)

# trier les entrees du dictionnaire
for i in dic.items() : 
    dic[i[0]] = sorted(i[1])

# trier les clefs du dicitonnaire
dic = dict(sorted(dic.items()))

print("Résultat :", dic)





















# 67