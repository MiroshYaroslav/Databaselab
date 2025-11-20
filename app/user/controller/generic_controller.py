from flask import Blueprint, request, jsonify
from app.user.service.generic_service import GenericService
from app.user.domain.models import (
    User,
    Address,
    Station,
    PanelType,
    Panel,
    Battery,
    PanelGeneration,
    BatteryCharge,
    EnergySale
)

MODEL_MAP = {
    "user": User,
    "address": Address,
    "station": Station,
    "panel_type": PanelType,
    "panel": Panel,
    "battery": Battery,
    "panel_generation": PanelGeneration,
    "battery_charge": BatteryCharge,
    "energy_sale": EnergySale
}


generic_bp = Blueprint("generic_bp", __name__, url_prefix="/api")

from app.user.dao.generic_dao import GenericDAO

@generic_bp.route("/<model_name>", methods=["GET"])
def list_model(model_name):
    Model = MODEL_MAP.get(model_name)
    if not Model:
        return jsonify({"message": "Model not found"}), 404
    GenericDAO.model = Model
    objs = GenericDAO.get_all()
    return jsonify(GenericService.serialize_many(objs, model_name))

@generic_bp.route("/<model_name>/<int:obj_id>", methods=["GET"])
def get_model(model_name, obj_id):
    Model = MODEL_MAP.get(model_name)
    if not Model:
        return jsonify({"message": "Model not found"}), 404
    GenericDAO.model = Model
    obj = GenericDAO.get_by_id(obj_id)
    return jsonify(GenericService.serialize(obj, model_name)) if obj else ({"message": "Not found"}, 404)

@generic_bp.route("/<model_name>", methods=["POST"])
def create_model(model_name):
    data = request.json
    Model = MODEL_MAP.get(model_name)
    if not Model:
        return jsonify({"message": "Model not found"}), 404
    GenericDAO.model = Model
    obj = GenericDAO.create(data)
    return jsonify(GenericService.serialize(obj, model_name)), 201

@generic_bp.route("/<model_name>/<int:obj_id>", methods=["PUT"])
def update_model(model_name, obj_id):
    data = request.json
    Model = MODEL_MAP.get(model_name)
    if not Model:
        return jsonify({"message": "Model not found"}), 404
    GenericDAO.model = Model
    obj = GenericDAO.update(obj_id, data)
    return jsonify(GenericService.serialize(obj, model_name)) if obj else ({"message": "Not found"}, 404)

@generic_bp.route("/<model_name>/<int:obj_id>", methods=["DELETE"])
def delete_model(model_name, obj_id):
    Model = MODEL_MAP.get(model_name)
    if not Model:
        return jsonify({"message": "Model not found"}), 404
    GenericDAO.model = Model
    ok = GenericDAO.delete(obj_id)
    return jsonify({"message": "deleted"}) if ok else ({"message": "Not found"}, 404)
