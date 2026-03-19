from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

file = "exercice1"

cas1 = TestCaseWholeFile(
    test_name="Test1",
    filename=file,
    mock_input=['Un chat chasse.'],
    expected_output=["Résultat : {'a': ['chasse', 'chat'], 'c': ['chasse', 'chat'], 'e': ['chasse'], 'h': ['chasse', 'chat'], 'n': ['un'], 's': ['chasse'], 't': ['chat'], 'u': ['un']}"],
    timeout=1
)
cas2 = TestCaseWholeFile(
    test_name="Test2",
    filename=file,
    mock_input=["Allo allo"],
    expected_output=["Résultat : {'a': ['allo'], 'l': ['allo'], 'o': ['allo']}"],
    timeout=1
)
cas3 = TestCaseWholeFile(
    test_name="Test3",
    filename=file,
    mock_input=["Bonjour le monde"],
    expected_output=["Résultat : {'b': ['bonjour'], 'd': ['monde'], 'e': ['le', 'monde'], 'j': ['bonjour'], 'l': ['le'], 'm': ['monde'], 'n': ['bonjour', 'monde'], 'o': ['bonjour', 'monde'], 'r': ['bonjour'], 'u': ['bonjour']}"],
    timeout=1
)
cas4 = TestCaseWholeFile(
    test_name="Test4",
    filename=file,
    mock_input=["Python"],
    expected_output=["Résultat : {'h': ['python'], 'n': ['python'], 'o': ['python'], 'p': ['python'], 't': ['python'], 'y': ['python']}"],
    timeout=1
)

cas5 = TestCaseWholeFile(
    test_name="Test5 - Empty phrase",
    filename=file,
    mock_input=[""],
    expected_output=["Résultat : {}"],
    timeout=1
)

cas6 = TestCaseWholeFile(
    test_name="Test6 - Only punctuation",
    filename=file,
    mock_input=[".,?!"],
    expected_output=["Résultat : {}"],
    timeout=1
)

cas7 = TestCaseWholeFile(
    test_name="Test7 - Numbers in text",
    filename=file,
    mock_input=["abc123 xyz789"],
    expected_output=["Résultat : {'a': ['abc123'], 'b': ['abc123'], 'c': ['abc123'], 'x': ['xyz789'], 'y': ['xyz789'], 'z': ['xyz789']}"],
    timeout=1
)

cas8 = TestCaseWholeFile(
    test_name="Test8 - Aprostophes in text",
    filename=file,
    mock_input=["L'avion vole !"],
    expected_output=["""Résultat : {'a': ["l'avion"], 'e': ['vole'], 'i': ["l'avion"], 'l': ["l'avion", 'vole'], 'n': ["l'avion"], 'o': ["l'avion", 'vole'], 'v': ["l'avion", 'vole']}"""],
    timeout=1
)

cas9 = TestCaseWholeFile(
    test_name="Test9 - Case sensitive",
    filename=file,
    mock_input=["Chat chat CHAT"],
    expected_output=["Résultat : {'a': ['chat'], 'c': ['chat'], 'h': ['chat'], 't': ['chat']}"],
    timeout=1
)

cas10 = TestCaseWholeFile(
    test_name="Test10 - Only numbers",
    filename=file,
    mock_input=["1213 12314 213"],
    expected_output=["Résultat : {}"],
    timeout=1
)

test.add_tests_cases(cas1, cas2, cas3, cas4, cas5, cas6, cas7, cas8, cas9, cas10)

# run la série de test
test()