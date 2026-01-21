def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    # prima cancella ... e definisci parametro e tipo per il dato mancante
    # successivamente cancella pass e scrivi il tuo codice
    return sum(filter(lambda x : x > threshold, numbers))
    # return sum(map(lambda x : x if x > threshold else 0, numbers)) # alternative