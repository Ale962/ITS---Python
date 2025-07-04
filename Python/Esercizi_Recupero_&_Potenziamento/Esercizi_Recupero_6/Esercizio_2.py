import math
def nomi() -> None:
    nomi: list[str] = []
    while len(nomi) <= 30:
        print()
        nome = input('Write rhe name here: ')
        if nome in nomi:
            print()
            print('Nome già usato, non sono ammessi duplicati')
            break
        elif len(nome) >= 20:
            print()
            print('Non sono ammessi nomi con un numero di caretteri superiore a 20')
            break
        elif nome == '':
            print()
            print('Non sono ammesse stringhe vuote come nomi')
            break
        else:
            nomi.append(nome)

    max_len = -math.inf
    max_str = ''

    for n in nomi:
        if len(n) > max_len:
            max_len = len(n)
            max_str = n
    print('----------------'*4)
    print(f'Sono stati inseriti in totale {len(nomi)} nomi distinti')
    print(f'Il nome più lungo ha lunghezza {max_len} ed è {max_str}')
    print('----------------'*4)

if __name__ == '__main__':
    nomi()