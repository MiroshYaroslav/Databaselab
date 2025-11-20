from flask import Blueprint, request, jsonify
from app.user.service.station_service import StationService

station_bp = Blueprint("station_bp", __name__, url_prefix="/api/stations")

# --- CRUD ---
@station_bp.route("", methods=["GET"])
def list_stations():
    return jsonify(StationService.list_stations())

@station_bp.route("/<int:station_id>", methods=["GET"])
def get_station(station_id):
    s = StationService.get_station(station_id)
    if not s:
        return jsonify({"message": "Not found"}), 404
    return jsonify(s)

@station_bp.route("", methods=["POST"])
def create_station():
    data = request.json
    return jsonify(StationService.create_station(data)), 201

@station_bp.route("/<int:station_id>", methods=["PUT"])
def update_station(station_id):
    data = request.json
    res = StationService.update_station(station_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@station_bp.route("/<int:station_id>", methods=["DELETE"])
def delete_station(station_id):
    ok = StationService.delete_station(station_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})

# --- M:1 relationship ---
@station_bp.route("/<int:station_id>/address", methods=["GET"])
def get_address_of_station(station_id):
    address = StationService.get_address_of_station(station_id)
    if not address:
        return jsonify({"message": "Not found"}), 404
    return jsonify(address)

# --- M:M relationship ---
@station_bp.route("/<int:station_id>/users", methods=["GET"])
def get_users_of_station(station_id):
    users = StationService.get_users_of_station(station_id)
    if users is None:
        return jsonify({"message": "Station not found"}), 404
    return jsonify(users)
