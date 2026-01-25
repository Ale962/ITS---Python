from __future__ import annotations
from abc import ABC, abstractmethod
from flask import Flask, jsonify, url_for, request
import json

class Booking(ABC):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str):
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.status = status

    @abstractmethod
    def booking_type(self) -> str:
        pass

    @abstractmethod
    def base_duration(self) -> int:
        pass

    @abstractmethod
    def priority_level(self) -> int:
        pass

    def info(self) -> dict[str, int | str | bool | float]:
        return {
            "booking_id": self.booking_id,
            "patient_name": self.patient_name,
            "doctor": self.doctor,
            "department": self.department,
            "date": self.date,
            "time": self.time,
            "status": self.status,
            "booking_type": self.booking_type()
        }

    def estimated_wait(self, factor: float = 1.0) -> int:
        return int(self.base_duration() * factor + self.priority_level() * 5)


class MedicalVisit(Booking):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str, visit_reason: str, first_time: bool):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.visit_reason = visit_reason
        self.first_time = first_time

    def booking_type(self) -> str:
        return "visit"

    def base_duration(self) -> int:
        return 30

    def priority_level(self) -> int:
        reason = (self.visit_reason or "").lower()
        keywords = ["urgente", "dolore", "acuto", "svenimento"]
        for k in keywords:
            if k in reason:
                return 7
        return 5

    def info(self) -> dict:
        data = super().info()
        data["visit_reason"] = self.visit_reason
        data["first_time"] = self.first_time
        return data


class DiagnosticExam(Booking):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str, exam_type: str, requires_fasting: bool):
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.exam_type = exam_type
        self.requires_fasting = requires_fasting

    def booking_type(self) -> str:
        return "exam"

    def base_duration(self) -> int:
        return 45

    def priority_level(self) -> int:
        et = (self.exam_type or "").strip().lower()
        if et in ["rmn", "mri", "tac", "ct"]:
            return 8
        return 7

    def info(self) -> dict:
        data = super().info()
        data["exam_type"] = self.exam_type
        data["requires_fasting"] = self.requires_fasting
        return data


class ClinicHub:
    def __init__(self):
        self.bookings = {}

    def add(self, booking: Booking) -> bool:
        if booking.booking_id in self.bookings:
            return False
        self.bookings[booking.booking_id] = booking
        return True

    def get(self, booking_id: str) -> Booking | None:
        return self.bookings.get(booking_id)

    def update(self, booking_id: str, new_booking: Booking) -> None:
        if booking_id in self.bookings:
            self.bookings[booking_id] = new_booking

    def patch_status(self, booking_id: str, new_status: str) -> None:
        if booking_id in self.bookings:
            self.bookings[booking_id].status = new_status

    def delete(self, booking_id: str) -> bool:
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return True
        return False

    def list_all(self) -> list[dict]:
        return [b.info() for b in self.bookings.values()]


app = Flask(__name__)
clinic_hub = ClinicHub()

visit1 = MedicalVisit(
    booking_id="BK-101",
    patient_name="Mario Rossi",
    doctor="Dr. Bianchi",
    department="Cardiologia",
    date="2026-02-10",
    time="10:00",
    status="scheduled",
    visit_reason="Dolore toracico",
    first_time=True
)

exam1 = DiagnosticExam(
    booking_id="BK-202",
    patient_name="Luca Verdi",
    doctor="Dr. Neri",
    department="Radiologia",
    date="2026-02-12",
    time="14:30",
    status="scheduled",
    exam_type="RMN",
    requires_fasting=True
)

visit2 = MedicalVisit(
    booking_id="BK-303",
    patient_name="Anna Gialli",
    doctor="Dr. Rossini",
    department="Dermatologia",
    date="2026-02-15",
    time="09:00",
    status="completed",
    visit_reason="Controllo annuale",
    first_time=False
)

clinic_hub.add(visit1)
clinic_hub.add(exam1)
clinic_hub.add(visit2)


@app.route('/', methods=['GET'])
def home():
    welcome: dict = {
        'message': 'Clinici Booking Hub Api',
        'lista_bookings': url_for('list_bookings'),
        'BK_101': url_for('get_booking', booking_id='BK-101'),
        'BK_101_wait_': url_for('get_wait', booking_id='BK-101', crowd=1.0)
    }
    
    return jsonify(welcome),200

@app.route('/bookings', methods=['GET'])
def list_bookings():
    return jsonify(clinic_hub.list_all()), 200

@app.route('/bookings/<string:booking_id>', methods=['GET'])
def get_booking(booking_id: str):
    booking = clinic_hub.get(booking_id)
    if not booking:
        return jsonify({'errore': 'Booking non esistente'}), 404
    return jsonify(booking.info())

@app.route('/bookings/<string:booking_id>/wait/<float:crowd>', methods=['GET'])
def get_wait(booking_id: str, crowd: float):
    booking = clinic_hub.get(booking_id)
    if not booking:
        return jsonify({'errore': 'Booking non esistente'}), 404
    return jsonify({'tempo_attesa':booking.estimated_wait(crowd)}),200

@app.route('/bookings', methods=['POST'])
def create_booking():
    data: dict = request.get_json()
    new_booking = None

    if not data:
        return jsonify({'errore': 'Invio richiesta sbagliato'}), 400
    
    if data.get('type') == 'visit':
        new_booking = MedicalVisit(
            booking_id=data.get('booking_id'),
            patient_name=data.get('patient_name'),
            doctor=data.get('doctor'),
            department=data.get('department'),
            date=data.get('date'),
            time=data.get('time'),
            status=data.get('status'),
            visit_reason=data.get('visit_reason'),
            first_time=data.get('first_time')
        )
    elif data.get('type') == 'exam':
        new_booking = DiagnosticExam(
            booking_id=data.get('booking_id'),
            patient_name=data.get('patient_name'),
            doctor=data.get('doctor'),
            department=data.get('department'),
            date=data.get('date'),
            time=data.get('time'),
            status=data.get('status'),
            exam_type=data.get('exam_type'),
            requires_fasting=data.get('requires_fasting')            
        )
    else:
        return jsonify({'errore': 'Type error nella richiesta'}), 400
    
    c = clinic_hub.add(new_booking)

    if c:
        return jsonify(new_booking.info()), 201
    else:
        return jsonify({'errore': 'Booking ID già esistente'}), 400
    
@app.route('/bookings/<string:booking_id>', methods=['PUT'])
def modify_booking(booking_id: str):
    data: dict = request.get_json()
    booking = clinic_hub.get(booking_id)
    new_booking = None
    if booking:
        if data.get('type') == 'visit':
            new_booking = MedicalVisit(
                booking_id=booking_id,
                patient_name=data.get('patient_name'),
                doctor=data.get('doctor'),
                department=data.get('department'),
                date=data.get('date'),
                time=data.get('time'),
                status=data.get('status'),
                visit_reason=data.get('visit_reason'),
                first_time=data.get('first_time')
            )
            clinic_hub.update(booking_id, new_booking)
            return jsonify(new_booking.info()), 200
        elif data.get('type') == 'exam':
            new_booking = DiagnosticExam(
                booking_id=booking_id,
                patient_name=data.get('patient_name'),
                doctor=data.get('doctor'),
                department=data.get('department'),
                date=data.get('date'),
                time=data.get('time'),
                status=data.get('status'),
                exam_type=data.get('exam_type'),
                requires_fasting=data.get('requires_fasting')            
            )
            clinic_hub.update(booking_id, new_booking)
            return jsonify(new_booking.info()), 200
        else:
            return jsonify({'errore': 'Type error nella richiesta'}), 400
    elif not booking:
        if data.get('type') == 'visit':
            new_booking = MedicalVisit(
                booking_id=booking_id,
                patient_name=data.get('patient_name'),
                doctor=data.get('doctor'),
                department=data.get('department'),
                date=data.get('date'),
                time=data.get('time'),
                status=data.get('status'),
                visit_reason=data.get('visit_reason'),
                first_time=data.get('first_time')
            )
            clinic_hub.add(new_booking)
            return jsonify(new_booking.info()), 201
        elif data.get('type') == 'exam':
            new_booking = DiagnosticExam(
                booking_id=booking_id,
                patient_name=data.get('patient_name'),
                doctor=data.get('doctor'),
                department=data.get('department'),
                date=data.get('date'),
                time=data.get('time'),
                status=data.get('status'),
                exam_type=data.get('exam_type'),
                requires_fasting=data.get('requires_fasting')            
            )
            clinic_hub.add(new_booking)
            return jsonify(new_booking.info()), 201
        else:
            return jsonify({'errore': 'Type error nella richiesta'}), 400
        
@app.route('/bookings/<string:booking_id>/status', methods=['PATCH'])
def update_status(booking_id: str):
    data = request.get_json()
    booking = clinic_hub.get(booking_id)
    status = data.get('status')
    if booking:
        clinic_hub.patch_status(booking_id, status)
        return jsonify(booking.info()), 200
    else:
        return jsonify({'errore': 'Prenotazione non esistente'}), 404
    
@app.route('/bookings/<string:booking_id>', methods=['DELETE'])
def delete_booking(booking_id:str):
    booking = clinic_hub.get(booking_id)
    if booking:
        clinic_hub.delete(booking_id)
        return jsonify({
            'deleted': True,
            'booking_id': booking_id
        })
    else:
        return jsonify({'errore': 'Prenotazione non esistente'}), 404