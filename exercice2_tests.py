from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

file = "exercice2"

cas1 = TestCaseWholeFile(
    test_name="Test1",
    filename=file,
    mock_input=['Bonjour je je suis un un un homme'],
    expected_output=["Résultat : {'bonjour': 1, 'je': 2, 'suis': 1, 'un': 3, 'homme': 1}"],
    timeout=1
)

cas2 = TestCaseWholeFile(
    test_name="Test2",
    filename=file,
    mock_input=["Ceci est une phrase tellement redondante que l'on pourrait dire que c'est une phrase redondante."],
    expected_output=["Résultat : {'ceci': 1, 'est': 1, 'une': 2, 'phrase': 2, 'tellement': 1, 'redondante': 2, 'que': 2, \"l'on\": 1, 'pourrait': 1, 'dire': 1, \"c'est\": 1}"],
    timeout=1
)

cas3 = TestCaseWholeFile(
    test_name="Test3",
    filename=file,
    mock_input=["Il s'agit de la seule province canadienne à avoir le français comme seule langue officielle"],
    expected_output=["Résultat : {'il': 1, \"s'agit\": 1, 'de': 1, 'la': 1, 'seule': 2, 'province': 1, 'canadienne': 1, 'à': 1, 'avoir': 1, 'le': 1, 'français': 1, 'comme': 1, 'langue': 1, 'officielle': 1}"],
    timeout=1
)

cas4 = TestCaseWholeFile(
    test_name="Test4",
    filename=file,
    mock_input=['OKAY okay OKaY OkAY OKAY OKAY'],
    expected_output=["Résultat : {'okay': 6}"],
    timeout=1
)

cas5 = TestCaseWholeFile(
    test_name="Test5 - Empty string",
    filename=file,
    mock_input=[''],
    expected_output=["Résultat : {}"],
    timeout=1
)

cas6 = TestCaseWholeFile(
    test_name="Test6 - Only punctuation",
    filename=file,
    mock_input=['.,.,.,'],
    expected_output=["Résultat : {}"],
    timeout=1
)

cas7 = TestCaseWholeFile(
    test_name="Test7 - Single word",
    filename=file,
    mock_input=['Hello'],
    expected_output=["Résultat : {'hello': 1}"],
    timeout=1
)

cas8 = TestCaseWholeFile(
    test_name="Test8 - Numbers in word",
    filename=file,
    mock_input=["Hello1 Hello2 Hello2 Hello1'"],
    expected_output=["""Résultat : {'hello1': 1, 'hello2': 2, "hello1'": 1}"""],
    timeout=1
)

cas9 = TestCaseWholeFile(
    test_name="Test9 - Remove . and ,",
    filename=file,
    mock_input=["Hello, Hello. Hello"],
    expected_output=["Résultat : {'hello': 3}"],
    timeout=1
)

test.add_tests_cases(cas1, cas2, cas3, cas4, cas5, cas6, cas7, cas8, cas9)

# run la série de test
test()
