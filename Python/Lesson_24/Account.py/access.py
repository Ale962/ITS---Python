def check_access(username: str, password: str, is_active: bool) -> str:
    # cancella ... è definisci il tipo di dato per password, successivamente cancella pass e scrivi il tuo codice
    if username == 'admin':
        if password == '12345':
            if is_active == True:
                return 'Accesso consentito'
            else:
                return 'Accesso negato'
        else:
            return 'Accesso negato'    
    else:
        return 'Accesso negato'
    
print(check_access("admin", "12345", True))
print(check_access("admin", "12345", False))
print(check_access("user", "12345", True))
print(check_access("admin", "54321", True))
print(check_access("admin", "54321", False))