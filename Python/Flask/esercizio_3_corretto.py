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

# 1. GET / - Messaggio di benvenuto e link
@app.route("/", methods=['GET'])
def welcome():
    # Costruiamo un dizionario, non HTML
    response_data = {
        "message": "Benvenuti al Parco",
        "links": {
            "all_rides": url_for('get_rides', _external=True)
        }
    }
    return jsonify(response_data), 200


# 2. GET /rides - Lista di tutte le attrazioni
@app.route("/rides", methods=['GET'])
def get_rides():
    # Recuperiamo tutte le attrazioni e prendiamo le loro info
    # park.list_all() restituisce oggetti, noi dobbiamo trasformarli in dizionari
    rides_list = [r.info() for r in park.list_all()]
    
    return jsonify(rides_list), 200


# 3. GET /rides/<ride_id> - Dettaglio singola attrazione
# NOTA: Ho tolto "int:" perché i tuoi ID sono "rc1", "c1" (stringhe)
@app.route('/rides/<ride_id>', methods=['GET'])
def get_ride(ride_id):
    ride = park.get(ride_id)
    
    if ride is None:
        return jsonify({"error": "Attrazione non trovata"}), 404
        
    # Costruiamo la risposta JSON
    data = ride.info()
    
    # Aggiungiamo un link utile per calcolare l'attesa (opzionale ma carino)
    # Esempio crowd default 1.0
    data["link_wait_time"] = url_for('get_wait', ride_id=ride_id, crowd=1.0, _external=True)
    
    return jsonify(data), 200


# 4. GET /rides/<ride_id>/wait/<crowd> - Tempo di attesa
# NOTA: crowd deve essere un parametro dinamico, es: <float:crowd>
@app.route('/rides/<ride_id>/wait/<float:crowd>', methods=['GET'])
def get_wait(ride_id, crowd):
    ride = park.get(ride_id)
    
    if ride is None:
        return jsonify({"error": "Attrazione non trovata"}), 404
    
    # Calcolo il tempo
    wait_minutes = ride.wait_time(crowd)
    
    return jsonify({
        "ride": ride.name,
        "crowd_factor": crowd,
        "estimated_wait_minutes": wait_minutes
    }), 200

# IMPORTANTE: Per avviare il server se lanci il file direttamente
if __name__ == '__main__':
    app.run(debug=True)