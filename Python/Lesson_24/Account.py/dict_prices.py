def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    # cancella pass e scrivi il tuo codice
    filter_products: dict[str: float] = {}

    for product, price in prodotti.items():
        if price > 20:
            price *= 0.9
            filter_products[product] = price
    
    return filter_products