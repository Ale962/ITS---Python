# Exercise 10

'''
10. Anagram Checker:

    Create a function that checks whether two given strings are anagrams of each other.
    Convert both strings to lowercase and remove any non-alphabetic characters.
    Sort the characters of each string and compare the sorted strings for equality.
    Indicate whether the strings are anagrams or not.

'''
import string
letters: list = list(string.ascii_lowercase)

def anagram(text1: str, text2: str) -> None:
    letters_text1 = []
    letters_text2 = []
    for l in text1.lower():
        if l not in letters:
            continue
        letters_text1.append(l)
    for l in text2.lower():
        if l not in letters:
            continue
        letters_text2.append(l)

    text1_sort = sorted(letters_text1)
    text2_sort = sorted(letters_text2)

    if text1_sort == text2_sort:
        print()
        print(f'The two text are angrams of each other, {text2} is an angram of {text1}!')
        print()
    else:
        print()
        print('The text are not are not anagram')
        print()
    
def anagram_checker():
    print("--------------"*3)
    print()
    print('ANAGRAM CHECKER PROGRAM')
    print()
    print("--------------"*3)
    print()
    text1 = input('Write the first text to check:\n' \
    '')
    text2 = input('Write the second text to check:\n' \
    '')
    print()
    print("--------------"*3)
    anagram(text1, text2)
    print("--------------"*3)

if __name__ == '__main__':
    anagram_checker()