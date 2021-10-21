import json_helper


def test():

    # Création d'un JsonHelper
    jh = json_helper.JsonHelper()

    # Les données à écrire
    data_1 = {
        'key_1': [
            [1, 0, 5],
            [1, 0, 5],
            [1, 0, 5]
        ],
        'key_2': [0.11, 0.11, 0.11]
    }

    # Le nom du fichier de test
    test_file = 'json-helper-test.json'

    # Test d'écriture
    jh.save(data_1, test_file)

    # Test de lecture
    data_2 = jh.load(test_file)

    # Resultats des tests

    print(data_1)
    print(data_2)

    if data_1 == data_2:
        result = 'OK'
    else:
        result = 'ERROR'

    print(result)


test()