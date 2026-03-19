from time import time
from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

def test():
    fichier="exercice6"

    cas1=TestCaseWholeFile(
        test_name="Test1", 
        filename=fichier, 
        mock_input=["22", "55", "44", "12", "52", "stop"], 
        expected_output=["Résultat :", "{22: [1, 2, 11, 22], 55: [1, 5, 11, 55], 44: [1, 2, 4, 11, 22, 44], 12: [1, 2, 3, 4, 6, 12], 52: [1, 2, 4, 13, 26, 52]}"], 
        timeout=1
    )

    cas2=TestCaseWholeFile(
        test_name="Test2", 
        filename=fichier, 
        mock_input=["24", "48", "12", "4", "2", "1", "0", "stop"], 
        expected_output=["Résultat :", "{24: [1, 2, 3, 4, 6, 8, 12, 24], 48: [1, 2, 3, 4, 6, 8, 12, 16, 24, 48], 12: [1, 2, 3, 4, 6, 12], 4: [1, 2, 4], 2: [1, 2], 1: [1], 0: []}"], 
        timeout=1
    )

    cas3=TestCaseWholeFile(
        test_name="Test3", 
        filename=fichier, 
        mock_input=["128", "156", "1024", "3", "233", "stop"], 
        expected_output=["Résultat :", "{128: [1, 2, 4, 8, 16, 32, 64, 128], 156: [1, 2, 3, 4, 6, 12, 13, 26, 39, 52, 78, 156], 1024: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], 3: [1, 3], 233: [1, 233]}"], 
        timeout=1
    )

    cas4=TestCaseWholeFile(
        test_name="Test4", 
        filename=fichier, 
        mock_input=["stop"], 
        expected_output=["Résultat :", "{}"], 
        timeout=1
    )

    cas5=TestCaseWholeFile(
        test_name="Test5 - Single number", 
        filename=fichier, 
        mock_input=["15", "stop"], 
        expected_output=["Résultat :", "{15: [1, 3, 5, 15]}"], 
        timeout=1
    )

    cas6=TestCaseWholeFile(
        test_name="Test6 - Prime number", 
        filename=fichier, 
        mock_input=["17", "stop"], 
        expected_output=["Résultat :", "{17: [1, 17]}"], 
        timeout=1
    )

    cas7=TestCaseWholeFile(
        test_name="Test7 - Negative number", 
        filename=fichier, 
        mock_input=["-12", "stop"], 
        expected_output=["Résultat :", "{-12: [1, 2, 3, 4, 6, 12]}"], 
        timeout=1
    )

    cas8=TestCaseWholeFile(
        test_name="Test8 - Invalid input then valid", 
        filename=fichier, 
        mock_input=["abc", "xyz", "12", "stop"], 
        expected_output=["Erreur : veuillez entrer un nombre entier valide ou 'stop'.", "Erreur : veuillez entrer un nombre entier valide ou 'stop'.", "Résultat :", "{12: [1, 2, 3, 4, 6, 12]}"], 
        timeout=1
    )

    cas9=TestCaseWholeFile(
        test_name="Test9 - Mix of valid and invalid inputs", 
        filename=fichier, 
        mock_input=["10", "invalid", "20", "not_a_number", "stop"], 
        expected_output=["Erreur : veuillez entrer un nombre entier valide ou 'stop'.", "Erreur : veuillez entrer un nombre entier valide ou 'stop'.", "Résultat :", "{10: [1, 2, 5, 10], 20: [1, 2, 4, 5, 10, 20]}"], 
        timeout=1
    )

    cas10=TestCaseWholeFile(
        test_name="Test10 - Decimal number input", 
        filename=fichier, 
        mock_input=["3.14", "5", "stop"], 
        expected_output=["Erreur : veuillez entrer un nombre entier valide ou 'stop'.", "Résultat :", "{5: [1, 5]}"], 
        timeout=1
    )

    suite=TestSuite([cas1, cas2, cas3, cas4, cas5, cas6, cas7], valeur_test=3)
    return suite.get_test_result()

if __name__== "__main__":
    test()