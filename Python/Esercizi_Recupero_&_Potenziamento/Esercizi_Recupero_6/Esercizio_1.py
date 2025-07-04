def recursivePalindrome(s: str) -> bool:
    s = s.lower().replace(' ', '')

    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return recursivePalindrome(s[1:-1])
    
if __name__ == '__main__':
    print(recursivePalindrome('radar'))
    print(recursivePalindrome('Anna'))
    print(recursivePalindrome('I topi non avevano nipoti'))
    print(recursivePalindrome('casa'))
    print(recursivePalindrome('Marta'))
    print(recursivePalindrome('Roma e Amore'))