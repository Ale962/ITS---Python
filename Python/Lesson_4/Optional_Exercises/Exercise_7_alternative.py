# Optional Exercise 7
# Alternative more quicker version for best performance

'''
7. Roman Numeral Conversion:

    Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman numeral.

'''

def roman_converter(n: int) -> str:
    if n in range(1, 4000):
        pass
    else:
        raise ValueError("The number must be in the range between 1 and 3999")
    roman_number = ""
    roman_letters: list[tuple[int, str]] = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I")
    ]
    for value, letter in roman_letters:
        while n >= value:
            roman_number += letter
            n -= value

    return roman_number

if __name__ == "__main__":
    test_cases = [1, 4, 9, 14, 44, 99, 400, 944, 1453, 1999, 2023, 3999]

    for num in test_cases:
        print(f"{num} => {roman_converter(num)}")