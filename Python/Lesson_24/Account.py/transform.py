def transform(x: int) -> int:
    # cancella pass e scrivi il tuo codice
    if x % 2 == 0:
        x //= 2
        return x
    else:
        x *= 3
        x -= 1
        return x