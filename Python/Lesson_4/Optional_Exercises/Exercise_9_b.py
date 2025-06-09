# Exercise 9

'''
9. Caesar Cipher Encryption/Decryption

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
     Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value.

'''
import string

letters = list(string.ascii_letters)

def Ceasar_Cypher_encrypt(text: str, key: int) -> str:
    encrypted_text = ""
    for l in text:
        if l not in letters:
                encrypted_text += l
                continue
        index = letters.index(l)
        l = letters[(index + key) % len(letters)]
        encrypted_text += l
    return encrypted_text

def Ceasar_Cypher_decrypt(text: str, key: int) -> str:
    decrypted_text = ''
    for l in text:
        if l not in letters:
            decrypted_text += l
            continue
        
        index = letters.index(l)
        l = letters[(index - key) % len(letters)]
        decrypted_text += l
    return decrypted_text

def Ceasar_Cypher() -> None:
    while True:
        question = input(
            "Do you want to decrypt o encrypt a text?\n" \
            "Insert E for encrypting\n" \
            "Insert D for decrypting\n" \
            "Insert Q to quit the program\n" \
            "Insert here: ").upper()
        print("--------------"*3)
        match question:
            case "E":
                print("Encrypt option selected")
                print("--------------"*3)
                print()
                text = input("Insert the text here:\n" \
                "")
                print()
                key = int(input("Insert the key to which encrypt the message:\n" \
                ""))
                if key >= 52:
                    raise ValueError("The key can not be more then 52")
                print()
                print("--------------"*3)
                encrypted_text = Ceasar_Cypher_encrypt(text, key)
                print("Message encryption succesuful")
                print(f"Encrypted message: {encrypted_text}")
                print(f"Encypting key: {key}")
                print("--------------"*3)
            case "D":
                print("Decrypt option selected")
                print("--------------"*3)
                print()
                text = input("Insert the text here:\n" \
                "")
                print()
                key = int(input("Insert the key to which decrypt the message:\n" \
                ""))
                if key >= 52:
                    raise ValueError("The key can not be more then 52")
                print()
                print("--------------"*3)
                decrypted_text = Ceasar_Cypher_decrypt(text, key)
                print("Message decryption succesuful")
                print(f"Decrypted message: {decrypted_text}")
                print(f"Decypting key: {key}")
                print("--------------"*3)
            case "Q":
                print()
                print("Thank you for trying the Ceasar Cypher Program!")
                print("Have a good day!")
                print()
                print("--------------"*3)
                break
            case _:
                print()
                print("Not valid option selected")
                print("Please restart the process and select a valid option")
                print()
                print("--------------"*3)

if __name__ == '__main__':
    print("--------------"*3)
    print()
    print("Ceaser Cypher Programm")
    print()
    print("--------------"*3)
    Ceasar_Cypher()