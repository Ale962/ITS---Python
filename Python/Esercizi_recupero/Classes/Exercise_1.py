# Exercise Classes

'''
Classi
Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di
creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà
essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.
1. Classe ContactManager:
Gestisce tutte le operazioni legate ai contatti.

'''

class ContactManager:
    def __init__(self):
        self.contacts: dict[str, list[str]] = {}

    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        new_number: dict[str, list[str]] = {}
        new_number[name] = phone_numbers
        if name in self.contacts.keys():
            raise  ValueError('Error: contact already exist')
        else:
            self.contacts[name] = phone_numbers

        return new_number
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

        if contact_name in self.contacts.keys():
            if phone_number in self.contacts[contact_name]:
                updated_contact: dict[str, list[str]] = {}
                updated_contact[contact_name] = [phone_number]
                self.contacts[contact_name].append(phone_number)
                return updated_contact
            else:
                raise RuntimeError('Error: number already present')
        else:
            raise ValueError('Error: contact does not exist')

    def remove_phone_number(self, contact_name: str, phone_number: str):

        if contact_name in self.contacts.keys():
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
                updated_contact: dict[str, list[str]] = {}
                updated_contact[contact_name] = self.contacts[contact_name]
                return updated_contact
            else:
                raise RuntimeError('Error: number not present')
        else:
            raise ValueError('Error: contact does not exist')
        
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]]:

        if contact_name in self.contacts.keys():
            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_phone_number)
                updated_contact: dict[str, list[str]] = {}
                updated_contact[contact_name] = self.contacts[contact_name]
                return updated_contact
            else:
                raise RuntimeError('Error: number not present')
        else:
            raise ValueError('Error: contact does not exist')
        
    def list_contacts(self) -> list[str]:

        list_contacts : list[str] = []

        for name in self.contacts.keys():
            list_contacts.append(name)

        return list_contacts
    
    def list_phone_numbers(self, contact_name: str) -> list[str]:
        
        list_numbers: list[str] = []

        if contact_name in self.contacts.keys():
            for number in self.contacts[contact_name]:
                list_numbers.append(number)
        else:
            raise ValueError('Error: contact does not exist')
        
        return list_numbers
        
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:

        list_contacts_number: list[str] = []

        for n, l in self.contacts.items():
            if phone_number in l:
                list_contacts_number.append(n)
            else:
                continue

        if len(list_contacts_number) > 0:
            return list_contacts_number
        else:
            raise RuntimeError('Empty list')