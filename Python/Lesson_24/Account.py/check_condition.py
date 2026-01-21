def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:

    if conditionA or (conditionB and conditionC):
        return f'Operazione permessa'
    else:
        return f'Operazione negata'