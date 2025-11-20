from flask import Blueprint, request, jsonify
from app.user.service.battery_service import BatteryService

battery_bp = Blueprint("battery_bp", __name__, url_prefix="/api/batteries")

# --- CRUD ---
@battery_bp.route("", methods=["GET"])
def list_batteries():
    return jsonify(BatteryService.list_batteries())

@battery_bp.route("/<int:battery_id>", methods=["GET"])
def get_battery(battery_id):
    b = BatteryService.get_battery(battery_id)
    if not b:
        return jsonify({"message": "Not found"}), 404
    return jsonify(b)

@battery_bp.route("", methods=["POST"])
def create_battery():
    data = request.json
    return jsonify(BatteryService.create_battery(data)), 201

@battery_bp.route("/<int:battery_id>", methods=["PUT"])
def update_battery(battery_id):
    data = request.json
    res = BatteryService.update_battery(battery_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@battery_bp.route("/<int:battery_id>", methods=["DELETE"])
def delete_battery(battery_id):
    ok = BatteryService.delete_battery(battery_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})

# --- M:1 relationship ---
@battery_bp.route("/<int:battery_id>/station", methods=["GET"])
def get_station_of_battery(battery_id):
    station = BatteryService.get_station_of_battery(battery_id)
    if not station:
        return jsonify({"message": "Not found"}), 404
    return jsonify(station)

# --- M:M relationship ---
@battery_bp.route("/<int:battery_id>/charges", methods=["GET"])
def get_charges_of_battery(battery_id):
    charges = BatteryService.get_charges_of_battery(battery_id)
    return jsonify(charges)
