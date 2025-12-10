from flask import Blueprint, request, jsonify
from app.user.service.energy_sale_service import EnergySaleService

energy_sale_bp = Blueprint("energy_sale_bp", __name__, url_prefix="/api/energy-sales")

@energy_sale_bp.route("", methods=["GET"])
def list_sales():
    return jsonify(EnergySaleService.list_sales())

@energy_sale_bp.route("/<int:sale_id>", methods=["GET"])
def get_sale(sale_id):
    s = EnergySaleService.get_sale(sale_id)
    if not s:
        return jsonify({"message": "Not found"}), 404
    return jsonify(s)

@energy_sale_bp.route("", methods=["POST"])
def create_sale():
    data = request.json
    return jsonify(EnergySaleService.create_sale(data)), 201

@energy_sale_bp.route("/<int:sale_id>", methods=["PUT"])
def update_sale(sale_id):
    data = request.json
    res = EnergySaleService.update_sale(sale_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@energy_sale_bp.route("/<int:sale_id>", methods=["DELETE"])
def delete_sale(sale_id):
    ok = EnergySaleService.delete_sale(sale_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})

@energy_sale_bp.route("/<int:sale_id>/station", methods=["GET"])
def get_station_of_sale(sale_id):
    station = EnergySaleService.get_station_of_sale(sale_id)
    if not station:
        return jsonify({"message": "Not found"}), 404
    return jsonify(station)
