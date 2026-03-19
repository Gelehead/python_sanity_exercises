__author__ = "Kodjo Joshua-Mercy N'tsougan"

import threading
import _thread
import unittest
from unittest.mock import patch
from typing import List
from io import StringIO
from collections import deque
import sys
import importlib
import ast
import re

# Dictionnaire global pour mettre en cache les modules importés
module = dict()

# --- Classes de validation (de utils_ne_pas_supprimer2.py) ---

class Equal:
    """Valide si la valeur testée est exactement égale à la valeur attendue."""
    def __init__(self, expected):
        self.expected = expected

    def validate(self, unittest_instance, value_to_test, fail_message: str):
        unittest_instance.assertEqual(value_to_test, self.expected, fail_message)

class AlmostEqualNumber:
    """
    Valide si les nombres flottants dans une chaîne de caractères sont
    presque égaux à ceux attendus, selon une précision définie.
    """
    def __init__(self, expected: str, precisions: List):
        self.expected = expected
        self.precisions = precisions

    def validate(self, unittest_instance, value_to_test, fail_message):
        regex_pattern = r"[-+]?(?:\d*\.\d+|\d+)"
        expected_numbers = re.findall(regex_pattern, self.expected)

        if len(self.precisions) != len(expected_numbers):
            raise Exception("Precision manquante dans la definition du test.")

        result_numbers = re.findall(regex_pattern, value_to_test)

        if len(expected_numbers) != len(result_numbers):
            message = f'La sortie de votre programme contient {len(result_numbers)} float. Vous devez avoir {len(expected_numbers)} float'
            raise Exception(message)

        for expected_number, result_number, precision in zip(expected_numbers, result_numbers, self.precisions):
            try:
                unittest_instance.assertAlmostEqual(float(expected_number), float(result_number), precision, fail_message)
            except ValueError:
                raise Exception("Impossible de convertir en float")

# --- Classe de test pour un fichier complet (fusion des 3 fichiers) ---

class TestCaseWholeFile(unittest.TestCase):
    """
    Cas de test qui exécute un fichier Python complet et compare sa sortie
    à une sortie attendue.
    """
    # AJOUTÉ : Liste pour la collecte automatique des tests pour run_test()
    tests_case = []

    def __init__(self, test_name: str, filename: str, mock_input: List, expected_output: List, timeout: float = 1, fail_message: str = None, modeStartsWith: bool = False, modeDict: bool = False):
        super(TestCaseWholeFile, self).__init__()
        self.shortDescription = lambda: test_name
        self.file = filename
        self.mock_input = mock_input
        self.expected_output = expected_output
        self.timeout = timeout
        self.fail_message = fail_message
        self.modeStartsWith = modeStartsWith
        self.modeDict = modeDict
        # AJOUTÉ : Ajout automatique de l'instance de test à la liste
        TestCaseWholeFile.tests_case.append(self)


    def run_whole_file(self):
        """Importe ou recharge le module à tester."""
        if self.file not in module:
            module[self.file] = importlib.import_module(self.file)
        else:
            importlib.reload(module[self.file])

    def override_input(self):
        """Remplace la fonction `input` standard pour simuler une entrée utilisateur."""
        queue = deque(self.mock_input)

        def fake_input(*args):
            if not queue:
                raise Exception("Vous avez appelé input trop souvent. Vérifiez votre code")
            return queue.popleft()
        return fake_input

    def runTest(self):
        """Exécute le test principal."""
        @patch('builtins.input', self.override_input())
        def exec_test():
            timer = None
            try:
                out = StringIO()
                sys.stdout = out
                if self.timeout is not None:
                    timer = threading.Timer(self.timeout, lambda: _thread.interrupt_main())
                    timer.start()

                self.run_whole_file()
                output = [line.strip() for line in out.getvalue().strip().splitlines()]

                if len(output) != len(self.expected_output):
                    message = f'La sortie de votre programme contient {len(output)} lignes. Vous devez avoir {len(self.expected_output)} lignes'
                    raise Exception(message)
                
                is_validator_mode = self.expected_output and hasattr(self.expected_output[0], 'validate')

                for result, expected in zip(output, self.expected_output):
                    if is_validator_mode:
                        expected.validate(self, result, self.fail_message)
                    elif self.modeStartsWith:
                        self.assertTrue(result.startswith(expected), msg=f"\n\nVoulu: '{expected}',\nVotre code: '{result}'\nLes décimales exactes ne sont pas importantes.")
                    elif self.modeDict:
                        self.assertDictEqual(ast.literal_eval(result), expected)
                    else:
                        self.assertEqual(result, expected, self.fail_message)

            except KeyboardInterrupt:
                raise Exception(f'Votre programme n\'a pas terminé son exécution dans le temps alloué de {self.timeout} seconde(s). Vous êtes peut-être dans une boucle infinie.')
            finally:
                sys.stdout = sys.__stdout__
                if timer is not None:
                    timer.cancel()
        exec_test()

# --- Classe de test basique (fusion des 3 fichiers) ---

class BasicTestCase(unittest.TestCase):
    """
    Cas de test qui compare le résultat d'une fonction à une valeur attendue.
    """
    # AJOUTÉ : Liste pour la collecte automatique des tests pour run_test()
    tests_case = []

    def __init__(self, test_name: str, result_func, expected_result, timeout: float, fail_message: str = None):
        super(BasicTestCase, self).__init__()
        self.shortDescription = lambda: test_name
        self.result_func = result_func
        self.expected_result = expected_result
        self.timeout = timeout
        self.fail_message = fail_message
        # AJOUTÉ : Ajout automatique de l'instance de test à la liste
        BasicTestCase.tests_case.append(self)


    def runTest(self):
        timer = None
        try:
            if self.timeout is not None:
                timer = threading.Timer(self.timeout, lambda: _thread.interrupt_main())
                timer.start()
            self.assertEqual(self.expected_result, self.result_func(), self.fail_message)
        except KeyboardInterrupt:
            raise Exception(f'Votre programme n\'a pas terminé son exécution dans le temps alloué de {self.timeout} seconde(s). Vous êtes peut-être dans une boucle infinie.')
        finally:
            if timer is not None:
                timer.cancel()

# --- Suite de tests (fusion des 3 fichiers) ---

class TestSuite:
    """
    Gère une collection de cas de test et peut les exécuter et calculer un pointage.
    """
    def __init__(self, cases=None, valeur_test=None):
        self.point_exercice = 0 if valeur_test is None else valeur_test
        self.suite = unittest.TestSuite()
        if cases:
            self.suite.addTests(cases)

    def add_tests_cases(self, *cases):
        """Ajoute des cas de test à la suite."""
        self.suite.addTests(cases)

    def get_test_result(self):
        """Exécute les tests et retourne un pointage basé sur les erreurs."""
        runner = unittest.TextTestRunner(verbosity=0)
        test_result = runner.run(self.suite)
        number_of_case = self.suite.countTestCases()
        if number_of_case == 0:
            return 0.0
        number_of_error = len(test_result.failures) + len(test_result.errors)
        point_per_error = self.point_exercice / number_of_case
        return round(self.point_exercice - (number_of_error * point_per_error), 2)

    def __call__(self):
        """Rend la suite de tests exécutable directement."""
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(self.suite)

# --- AJOUTÉ : La fonction run_test() manquante ---
def run_test():
    """
    Fonction simple pour exécuter tous les tests automatiquement collectés.
    """
    suite = unittest.TestSuite()
    # Collecte les tests depuis les listes de classe
    suite.addTests(BasicTestCase.tests_case)
    suite.addTests(TestCaseWholeFile.tests_case)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)