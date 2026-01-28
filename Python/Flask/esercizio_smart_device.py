from __future__ import annotations
from abc import ABC, abstractmethod
from flask import Flask, jsonify, url_for, request
import json

class SmartDevice(ABC):
    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str):
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        pass

    @abstractmethod
    def energy_consumption(self) -> float | int:
        pass

    @abstractmethod
    def connection_quality(self) -> int:
        pass

    def info(self) -> dict[str, float | int | str]:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            "device_type": self.device_type()
        }

    def diagnostics_time(self, factor: float = 1.0) -> float:
        return (self.energy_consumption() * factor) + (self.connection_quality() * 10)


class SmartBulb(SmartDevice):
    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str, brightness_lumens: int, color_capability: bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float | int:
        return 12 

    def connection_quality(self) -> int:
        return 3

    def info(self) -> dict[str, float | int | str]:
        data = super().info()
        data["brightness_lumens"] = self.brightness_lumens
        data["color_capability"] = self.color_capability
        return data


class SecurityCamera(SmartDevice):
    def __init__(self, serial_number: str, brand: str, room: str, installation_year: int, status: str, resolution: str, night_vision: bool):
        super().__init__(serial_number, brand, room, installation_year, status)
        self.resolution = resolution
        self.night_vision = night_vision

    def device_type(self) -> str:
        return "camera"

    def energy_consumption(self) -> float | int:
        return 50

    def connection_quality(self) -> int:
        return 9

    def info(self) -> dict:
        data = super().info()
        data["resolution"] = self.resolution
        data["night_vision"] = self.night_vision
        return data


class IoTHub:
    def __init__(self):
        self.devices = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number in self.devices:
            return False
        self.devices[device.serial_number] = device
        return True

    def get(self, serial_number: str) -> SmartDevice | None:
        return self.devices.get(serial_number)

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        if serial_number in self.devices:
            self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        if serial_number in self.devices:
            self.devices[serial_number].status = new_status

    def delete(self, serial_number: str) -> bool:
        if serial_number in self.devices:
            del self.devices[serial_number]
            return True
        return False

    def list_all(self) -> list[dict]:
        return [device.info() for device in self.devices.values()]


# Setup e Popolamento
iot_hub = IoTHub()

bulb1 = SmartBulb(
    serial_number="SN-101",
    brand="Nest",
    room="Living Room",
    installation_year=2023,
    status="online",
    brightness_lumens=800,
    color_capability=True
)

camera1 = SecurityCamera(
    serial_number="SN-202",
    brand="Ring",
    room="Front Door",
    installation_year=2022,
    status="online",
    resolution="1080p",
    night_vision=True
)

iot_hub.add(bulb1)
iot_hub.add(camera1)

VALID_S = ['online', 'offline', 'updating', 'error']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    links = {
        'devices': url_for('list_devices'),
        'SN-101': url_for('description',SN='SN-101'),
        'diagnostic SN-101': url_for('time', SN='SN-101', factor=1.0)
    }
    home = {
        'welcome': 'Smart Home Hub API',
        'links': links
    }
    return jsonify(home), 200

@app.route('/devices', methods=['GET'])
def list_devices():
    if len(iot_hub.list_all()) == 0:
        return jsonify({'errore': 'List not existent'}), 404
    return jsonify(iot_hub.list_all()), 200

@app.route('/devices/<string:SN>', methods=['GET'])
def description(SN: str):
    d = iot_hub.get(SN)
    if not d:
        return jsonify({'error':'Il Device non esiste'}), 404
    return jsonify(d.info()), 200

@app.route('/devices/<string:SN>/diagnostic/<float:factor>', methods=['GET'])
def time(SN: str, factor: float):
    d = iot_hub.get(SN)
    if not d:
        return jsonify({'error':'Il Device non esiste'}), 404
    time_d = d.diagnostics_time(factor)
    return jsonify({'wait_time': time_d}), 200

@app.route('/devices', methods=['POST'])
def create_device():
    data: dict = request.get_json()
    new_device = None
    SN = data.get('serial_number')
    b = data.get('brand')
    r = data.get('room')
    inY = data.get('installation_year')
    s = data.get('status')
    bl = data.get('brightness_lumens')
    cc = data.get('color_capability')
    res = data.get('resolution')
    nv = data.get('night_vision')
    t = data.get('type')

    if not data or not SN or not b or not r or not inY or not s or not t:
        return jsonify({'error':'The request is missing or is incomplete'}), 400
    
    if s not in VALID_S:
        return jsonify({'errore': 'The status in the request is not valid'}), 400
    
    if t == 'bulb':
        if not bl or cc is None:
            return jsonify({'error':'The request is incomplete'}), 400
        new_device = SmartBulb(
            serial_number = SN,
            brand = b,
            room = r,
            installation_year = inY,
            status = s, 
            brightness_lumens = bl, 
            color_capability = cc 
        )
    elif t == 'camera':
        if not res or nv is None:
            return jsonify({'error':'The request is incomplete'}), 400
        new_device = SecurityCamera(
            serial_number = SN,
            brand = b,
            room = r,
            installation_year = inY,
            status = s, 
            resolution = res, 
            night_vision = nv 
        )
    else:
        return jsonify({'error':'The type is incorrect'}), 400 
    
    confirmation = iot_hub.add(new_device)

    if not confirmation:
        return jsonify({'error':'The device already exist'}), 400
    else:
        return jsonify(new_device.info()), 201

@app.route('/devices/<string:SN>', methods=['PUT'])
def update_device(SN: str):
    data: dict = request.get_json()
    new_device = None
    b = data.get('brand')
    r = data.get('room')
    inY = data.get('installation_year')
    s = data.get('status')
    bl = data.get('brightness_lumens')
    cc = data.get('color_capability')
    res = data.get('resolution')
    nv = data.get('night_vision')
    t = data.get('type')
    device = iot_hub.get(SN)

    if not data or not b or not r or not inY or not s or not t:
        return jsonify({'error':'The request is missing or is incomplete'}), 400
    
    if s not in VALID_S:
        return jsonify({'errore': 'The status in the request is not valid'}), 400

    if not device:
        return jsonify({'error':'The device does not exist'}), 404
    
    if t == 'bulb':
        if not bl or cc is None:
            return jsonify({'error':'The request is incomplete'}), 400
        new_device = SmartBulb(
            serial_number = SN,
            brand = b,
            room = r,
            installation_year = inY,
            status = s, 
            brightness_lumens = bl, 
            color_capability = cc 
        )
    elif t == 'camera':
        if not res or nv is None:
            return jsonify({'error':'The request is incomplete'}), 400
        new_device = SecurityCamera(
            serial_number = SN,
            brand = b,
            room = r,
            installation_year = inY,
            status = s, 
            resolution = res, 
            night_vision = nv 
        )
    else:
        return jsonify({'error':'The type is incorrect'}), 400
    
    iot_hub.update(SN, new_device)
    return jsonify(new_device.info()), 200

@app.route('/devices/<string:SN>/status', methods=['PATCH'])
def update_status(SN: str):
    data: dict = request.get_json()
    s = data.get('status')
    device = iot_hub.get(SN)

    if not s or s not in VALID_S:
        return jsonify({'errore': 'The status in the request is not valid or not present'}), 400
    
    if not device:
        return jsonify({'error':'The device does not exist'}), 404
    
    iot_hub.patch_status(SN,s)

    return jsonify({'meesage': 'Status aggiornato correttamente'}), 200

@app.route('/devices/<string:SN>', methods=['DELETE'])
def remove_device(SN: str):
    confirmation = iot_hub.delete(SN)

    if not confirmation:
        return jsonify({'error':'The device does not exist'}), 404
    else:
        return jsonify({'message': 'Device removed with success'}), 200