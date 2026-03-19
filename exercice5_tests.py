from time import time
from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

def test():
    fichier="exercice5"
    
    cas1=TestCaseWholeFile(
        test_name="Test1 - Example 1", 
        filename=fichier, 
        mock_input=["1 2 3 1", "2"], 
        expected_output=["Résultat : 1 (Deux plus grands indices : 0 et 3. Somme 3 > 2)"], 
        timeout=1
    )

    cas2=TestCaseWholeFile(
        test_name="Test2 - Example 2", 
        filename=fichier, 
        mock_input=["1 2 3", "5"], 
        expected_output=["Résultat : Aucun duplicata ne respecte la condition."], 
        timeout=1
    )

    cas3=TestCaseWholeFile(
        test_name="Test3 - Example 3", 
        filename=fichier, 
        mock_input=["5 5 5", "1"], 
        expected_output=["Résultat : 5 (Deux plus grands indices : 1 et 2. Somme 3 > 1)"], 
        timeout=1
    )

    cas4=TestCaseWholeFile(
        test_name="Test4 - Multiple duplicates", 
        filename=fichier, 
        mock_input=["1 2 1 2 1", "4"], 
        expected_output=["Résultat : 1 (Deux plus grands indices : 2 et 4. Somme 6 > 4)"], 
        timeout=1
    )

    cas5=TestCaseWholeFile(
        test_name="Test5 - No duplicates", 
        filename=fichier, 
        mock_input=["1 2 3 4 5", "10"], 
        expected_output=["Résultat : Aucun duplicata ne respecte la condition."], 
        timeout=1
    )

    cas6=TestCaseWholeFile(
        test_name="Test6 - All same number", 
        filename=fichier, 
        mock_input=["7 7 7 7", "0"], 
        expected_output=["Résultat : 7 (Deux plus grands indices : 2 et 3. Somme 5 > 0)"], 
        timeout=1
    )

    cas7=TestCaseWholeFile(
        test_name="Test7 - Invalid list input then valid", 
        filename=fichier, 
        mock_input=["abc def", "1 2 3 1", "2"], 
        expected_output=["Erreur : veuillez entrer des nombres valides séparés par des espaces.", "Résultat : 1 (Deux plus grands indices : 0 et 3. Somme 3 > 2)"], 
        timeout=1
    )

    cas8=TestCaseWholeFile(
        test_name="Test8 - Empty list then valid", 
        filename=fichier, 
        mock_input=["", "5 5 5", "1"], 
        expected_output=["Erreur : veuillez entrer des nombres valides séparés par des espaces.", "Résultat : 5 (Deux plus grands indices : 1 et 2. Somme 3 > 1)"], 
        timeout=1
    )

    cas9=TestCaseWholeFile(
        test_name="Test9 - Invalid k then valid", 
        filename=fichier, 
        mock_input=["1 2 3 1", "abc", "2"], 
        expected_output=["Erreur : veuillez entrer un nombre entier valide.", "Résultat : 1 (Deux plus grands indices : 0 et 3. Somme 3 > 2)"], 
        timeout=1
    )

    cas10=TestCaseWholeFile(
        test_name="Test10 - Multiple invalid lists then valid", 
        filename=fichier, 
        mock_input=["", "2 abs", "5 5 5", "1"], 
        expected_output=["Erreur : veuillez entrer des nombres valides séparés par des espaces.", "Erreur : veuillez entrer des nombres valides séparés par des espaces.", "Résultat : 5 (Deux plus grands indices : 1 et 2. Somme 3 > 1)"], 
        timeout=1
    )

    cas11=TestCaseWholeFile(
        test_name="Test11 - Multiple invalid ks then valid", 
        filename=fichier, 
        mock_input=["5 5 5", ".", "", " ", "1"], 
        expected_output=["Erreur : veuillez entrer un nombre entier valide.",
                         "Erreur : veuillez entrer un nombre entier valide.",
                         "Erreur : veuillez entrer un nombre entier valide.",
                        "Résultat : 5 (Deux plus grands indices : 1 et 2. Somme 3 > 1)"], 
        timeout=1
    )

    cas12=TestCaseWholeFile(
        test_name="Test12 - Negative k", 
        filename=fichier, 
        mock_input=["5 5 5", "-1"], 
        expected_output=["Résultat : 5 (Deux plus grands indices : 1 et 2. Somme 3 > -1)"], 
        timeout=1
    )

    cas13=TestCaseWholeFile(
        test_name="Test12 - Strictly equal to k", 
        filename=fichier, 
        mock_input=["1 1 5", "1"], 
        expected_output=["Résultat : Aucun duplicata ne respecte la condition."], 
        timeout=1
    )

    suite=TestSuite([cas1, cas2, cas3, cas4, cas5, cas6, cas7, cas8, cas9, cas10, cas11, cas12, cas13], valeur_test=2)
    return suite.get_test_result()

if __name__== "__main__":
    test()
