from esercizio_smart_device import *
import requests

# Variabile new_bulb per test POST (Creazione)
new_bulb = {
    "type": "bulb",
    "serial_number": "SN-TEST-999",
    "brand": "LIFX",
    "room": "Kitchen",
    "installation_year": 2024,
    "status": "online",
    "brightness_lumens": 1200,
    "color_capability": True
}

# Variabile update_camera per test PUT (Sostituzione completa - cambio tipo)
update_camera = {
    "type": "camera",
    "serial_number": "SN-TEST-999", # Stesso ID per sovrascrivere
    "brand": "Sony",
    "room": "Garage",
    "installation_year": 2025,
    "status": "offline",
    "resolution": "4K",
    "night_vision": True
}

# Costante per l'ID
SERIAL_NUM = new_bulb['serial_number']

NEW_STATUS = {'status': 'updating'}

BASE_URL = 'http://127.0.0.1:5000'

HEADERS = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

if __name__ == '__main__':

    # 1-- GET /
    r = requests.get(f'{BASE_URL}', headers=HEADERS)
    if r.status_code == 200:
        print(f'GET \'/\',\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\nTEST NON SUPERATO')

    # 2-- GET /devices (ottiene tutti i devices)
    r = requests.get(f'{BASE_URL}/devices', headers=HEADERS)
    if r.status_code == 200:
        print(f'GET \'/devices\',\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\nTEST NON SUPERATO')

    # 3-- POST /devices (crea nuovo oggetto)
    r = requests.post(f'{BASE_URL}/devices', json=new_bulb, headers=HEADERS)
    if r.status_code == 201:
        print(f'POST \'/devices\',\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\nTEST NON SUPERATO')

    # 4-- GET /devices/{SERIAL_NUM} (conferma creazione nuovo device)
    r = requests.get(f'{BASE_URL}/devices/{SERIAL_NUM}', headers=HEADERS)
    if r.status_code == 200 and (len(r.json()) > 0):
        print(f'GET \'/devices/{SERIAL_NUM}\',\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\nTEST NON SUPERATO')

    # 5-- PATCH /devices/{SERIAL_NUM}/status
    r = requests.patch(f'{BASE_URL}/devices/{SERIAL_NUM}/status', json=NEW_STATUS, headers=HEADERS)
    if r.status_code == 200:
        print(f'PATCH \'/devices/{SERIAL_NUM}/status\',\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\nTEST NON SUPERATO')

    # 6-- PUT /devices/{SERIAL_NUM}
    r = requests.put(f'{BASE_URL}/devices/{SERIAL_NUM}', json=update_camera, headers=HEADERS)
    if r.status_code == 200:
        print(f'PUT \'/devices/{SERIAL_NUM}\',\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\nTEST NON SUPERATO')

    # 7-- DELETE /devices/{SERIAL_NUM}
    r = requests.delete(f'{BASE_URL}/devices/{SERIAL_NUM}', headers=HEADERS)
    if r.status_code == 200:
        print(f'DELETE \'/devices/{SERIAL_NUM}\',\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\nTEST NON SUPERATO')

    # 8-- GET /devices/{SERIAL_NUM}
    r = requests.get(f'{BASE_URL}/devices/{SERIAL_NUM}', headers=HEADERS)
    if r.status_code == 404:
        print(f'GET \'/devices/{SERIAL_NUM}\',\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\nTEST NON SUPERATO')