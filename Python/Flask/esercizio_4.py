from __future__ import annotations
from abc import ABC, abstractmethod
from flask import Flask, jsonify, url_for, request
from enum import *

class Status(str,Enum):
    available = 'available'
    rented = 'rented'
    maintenance = 'maintenance'
    cleaning = 'cleaning'
    retired = 'retired'

class Vehicle(ABC):
    def __init__(self, plate_id: str, model: str, driver_name: str, registration_year: int, status: Status):
        self.plate_id = plate_id
        self.model = model
        self.driver_name = driver_name
        self.registration_year = registration_year
        self.status = status

    @abstractmethod
    def vehicle_type(self) -> str:
        pass

    @abstractmethod
    def base_cleaning_time(self) -> int:
        pass

    @abstractmethod
    def wear_level(self) -> int:
        pass

    def info(self):
        info: dict[str, str|Status|int] = {
            'id': self.plate_id,
            'model': self.model,
            'driver_name': self.driver_name,
            'vehicle_type': self.vehicle_type(),
            'status': self.status
        }

        return info
    
    def estimated_prep_time(self, factor: float = 1.0):
        return int((self.base_cleaning_time()*factor)+(self.wear_level()*15))
    
class Car(Vehicle):
    def __init__(self, plate_id, model, driver_name, registration_year, status, doors: int, is_cabrio: bool = False):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors = doors
        self.is_cabrio = is_cabrio

    def vehicle_type(self) -> str:
        return 'car'
    
    def base_cleaning_time(self) -> int:
        return 30
    
    def wear_level(self):
        return 2
    
    def info(self):
        data = super().info()
        data['doors'] = self.doors
        data['is_cabrio'] = self.is_cabrio
        return data
    
class Van(Vehicle):
    def __init__(self, plate_id, model, driver_name, registration_year, status, max_load_kg: int, require_special_license: bool = False):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = require_special_license

    def vehicle_type(self):
        return 'van'
    
    def base_cleaning_time(self):
        return 60
    
    def wear_level(self):
        return 4
    
    def info(self):
        data = super().info()
        data['max_load_kg'] = self.max_load_kg
        data['require_special_license'] = self.require_special_license
        return data

class FleetManager():
    def __init__(self, vehicles: dict[str,Vehicle]=None):
        if not vehicles:
            self.vehicles: dict[str,Vehicle] = {}
        else:    
            self.vehicles: dict[str,Vehicle] = vehicles

    def add(self, vehicle: Vehicle) -> bool:
        if vehicle.plate_id in self.vehicles:
            return False
        self.vehicles[vehicle.plate_id] = vehicle
        return True
    
    def get(self, plate_id: str) -> Vehicle:
        if plate_id in self.vehicles:
            vehicle = self.vehicles.get(plate_id)
            return vehicle
        else:
            return None
        
    def update(self, plate_id: str, new_vehicle: Vehicle) -> None:
        if plate_id in self.vehicles:
            self.vehicles[plate_id] = new_vehicle
        else:
            print('Veicolo non presente')
        
    def patch_status(self, plate_id: str, new_status: Status) -> None:
        if plate_id in self.vehicles:
            self.vehicles[plate_id].status = new_status
        else:
            print('Veicolo non presente')
        
    def delete(self, plate_id: str) -> bool:
        if plate_id in self.vehicles:
            self.vehicles.pop(plate_id)
            return True
        else:
            return False
        
    def list_all(self) -> list[dict]:
        list_vehicle = [v.info() for v in self.vehicles.values()]
        return list_vehicle
    
app = Flask(__name__)

# ==========================
# POPOLAMENTO DATI (SETUP)
# ==========================

# 1. Inizializzo il Manager
fleet_manager = FleetManager()

# 2. Creo un'Auto Standard (Fiat Panda)
car_panda = Car(
    plate_id="AB123CD",
    model="Fiat Panda Hybrid",
    driver_name=None,         # Nessun guidatore
    registration_year=2022,
    status=Status.available,   
    doors=5,
    is_cabrio=False
)

# 3. Creo un Furgone (Ford Transit)
van_ford = Van(
    plate_id="VN987XY",
    model="Ford Transit Custom",
    driver_name="Mario Rossi",
    registration_year=2019,
    status=Status.rented,     # Attualmente noleggiato
    max_load_kg=1400,
    require_special_license=False
)

# 4. Creo un'Auto Sportiva (Mazda MX-5) - In manutenzione
car_mazda = Car(
    plate_id="SP500RR",
    model="Mazda MX-5",
    driver_name=None,
    registration_year=2023,
    status=Status.maintenance,
    doors=2,
    is_cabrio=True
)

# 5. Aggiungo tutto al Manager
fleet_manager.add(car_panda)
fleet_manager.add(van_ford)
fleet_manager.add(car_mazda)

@app.route('/', methods=['GET'])
def welcome():
    home = {
        'message': 'Welcome to Rent Service API',
        'lista_veicoli': url_for('list_vehicles'),
        'dettagli_veicolo': url_for('vehicle_info',plate_id='HA014AS'),
        'tempo_preparazione': url_for('get_time',plate_id='HA014AS', factor=2.0)
    }

    return jsonify(home), 200

@app.route('/vehicles', methods=['GET'])
def list_vehicles():
    list_v = fleet_manager.list_all()
    link_home = {'link_home': url_for('welcome')}
    list_v.append(link_home)
    return jsonify(list_v), 200

@app.route('/vehicles/<string:plate_id>', methods=['GET'])
def vehicle_info(plate_id: str):
    if plate_id in fleet_manager.vehicles:
        v = fleet_manager.vehicles[plate_id]
        v_info = v.info()
        return jsonify(v_info), 200
    
    else:
        error = {'error': 'Vehicle Not Found'}
        return jsonify(error), 404
    
@app.route('/vehicles/<string:plate_id>/prep-time/<float:factor>', methods=['GET'])
def get_time(plate_id: str, factor: float):
    if plate_id in fleet_manager.vehicles:
        v = fleet_manager.vehicles.get(plate_id)
        v_time = v.estimated_prep_time(factor)
        v_info = v.info()
        v_info['prep_time'] = v_time
        return jsonify(v_info),200
    else:
        error = {'error': 'Vehicle Not Found'}
        return jsonify(error), 404
    
@app.route('/vehicles', methods=['POST'])
def create_vehicle():

    data: dict = request.get_json()
    new_vehicle = None

    if data.get('status') not in Status.__members__:
        error = {'error': 'Status non riconosciuto'}
        return jsonify(error), 400
    
    new_status_enum = Status[data.get('status')]
    try:
        if data['type'] == 'car':
            new_vehicle = Car(
                plate_id=data.get('plate_id'),
                model=data.get('model'),
                driver_name=data.get('driver_name'),
                registration_year=data.get('registration_year'),
                doors=data.get('doors'),
                is_cabrio=data.get('is_cabrio'),
                status= new_status_enum
            )
        elif data['type'] == 'van':
            new_vehicle = Van(
                plate_id=data.get('plate_id'),
                model=data.get('model'),
                driver_name=data.get('driver_name'),
                registration_year=data.get('registration_year'),
                max_load_kg=data.get('max_load_kg'),
                require_special_license=data.get('require_special_license'),
                status=new_status_enum
            )
        else:
            error = {'error': 'Tipo non riconosciuto'}
            return jsonify(error), 400
        if fleet_manager.add(new_vehicle):
            return jsonify(new_vehicle.info()),201
        else:
            return jsonify({'error': 'Veicolo già esistente'}), 409
        
    except Exception as e:
        return jsonify({'error': f'No data or missing parameters: {str(e)}'}), 400

@app.route('/vehicles/<string:plate_id>', methods=['PUT'])
def sub_vehicle(plate_id: str):
    data: dict = request.get_json()
    if not fleet_manager.get(plate_id):
        error = {'error': 'Vehicle Not Found'}
        return jsonify(error), 404
        
    if data.get('status') not in Status.__members__:
        error = {'error': 'Status non riconosciuto'}
        return jsonify(error), 400
    
    new_status_enum = Status[data.get('status')]
    updated_vehicle = None

    if data['type'] == 'car':
            updated_vehicle = Car(
                plate_id=plate_id,
                model=data.get('model'),
                driver_name=data.get('driver_name'),
                registration_year=data.get('registration_year'),
                doors=data.get('doors'),
                is_cabrio=data.get('is_cabrio'),
                status= new_status_enum
            )
    elif data['type'] == 'van':
            updated_vehicle = Van(
                plate_id=plate_id,
                model=data.get('model'),
                driver_name=data.get('driver_name'),
                registration_year=data.get('registration_year'),
                max_load_kg=data.get('max_load_kg'),
                require_special_license=data.get('require_special_license'),
                status=new_status_enum
            )

    fleet_manager.update(plate_id, updated_vehicle)

    return jsonify(updated_vehicle.info())
    
    
    
@app.route('/vehicles/<string:plate_id>/status', methods=['PATCH'])
def update_status(plate_id: str):
    data: dict = request.get_json()

    if data.get('status') not in Status.__members__:
        error = {'error': 'Status non riconosciuto'}
        return jsonify(error), 400

    new_status_enum = Status[data.get('status')]

    if plate_id in fleet_manager.vehicles:
        fleet_manager.patch_status(plate_id, new_status_enum)
        v = fleet_manager.get(plate_id)
        return jsonify(v.info()), 200
    
    else:
        error = {'error': 'Vehicle Not Found'}
        return jsonify(error), 404
    
@app.route('/vehicles/<string:plate_id>', methods=['DELETE'])
def delete_vehicle(plate_id: str):
    if plate_id in fleet_manager.vehicles:
        fleet_manager.delete(plate_id)
        return jsonify({'result': 'deleted'}),200
    else:
        error = {'error': 'Vehicle Not Found'}
        return jsonify(error), 404