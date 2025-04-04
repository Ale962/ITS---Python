def prime_factors(n: int) -> list[int]:
    
    pf_list: list[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    n_pf_list: list[int] = []

    while n > 1:

        for x in pf_list:
        
            if n % x == 0:
                n_pf_list.append(x)
                n = n / x
        
        

    
    print(n_pf_list)
    return n_pf_list

prime_factors(52)