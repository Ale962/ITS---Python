from abc import ABC, abstractmethod
from flask import Flask, jsonify, url_for

# ==========================
# 1. Classi di Dominio (OOP)
# ==========================

class Ride(ABC):
    """
    Classe astratta che rappresenta un'attrazione generica.
    """
    def _init_(self, ride_id: str, name: str, min_height_cm: int):
        self.id = ride_id
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self) -> str:
        """Restituisce la categoria dell'attrazione."""
        pass

    @abstractmethod
    def base_wait(self) -> int:
        """Restituisce il tempo di attesa base in minuti."""
        pass

    def info(self) -> dict:
        """
        Restituisce un dizionario con le informazioni principali.
        Nota: Chiama il metodo astratto category() per ottenere il tipo.
        """
        return {
            "id": self.id,
            "name": self.name,
            "min_height_cm": self.min_height_cm,
            "category": self.category()
        }

    def wait_time(self, crowd_factor: float = 1.0) -> int:
        """
        Calcola il tempo di attesa stimato.
        Arrotonda il risultato all'intero più vicino.
        """
        estimate = self.base_wait() * crowd_factor
        return int(round(estimate))


class RollerCoaster(Ride):
    """
    Sottoclasse per le montagne russe.
    """
    def _init_(self, ride_id: str, name: str, min_height_cm: int, inversions: int):
        super()._init_(ride_id, name, min_height_cm)
        self.inversions = inversions

    def category(self) -> str:
        return "roller_coaster"

    def base_wait(self) -> int:
        return 40

    def info(self) -> dict:
        # Ottengo il dizionario base dalla superclasse e aggiungo il campo specifico
        data = super().info()
        data["inversions"] = self.inversions
        return data


class Carousel(Ride):
    """
    Sottoclasse per le giostre con animali.
    """
    def _init_(self, ride_id: str, name: str, min_height_cm: int, animals: list):
        super()._init_(ride_id, name, min_height_cm)
        self.animals = animals

    def category(self) -> str:
        return "family"

    def base_wait(self) -> int:
        return 10

    def info(self) -> dict:
        # Ottengo il dizionario base dalla superclasse e aggiungo il campo specifico
        data = super().info()
        data["animals"] = self.animals
        return data


class Park:
    """
    Classe contenitore (Manager) per gestire tutte le attrazioni.
    """
    def _init_(self):
        self.rides = {}  # Dizionario: id -> oggetto Ride

    def add(self, ride: Ride):
        """Aggiunge un'attrazione al parco."""
        self.rides[ride.id] = ride

    def get(self, ride_id: str):
        """Restituisce l'attrazione cercata o None."""
        return self.rides.get(ride_id)

    def list_all(self):
        """Restituisce una lista di tutte le attrazioni (oggetti)."""
        return list(self.rides.values())


# ==========================
# 2. Setup e Popolamento
# ==========================

app = Flask(__name__)
park = Park()

# Creazione delle attrazioni richieste
rc1 = RollerCoaster(
    ride_id="rc1", 
    name="Vortex", 
    min_height_cm=140, 
    inversions=5
)

c1 = Carousel(
    ride_id="c1", 
    name="Magic Horses", 
    min_height_cm=0, 
    animals=["horse", "unicorn", "lion"]
)

# Aggiunta al parco
park.add(rc1)
park.add(c1)


# ==========================
# 3. Route API (Flask)
# ==========================



# ---------------------------------------------------------
# SPAZIO RISERVATO AL TUO CODICE PER L'ESAME
# Qui dovrai implementare le seguenti route:
#
# 1. GET / 
#    - Return: JSON con messaggio di benvenuto e link generati con url_for
#
# 2. GET /rides
#    - Return: JSON lista di tutte le attrazioni
#
# 3. GET /rides/<ride_id>
#    - Return: JSON dettaglio singola attrazione (gestire errore se non esiste?)
#
# 4. GET /rides/<ride_id>/wait/<crowd>
#    - Return: JSON con tempo di attesa calcolato (usare metodo wait_time)
# ---------------------------------------------------------


# 1.
@app.route("/", methods= ['GET'])
def welcome():
    Dati: dict[str,str] = {
        "benvenuto": "Benvenuti",
        "attrazioni": url_for('get_rides')
        }
    return jsonify(Dati),200

# 2.
@app.route("/rides", methods= ['GET'])
def get_rides():
    ride_list: list[dict] = [r.info() for r in park.list_all()]
    ride_list_link_home = {'ritorno alla home': url_for('welcome')}
    ride_list.append(ride_list_link_home)
    return jsonify(ride_list), 200

# 3.
@app.route('/rides/<string:ride_id>', methods= ['GET'])
def get_ride(ride_id: str):
    ride = park.get(ride_id)
    if ride == None:
        return jsonify({'error': 'Attrazione non trovata'}),404
    data = ride.info()
    data['link_calcolo_attesa'] = url_for('get_wait',ride_id=ride_id,crowd = 1)
    return jsonify(data),200

# 4.
@app.route('/rides/<string:ride_id>/wait/<int:crowd>', methods= ['GET'])
def get_wait(ride_id: str, crowd: int):
    ride = park.get(ride_id)
    if ride == None:
        return jsonify({'error': 'Attrazione non trovata'}),404
    wait_time = ride.wait_time(crowd)
    attesa:dict = {
        'ride': ride.name,
        'crowd': crowd,
        'attesa': wait_time
        }
    return jsonify(attesa)


if __name__ == '__main__':
    app.run(debug=True)