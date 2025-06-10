# Exercise 5

'''
Validazione di un Indirizzo IPv4
Scrivi una funzione is_valid_ipv4(address: str) -> bool che determina se una
stringa è un indirizzo IPv4 valido. Un indirizzo IPv4 è composto da quattro numeri decimali
(ciascuno da 0 a 255) separati da punti (.). Gli zeri iniziali sono consentiti (ad esempio
192.168.001.001 è valido), ma ciascuna delle quattro parti deve essere compresa tra 0 e
255 e non deve contenere caratteri o spazi aggiuntivi.
Requisiti:
● Se non ci sono esattamente tre punti o non ci sono quattro parti numeriche,
restituisci False.
● Ciascuna parte deve contenere solo cifre (isdigit()) e, convertita in intero, deve
essere nel range [0,255][0,255][0,255].
Esempi:
is_valid_ipv4("192.168.0.1") # True
is_valid_ipv4("255.255.255.255") # True
is_valid_ipv4("256.100.10.1") # False (256 è fuori range)
is_valid_ipv4("192.168.1") # False (solo 3 parti)
is_valid_ipv4("192.168.1.a") # False (parte non numerica)

'''
import string

def is_valid_ipv4(adress: str) -> bool:

    # Check docs number
    doc_counter = 0
    for p in adress:
        if p == '.':
            doc_counter += 1
    if doc_counter != 3:
        return False
    # Check numbers present
    parts: list[str] = adress.split('.')
    if len(parts) != 4:
        return False
    # Check if number are in given range and are valid character
    for num in parts:

        if not num.isdigit():
            return False
        
        n = int(num)
        
        if n in range(0, 256):
            continue
        else:
            return False
        
    return True

if __name__ == '__main__':

    print(is_valid_ipv4("192.168.0.1")) # True
    print(is_valid_ipv4("255.255.255.255")) # True
    print(is_valid_ipv4("256.100.10.1")) # False (256 è fuori range)
    print(is_valid_ipv4("192.168.1")) # False (solo 3 parti)
    print(is_valid_ipv4("192.168.1.a")) # False (parte non numerica)
    tests = [
        "192.168.0.1",        # True TIM server for modem
        "255.255.255.255",    # True
        "256.100.10.1",       # False (256 out of range)
        "192.168.1",          # False (only 3 parts)
        "192.168.1.a",        # False (non-numeric)
        "192.168..1",         # False (empty part)
        "192.168.01.1",       # True (leading zero allowed)
        " 192.168.0.1 ",      # False (spaces not allowed)
        "0.0.0.0",            # True (lowest valid IP)
        "123.045.067.089",    # True (leading zeros allowed)
    ]

    for ip in tests:
        print(f"is_valid_ipv4({ip}) -> {is_valid_ipv4(ip)}")

        