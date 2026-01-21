def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    # cancella pass e scrivi il tuo codice
    dict3: dict = {}

    for key1, value1 in dict1.items():
        dict3[key1]=value1
    for key2, value2 in dict2.items():
        if key2 in dict3:
            dict3[key2] += value2
        else:
            dict3[key2] = value2

    return dict3