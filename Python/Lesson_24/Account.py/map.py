def frequency_dict(elements: list) -> dict:
    # cancella pass e scrivi il tuo codice

    counting_dict: dict = {}

    for x in elements:
        if x not in counting_dict:
            counting_dict[x] = 1
        else:
            counting_dict[x] += 1

    return counting_dict