from time import time
from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

def test():
    fichier="exercice4"
    cas1=TestCaseWholeFile(
        test_name="Test1", 
        filename=fichier, 
        mock_input=["2", "Lewis", "18", "Max", "19"], 
        expected_output=["Classement :", "('Lewis', 18)", "('Max', 19)"], 
        timeout=1
    )

    cas2=TestCaseWholeFile(
        test_name="Test2", 
        filename=fichier, 
        mock_input=["3", "Charles", "15", "Lando", "10", "Carlos", "12"], 
        expected_output=["Classement :", "('Lando', 10)", "('Carlos', 12)", "('Charles', 15)"], 
        timeout=1
    )

    cas3=TestCaseWholeFile(
        test_name="Test3", 
        filename=fichier, 
        mock_input=["-1", "2", "Alice", "5", "Bob", "3"], 
        expected_output=["Classement :", "('Bob', 3)", "('Alice', 5)"], 
        timeout=1
    )

    cas4=TestCaseWholeFile(
        test_name="Test4", 
        filename=fichier, 
        mock_input=["3", "Pierre", "22", "-1", "10", "Marie", "8", "Jean", "15"], 
        expected_output=["Classement :", "('Marie', 8)", "('Pierre', 10)", "('Jean', 15)"], 
        timeout=1
    )

    cas5=TestCaseWholeFile(
        test_name="Test5 - Invalid number of pilots", 
        filename=fichier, 
        mock_input=["abc", "-5", "0", "1", "Alice", "15"], 
        expected_output=["Classement :", "('Alice', 15)"], 
        timeout=1
    )

    cas6=TestCaseWholeFile(
        test_name="Test6 - Invalid scores", 
        filename=fichier, 
        mock_input=["2", "Bob", "abc", "25", "10", "Carol", "-5", "5"], 
        expected_output=["Classement :", "('Carol', 5)", "('Bob', 10)"], 
        timeout=1
    )

    cas7=TestCaseWholeFile(
        test_name="Test6 - valid scores (limits)", 
        filename=fichier, 
        mock_input=["2", "Bob", "0", "Carol", "20"], 
        expected_output=["Classement :", "('Bob', 0)", "('Carol', 20)"], 
        timeout=1
    )

    suite=TestSuite([cas1, cas2, cas3, cas4, cas5, cas6, cas7], valeur_test=6)
    return suite.get_test_result()

if __name__== "__main__":
    test()
