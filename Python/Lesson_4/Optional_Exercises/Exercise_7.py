# Optional Exercise 7

'''
7. Roman Numeral Conversion:

    Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman numeral.

'''

def roman_conversion(n: int):

    if n in range(1, 4000):
        pass
    else: 
        raise ValueError("Number must be in the range beetwen 1 and 3999")
    
    roman_number =  ""

    if n < 4:
        roman_number = "I"*n
        return roman_number
    
    elif n < 10:

        if n == 4:
            roman_number = "I" + "V"
            return roman_number
        elif n == 9:
            roman_number = "I" + "X"
            return roman_number
        
        n -= 5
        roman_number = "V" + "I"*n
        return roman_number
    
    elif n < 50:
        x = n // 10
        v = (n-(10*x)) // 5
        i = (n-((10*x)+(5*v))) // 1

        if x == 4:
            if v == 1 and i == 4:
                roman_number = "X" + "L" + "I" + "X"
                return roman_number
            elif i == 4:
                roman_number = "X" + "L" + "I" + "V"
                return roman_number
            roman_number = "X" + "L" + ("V"*v) + ("I"*i)
            return roman_number
        
        if v == 1 and i == 4:
            roman_number = ("X"*x) + "I" + "X"
            return roman_number
        elif i == 4:
            roman_number = ("X"*x) + "I" + "V"
            return roman_number
        
        else:    
            roman_number = ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number
        
    elif n < 100:
        l = n // 50
        x = (n-(50*l)) // 10
        v = (n-((50*l)+(10*x))) // 5
        i = (n-((50*l)+(10*x)+(5*v))) // 1

        if  l == 1 and x == 4:
            if v == 1 and i == 4:
                roman_number = "X" + "C" + "I" + "X"
                return roman_number
            elif i == 4:
                roman_number = "X" + "C" + "I" + "V"
                return roman_number
            roman_number = "X" + "C" + ("V"*v) + ("I"*i)
            return roman_number    

        if v == 1 and i == 4:
            roman_number = ("L"*l) + ("X"*x) + "I" + "X"
            return roman_number
        elif i == 4:
            roman_number = ("L"*l) + ("X"*x) + "I" + "V"
            return roman_number
        
        else:    
            roman_number = ("L"*l) + ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number
    
    elif n < 500:
        c = n // 100
        l = (n-(100*c)) // 50
        x = (n-((100*c)+(50*l))) // 10
        v = (n-((100*c)+(50*l)+(10*x))) // 5
        i = (n-((100*c)+(50*l)+(10*x)+(5*v))) // 1

        if c == 4:
            if l == 1 and x == 4:
                if v == 1 and i == 4:
                    roman_number = "C" + "D" + "X" + "C" + "I" + "X"
                    return roman_number
                elif i == 4:
                    roman_number = "C" + "D" + "X" + "C" + "I" + "V"
                    return roman_number
                roman_number = "C" + "D" + "X" + "C" + ("V"*v) + ("I"*i)
                return roman_number
            elif x == 4:
                if v == 1 and i == 4:
                    roman_number = "C" + "D" + "X" + "L" + "I" + "X"
                    return roman_number
                elif i == 4:
                    roman_number = "C" + "D" + "X" + "L" + "I" + "V"
                    return roman_number
                roman_number = "C" + "D" + "X" + "L" + ("V"*v) + ("I"*i)
                return roman_number
            roman_number = "C" + "D" + ("L"*l) + ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number

        if l == 1 and x == 4:
            if v == 1 and i == 4:
                roman_number = ("C"*c) + "X" + "C" + "I" + "X"
                return roman_number
            elif i == 4:
                roman_number = ("C"*c) + "X" + "C" + "I" + "V"
                return roman_number
            roman_number = ("C"*c) + "X" + "C" + ("V"*v) + ("I"*i)
            return roman_number
        elif x == 4:
            if v == 1 and i == 4:
                roman_number = ("C"*c) + "X" + "L" + "I" + "X"
                return roman_number
            elif i == 4:
                roman_number = ("C"*c) + "X" + "L" + "I" + "V"
                return roman_number
            roman_number = ("C"*c) + "X" + "L" + ("V"*v) + ("I"*i)
            return roman_number
        
        if v == 1 and i == 4:
            roman_number = ("C"*c) + ("L"*l) + ("X"*x) + "I" + "X"
            return roman_number
        elif i == 4:
            roman_number = ("C"*c) + ("L"*l) + ("X"*x) + "I" + "V"
            return roman_number
        
        else:    
            roman_number = ("C"*c) + ("L"*l) + ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number
    
    elif n < 1000:
        d = n // 500
        c = (n-(500*d)) // 100
        l = (n-((500*d)+(100*c))) // 50
        x = (n-((500*d)+(100*c)+(50*l))) // 10
        v = (n-((500*d)+(100*c)+(50*l)+(10*x))) // 5
        i = (n-((500*d)+(100*c)+(50*l)+(10*x)+(5*v))) // 1

        if d == 1 and c == 4:
            if l == 1 and x == 4:
                if v == 1  and i == 4:
                    roman_number = "C" + "M" + "X" + "C" + "I" + "X"
                    return roman_number
                elif i == 4:
                    roman_number = "C" + "M" + "X" + "C" + "I" + "V"
                    return roman_number
                roman_number = "C" + "M" + "X" + "C" + ("V"*v) + ("I"*i)
                return roman_number
            elif x == 4:
                if v == 1 and i == 4:
                    roman_number = "C" + "M" + "X" + "L" + "I" + "X"
                    return roman_number
                elif i == 4:
                    roman_number = "C" + "M" + "X" + "L" + "I" + "V"
                    return roman_number
                roman_number = "C" + "M" + "X" + "L" + ("V"*v) + ("I"*i)
                return roman_number
            roman_number = "C" + "M" + ("L"*l) + ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number


        if l == 1 and x == 4:
            if v == 1 and i == 4:
                roman_number = ("D"*d) + ("C"*c) + "X" + "C" + "I" + "X"
                return roman_number
            elif i == 4:
                roman_number = ("D"*d) + ("C"*c) + "X" + "C" + "I" + "V"
                return roman_number
            roman_number = ("D"*d) + ("C"*c) + "X" + "C" + ("V"*v) + ("I"*i)
            return roman_number
        elif x == 4:
            if v == 1 and i == 4:
                roman_number = ("D"*d) + ("C"*c) + "X" + "L" + "I" + "X"
                return roman_number
            elif i == 4:
                roman_number = ("D"*d) + ("C"*c) + "X" + "L" + "I" + "V"
                return roman_number
            roman_number = ("D"*d) + ("C"*c) + "X" + "L" + ("V"*v) + ("I"*i)
            return roman_number
        
        if v == 1 and i == 4:
            roman_number = ("D"*d) + ("C"*c) + ("L"*l) + ("X"*x) + "I" + "X"
            return roman_number
        if i == 4:
            roman_number = ("D"*d) + ("C"*c) + ("L"*l) + ("X"*x) + "I" + "V"
            return roman_number
        
        else:
            roman_number = ("D"*d) + ("C"*c) + ("L"*l) + ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number
    
    else:
        m = n // 1000
        d = (n-(1000*m)) // 500
        c = (n-((1000*m)+(500*d))) // 100
        l = (n-((1000*m)+(500*d)+(100*c))) // 50
        x = (n-((1000*m)+(500*d)+(100*c)+(50*l))) // 10
        v = (n-((1000*m)+(500*d)+(100*c)+(50*l)+(10*x))) // 5
        i = (n-((1000*m)+(500*d)+(100*c)+(50*l)+(10*x)+(5*v))) // 1

        if d == 1 and c == 4:
            if l == 1 and x == 4:    
                if v == 1 and i == 4:
                    roman_number = ("M"*m) + "C" + "M" + "X" + "C" + "I" + "X"
                    return roman_number
                elif i == 4:
                    roman_number = ("M"*m) + "C" + "M" + "X" + "C" + "I" + "V"
                    return roman_number
                roman_number = ("M"*m) + "C" + "M" + "X" + "C" + ("V"*v) + ("I"*i)
                return roman_number
            elif x == 4:
                if v == 1 and i == 4:
                    roman_number = ("M"*m) + "C" + "M" + "X" + "L" + "I" + "X"
                    return roman_number
                elif i == 4:
                    roman_number = ("M"*m) + "C" + "M" + "X" + "L" + "I" + "V"
                    return roman_number
                roman_number = ("M"*m) + "C" + "M" + "X" + "L" + ("V"*v) + ("I"*i)
                return roman_number
            roman_number = ("M"*m) + "C" + "M" + ("L"*l) + ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number
        elif c == 4:
            if l == 1 and x == 4:    
                if v == 1 and i == 4:
                    roman_number = ("M"*m) + "C" + "D" + "X" + "C" + "I" + "X"
                    return roman_number
                elif i == 4:
                    roman_number = ("M"*m) + "C" + "D" + "X" + "C" + "I" + "V"
                    return roman_number
                roman_number = ("M"*m) + "C" + "D" + "X" + "C" + ("V"*v) + ("I"*i)
                return roman_number
            elif x == 4:
                if v == 1 and i == 4:
                    roman_number = ("M"*m) + "C" + "D" + "X" + "L" + "I" + "V"
                    return roman_number
                elif i == 4:
                    roman_number = ("M"*m) + "C" + "D" + "X" + "L" + "I" + "V"
                    return roman_number
                roman_number = ("M"*m) + "C" + "D" + "X" + "L" + ("V"*v) + ("I"*i)
                return roman_number
            roman_number = ("M"*m) + "C" + "D" + ("L"*l) + ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number


        if l == 1 and x == 4:
            if v == 1 and i == 4:
                roman_number = ("M"*m) + ("D"*d) + ("C"*c) + "X" + "C" + "I" + "X"
                return roman_number
            elif i == 4:
                roman_number = ("M"*m) + ("D"*d) + ("C"*c) + "X" + "C" + "I" + "V"
                return roman_number
            roman_number = ("M"*m) + ("D"*d) + ("C"*c) + "X" + "C" + ("V"*v) + ("I"*i)
            return roman_number
        elif x == 4:
            if v == 1 and i == 4:
                roman_number = ("M"*m) + ("D"*d) + ("C"*c) + "X" + "L" + "I" + "X"
                return roman_number
            elif i == 4:
                roman_number = ("M"*m) + ("D"*d) + ("C"*c) + "X" + "L" + "I" + "V"
                return roman_number
            roman_number = ("M"*m) + ("D"*d) + ("C"*c) + "X" + "L" + ("V"*v) + ("I"*i)
            return roman_number
        
        if v ==1 and i == 4:
            roman_number = ("M"*m) + ("D"*d) + ("C"*c) + ("L"*l) + ("X"*x) + "I" + "X"
            return roman_number
        elif i == 4:
            roman_number = ("M"*m) + ("D"*d) + ("C"*c) + ("L"*l) + ("X"*x) + "I" + "V"
            return roman_number
        
        else:
            roman_number = ("M"*m) + ("D"*d) + ("C"*c) + ("L"*l) + ("X"*x) + ("V"*v) + ("I"*i)
            return roman_number
        
if __name__ == "__main__":
    test_cases = [1, 4, 9, 14, 44, 99, 400, 944, 1453, 1999, 2023, 3999]

    for num in test_cases:
        print(f"{num} => {roman_conversion(num)}")