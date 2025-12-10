from flask import Blueprint, request, jsonify
from app.user.service.address_service import AddressService

address_bp = Blueprint("address_bp", __name__, url_prefix="/api/addresses")

@address_bp.route("", methods=["GET"])
def list_addresses():
    return jsonify(AddressService.list_addresses())

@address_bp.route("/<int:address_id>", methods=["GET"])
def get_address(address_id):
    a = AddressService.get_address(address_id)
    if not a:
        return jsonify({"message": "Not found"}), 404
    return jsonify(a)

@address_bp.route("", methods=["POST"])
def create_address():
    data = request.json
    return jsonify(AddressService.create_address(data)), 201

@address_bp.route("/<int:address_id>", methods=["PUT"])
def update_address(address_id):
    data = request.json
    res = AddressService.update_address(address_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@address_bp.route("/<int:address_id>", methods=["DELETE"])
def delete_address(address_id):
    ok = AddressService.delete_address(address_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})

@address_bp.route("/<int:address_id>/users", methods=["GET"])
def get_users_by_address(address_id):
    users = AddressService.get_users_by_address(address_id)
    if users is None:
        return jsonify({"message": "Address not found"}), 404
    return jsonify(users)
