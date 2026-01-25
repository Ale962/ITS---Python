from esercizio_gestione_ospedale import *
import requests


# COSTANTE BASE_URL
BASE_URL = 'http://127.0.0.1:5000'

#COSTANTE HEADERS
HEADERS = {
    'Content-type': 'application/json',
    'Accept': 'application/json'
}

# Variabile new_booking da usare per test POST
new_booking = {
    'type': 'visit',
    'booking_id': 'BK-TEST-001',
    'patient_name': 'Giuseppe Verdi',
    'doctor': 'Dr. House',
    'department': 'Diagnostica',
    'date': '2026-03-01',
    'time': '09:00',
    'status': 'scheduled',
    'visit_reason': 'Emicrania acuta',
    'first_time': True
}

# Variabile booking_update da usare per test PUT
# Nota: Cambio tipo in 'exam' per testare se il sistema gestisce il cambio classe
booking_update = {
    'type': 'exam', 
    'booking_id': 'BK-TEST-001',
    'patient_name': 'Giuseppe Verdi',
    'doctor': 'Dr. Strange',
    'department': 'Radiologia',
    'date': '2026-03-05',
    'time': '10:30',
    'status': 'completed',
    'exam_type': 'TAC',
    'requires_fasting': True
}

# COSTANTE PER UTILIZZARE L'ID NEI TEST (URL)
BOOKING_ID = new_booking['booking_id']

if __name__ == '__main__':
    
    # 1-- TEST GET /  (Prendo la Home)
    r = requests.get(f'{BASE_URL}/', headers=HEADERS)
    if r.status_code == 200:
        print(f'GET /,\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\n{r.json()},\nTEST NON SUPERATO')

    # 2-- TEST GET /bookings (Ottengo la lista dei booking)
    r = requests.get(f'{BASE_URL}/bookings', headers=HEADERS)
    bookings = r.json()
    if len(bookings) > 0 and r.status_code == 200:
        print(f'GET /bookings,\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\n{r.json()},\nTEST NON SUPERATO')

    # 3-- TEST POST /bookings (Creo un nuovo booking)
    r = requests.post(f'{BASE_URL}/bookings', json=new_booking, headers=HEADERS)
    if r.status_code == 201:
        print(f'POST /bookings,\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\n{r.json()},\nTEST NON SUPERATO')

    # 4-- TEST GET /bookings/{BOOKING_ID} (Cerco di prendere il veicolo appena creato)
    r = requests.get(f'{BASE_URL}/bookings/{BOOKING_ID}', headers=HEADERS)
    if r.status_code == 200:
        print(f'GET /bookings/{BOOKING_ID},\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\n{r.json()},\nTEST NON SUPERATO')

    # 5-- TEST PATCH /bookings/{BOKING_ID}/status (Aggiornamento dello stato)
    status = {'status': 'checked_in'}
    r = requests.patch(f'{BASE_URL}/bookings/{BOOKING_ID}/status', json=status, headers=HEADERS)
    if r.status_code == 200:
        print(f'PATCH /bookings/{BOOKING_ID}/stauts,\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\n{r.json()},\nTEST NON SUPERATO')

    # 6-- TEST PUT /bookings/{BOOKING_ID} (Aggiornamento totale)
    r = requests.put(f'{BASE_URL}/bookings/{BOOKING_ID}', json=booking_update, headers=HEADERS)
    if r.status_code == 200:
        print(f'PUT /bookings/{BOOKING_ID},\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\n{r.json()},\nTEST NON SUPERATO')

    # 7-- TEST DELETE /bookings/{BOOKING_ID} (Cancellazione booking di testing)
    r = requests.delete(f'{BASE_URL}/bookings/{BOOKING_ID}', headers=HEADERS)
    if r.status_code == 200:
        print(f'DELETE /bookings/{BOOKING_ID},\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\n{r.json()},\nTEST NON SUPERATO')

    # 8-- CONFERMA CANCELLAZIONE 
    r = requests.get(f'{BASE_URL}/bookings/{BOOKING_ID}', headers=HEADERS)
    if r.status_code == 404:
        print(f'GET /bookings/{BOOKING_ID},\n{r.status_code},\n{r.json()},\nTEST SUPERATO')
    else:
        print(f'{r.status_code},\n{r.json()},\nTEST NON SUPERATO, CANCELLAZIONE NON AVVENUTA COME SI DEVE')