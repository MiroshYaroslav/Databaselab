from flask import Blueprint, request, jsonify
from app.user.service.panel_type_service import PanelTypeService

panel_type_bp = Blueprint("panel_type_bp", __name__, url_prefix="/api/panel-types")

@panel_type_bp.route("", methods=["GET"])
def list_panel_types():
    return jsonify(PanelTypeService.list_panel_types())

@panel_type_bp.route("/<int:panel_type_id>", methods=["GET"])
def get_panel_type(panel_type_id):
    pt = PanelTypeService.get_panel_type(panel_type_id)
    if not pt:
        return jsonify({"message": "Not found"}), 404
    return jsonify(pt)

@panel_type_bp.route("", methods=["POST"])
def create_panel_type():
    data = request.json
    return jsonify(PanelTypeService.create_panel_type(data)), 201

@panel_type_bp.route("/<int:panel_type_id>", methods=["PUT"])
def update_panel_type(panel_type_id):
    data = request.json
    res = PanelTypeService.update_panel_type(panel_type_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@panel_type_bp.route("/<int:panel_type_id>", methods=["DELETE"])
def delete_panel_type(panel_type_id):
    ok = PanelTypeService.delete_panel_type(panel_type_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})
