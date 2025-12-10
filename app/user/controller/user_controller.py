import traceback

from flask import Blueprint, request, jsonify
from app.user.service.user_service import UserService

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/users")

@user_bp.route("", methods=["GET"])
def list_users():
    try:
        users = UserService.list_users()
        return jsonify(users)
    except Exception as e:
        print("Error in list_users:", e)
        traceback.print_exc()
        return jsonify({"message": str(e)}), 500


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserService.get_user(user_id)
    if not user:
        return jsonify({"message": "Not found"}), 404
    return jsonify(user)

@user_bp.route("", methods=["POST"])
def create_user():
    data = request.json
    return jsonify(UserService.create_user(data)), 201

@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    res = UserService.update_user(user_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    ok = UserService.delete_user(user_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})

@user_bp.route("/<int:user_id>/stations", methods=["GET"])
def get_stations_by_user(user_id):
    stations = UserService.get_stations_by_user(user_id)
    if stations is None:
        return jsonify({"message": "User not found"}), 404
    return jsonify(stations)
