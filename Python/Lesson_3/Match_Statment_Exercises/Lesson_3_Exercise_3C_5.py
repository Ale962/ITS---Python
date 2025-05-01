# Lesson 3 Exercise 3C-5

'''

Esercizio 3C-5. Scrivere un programma in Python che memorizzi il nome, il ruolo e l'età di un utente in un dizionario. Il nome, il ruolo e l'età devono essere inseriti in input dall'utente stesso. Il programma deve determinare il livello di accesso ai servizi in base al ruolo e all'età dell'utente secondo questo schema:

- Admin → "Accesso completo a tutte le funzionalità."
- Moderatore → "Può gestire i contenuti ma non modificare le impostazioni."
- Utente adulto (età ≥ 18) → "Accesso standard a tutti i servizi."
- Utente minorenne (età < 18) → "Accesso limitato! Alcune funzionalità sono bloccate."
- Ospite → "Accesso ristretto! Solo visualizzazione dei contenuti."
- Ruolo non riconosciuto → "Attenzione! Ruolo non riconsciuto! Accesso Negato!"

Expected Output:

Digitare nome dell'utente: Mario Rossi
Digitare ruolo dell'utente: admin
Digitare l'età dell'utente: 30
Output: Accesso completo a tutte le funzionalità.

- - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Giulia Bianchi
Digitare ruolo dell'utente: utente
Digitare l'età dell'utente: 16
Output: Accesso limitato! Alcune funzionalità sono limitate!

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Sara Neri
Digitare ruolo dell'utente: vip
Digitare l'età dell'utente: 22
Output: Attenzione! Ruolo non riconosciuto! Accesso Negato!

 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digitare nome dell'utente: Luca Verdi
Digitare ruolo dell'utente: moderatore
Digitare l'età dell'utente: 25
Output: Salve Luca Verdi! Può gestire i contenuti ma non modificare le impostazioni.

'''

users: dict = {}

while True:
    user: dict = {}
    name: str = input("")
    age: int = int(input(""))
    role: str = input("")

    user["name"] = name
    user["age"] = age
    user["role"] = role
    users[name] = user

    match (user["role"], user["age"]):
        
        case ("admin", _):
            print(f"Complete access to all functions.")

        case ("moderator", _):
            print(f"Hello {user["name"]}! You can manage contents but you can't modify settings.")

        case ("user", age) if age >= 18:
            print("Standard access to all services.")
        
        case ("user", age) if age < 18:
            print("Restricted access! Some services are limited.")

        case _:
            print("Warning! Role not recognised! Access denied!")

    add_user: str = input("Want to add a new user? (Y or N) ")
    if add_user.upper() == "N":
        break

