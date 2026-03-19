from utils_ne_pas_supprimer import TestSuite, TestCaseWholeFile

test = TestSuite()

fichier = "exercice3"

cas1=TestCaseWholeFile(
    test_name="Exemple 1",
    filename=fichier,
    mock_input=['Paris Rome Tokyo', 'Paris Berlin Londres', 'Paris Tokyo Madrid'], 
    expected_output=["Destinations communes : paris"]
)

cas2=TestCaseWholeFile(
    test_name="Exemple 2",
    filename=fichier,
    mock_input=['Lyon Alger', 'Lyon Alger', 'Alger Lyon'],
    expected_output=["Destinations communes : alger lyon"]
)

cas3=TestCaseWholeFile(
    test_name="Exemple 3",
    filename=fichier,
    mock_input=['Paris Rome', 'Londres Berlin', 'Tokyo Madrid'],
    expected_output=["Destinations communes :"]
)

cas4=TestCaseWholeFile(
    test_name="Exemple 4",
    filename=fichier,
    mock_input=['Montreal Quebec Toronto', 'Montreal Quebec Vancouver', 'Montreal Quebec'],
    expected_output=["Destinations communes : montreal quebec"]
)

cas5=TestCaseWholeFile(
    test_name="Empty input",
    filename=fichier,
    mock_input=['', '', ''],
    expected_output=["Destinations communes :"]
)

cas6=TestCaseWholeFile(
    test_name="Single destination each",
    filename=fichier,
    mock_input=['Paris', 'Paris', 'Paris'],
    expected_output=["Destinations communes : paris"]
)

cas7=TestCaseWholeFile(
    test_name="Case insensitive",
    filename=fichier,
    mock_input=['Lyon', 'lyOn', 'LYON'],
    expected_output=["Destinations communes : lyon"]
)

cas8=TestCaseWholeFile(
    test_name="Repeated destination",
    filename=fichier,
    mock_input=['Lyon lyon Lyon', 'lyOn LYON lyon', 'LYON LYON LYON'],
    expected_output=["Destinations communes : lyon"]
)

cas9=TestCaseWholeFile(
    test_name="Only number and punctuation",
    filename=fichier,
    mock_input=['1, 2 3', '. 1, :', '% 22 1,'],
    expected_output=["Destinations communes : 1,"]
)

test.add_tests_cases(cas1, cas2, cas3, cas4, cas5, cas6, cas7, cas8, cas9)


if __name__== "__main__":
    test()
