# Esercizio 1

def isDNA(s: str) -> bool:
    DNA_SAMPLE_POOL = 'ACGT'
    is_dna: bool = True

    for l in s:
        if l in DNA_SAMPLE_POOL:
            continue
        else:
            is_dna = False

    return is_dna

def sovraposition(s1: str, s2: str) -> None:
    s1 = s1.upper()
    s2 = s2.upper()
    lenght = 0

    if isDNA(s1) and isDNA(s2):
        pass
    else:
        raise ValueError('One of the string is not a DNA')  
    
    l = s2[0]
    valid_index = 0
    for i, c in enumerate(s1):
        if c == l:
            current_index = i
            valid_index = 0
            current_length = 0
            for character in s1[current_index:]:
                
                if character == s2[valid_index]:
                    if valid_index >= len(s2):
                        break
                    else:
                        current_length += 1
                        valid_index += 1
                else:
                    break
            
            if current_length > lenght:
                lenght = current_length

    print('-------------'*3)
    print(f's1 = {s1}')
    print(f's2 = {s2}')
    print(f'La massima lunghezza è {lenght}')
    print('-------------'*3)


if __name__ == '__main__':
    s1 = 'TTACGAGTACGCTAGT'
    s2 = 'ACGCTAGTCCGA'

    sovraposition(s1, s2)