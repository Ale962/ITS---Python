# TEST AUTOMATICI PARKING LOT CON REQUEST
import json
import requests
from esercizio_4 import *

# COSTANTE BASE URL
BASE_URL = 'http://127.0.0.1:5000'

# COSTANTE HEADER PER TIPO JSON
HEADERS = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

# Variabile new_vheicle da usare dopo per test POST
new_vehicle = {
    'plate_id': 'AA123BB',
    'model': 'FIAT Panda 4x4',
    'driver_name': 'Alex Il Leone',
    'registration_year': 2024,
    'status': 'available',
    'doors': 5,
    'is_cabrio': False,
    'type': 'car'
}

vehicle_update = {
    'plate_id': 'AA123BB',
    'model': 'FIAT Panda 4x4',
    'driver_name': 'Martinnnnnnn',
    'registration_year': 2012,
    'status': 'retired',
    'doors': 5,
    'is_cabrio': False,
    'type': 'car'
}

#COSTANTE PER UTILIZZARE LA TARGA DEL VEICOLO NEI TEST POST/PUT/PATCH/DELETE
TARGA = new_vehicle['plate_id']

if __name__ == '__main__':

    # 1-- TEST GET HOME
    r = requests.get(f"{BASE_URL}/", headers=HEADERS)
    print('GET /', r.status_code, r.json()) # --> Expected 200

    # 2-- TEST GET /vehicles CON CERTEZZA DI LISTA DISPONIBILE
    r = requests.get(f"{BASE_URL}/vehicles", headers=HEADERS)
    lists_vehicles = r.json()
    if r.status_code == 200:
        if len(lists_vehicles) > 0:
            print('GET /vehicles')
            print(r.status_code)
            print(r.json()) # --> json.dumps(r) per avere una stringa invece del dizionario stampato a risposta
            print('TEST SUPERATO')

        else:
            print('TEST FALLITO, LISTA VEICOLI VUOTA')

    # 3-- TEST POST /vehicles/TARGA CREAZIONE NUOVO VEICOLO
    r = requests.post(f"{BASE_URL}/vehicles", json=new_vehicle, headers=HEADERS) # --> alternativa a json= è json.dumps(new_vehicle), passandogli in stringa il dizionario e rendedolo leggibile per HTTP (che legge solo testi)
    print(f'POST /vehicles/{TARGA}', r.status_code, r.json()) # --> Stampa percorso, conferma della CREAZIONE (code 201), stampa nuovo veicolo

    # 4-- TEST GET /vehicles/TARGA VERIFICA CREAZIONE EFFETTIVA NUOVO VEICOLO
    r = requests.get(f"{BASE_URL}/vehicles/{TARGA}", headers=HEADERS)
    print(f'GET /vehicles/{TARGA}', r.status_code, r.json()) # --> Expected 200

    # 5-- TEST PATCH /vehicles/TARGA/status PROVA MODIFICA PARZIALE
    status_change = {'status': 'cleaning'}
    r = requests.patch(f"{BASE_URL}/vehicles/{TARGA}/status",json=status_change, headers=HEADERS)
    print(f'PATCH /vehicle/{TARGA}/status', r.status_code, r.json().get('status')) # --> Expected 200

    # 6-- TEST PUT /vehicle/TARGA SOSTITUZIONE COMPLETA VEICOLO
    r = requests.put(f"{BASE_URL}/vehicles/{TARGA}", json=vehicle_update, headers=HEADERS)
    print(f'PUT /vehicles/{TARGA}', r.status_code, r.json()) # --> Expected 200

    # 7-- TEST DELETE /vehicle/TARGA ELIMINAZIONE VEICOLO PER PROVA
    r = requests.delete(f"{BASE_URL}/vehicles/{TARGA}", headers=HEADERS)
    print(f'DELETE /vehicle/{TARGA}', r.status_code) # --> Expected 200

    # 8-- TEST GET /vehicle/TARGA CONTROLLO FINALE DI AVVENUTA CANCELLAZIONE CORRETTAMENTE
    r = requests.get(f"{BASE_URL}/vehicles/{TARGA}", headers=HEADERS)
    print(f'GET /vehicles/{TARGA}', r.status_code, r.json()) # --> Expected 404