def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo 
    new_dict: dict[str: list[int]] = {}
    for x, y in tuples:
        if x not in new_dict:
            new_dict[x] = [y]
        else:
            new_dict[x].append(y)

    return new_dict