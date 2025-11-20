from flask import Blueprint, request, jsonify
from app.user.service.battery_charge_service import BatteryChargeService

battery_charge_bp = Blueprint("battery_charge_bp", __name__, url_prefix="/api/battery-charges")

# --- CRUD ---
@battery_charge_bp.route("", methods=["GET"])
def list_charges():
    return jsonify(BatteryChargeService.list_charges())

@battery_charge_bp.route("/<int:charge_id>", methods=["GET"])
def get_charge(charge_id):
    c = BatteryChargeService.get_charge(charge_id)
    if not c:
        return jsonify({"message": "Not found"}), 404
    return jsonify(c)

@battery_charge_bp.route("", methods=["POST"])
def create_charge():
    data = request.json
    return jsonify(BatteryChargeService.create_charge(data)), 201

@battery_charge_bp.route("/<int:charge_id>", methods=["PUT"])
def update_charge(charge_id):
    data = request.json
    res = BatteryChargeService.update_charge(charge_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@battery_charge_bp.route("/<int:charge_id>", methods=["DELETE"])
def delete_charge(charge_id):
    ok = BatteryChargeService.delete_charge(charge_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})

# --- M:1 ---
@battery_charge_bp.route("/<int:charge_id>/battery", methods=["GET"])
def get_battery_of_charge(charge_id):
    battery = BatteryChargeService.get_battery_of_charge(charge_id)
    if not battery:
        return jsonify({"message": "Not found"}), 404
    return jsonify(battery)
