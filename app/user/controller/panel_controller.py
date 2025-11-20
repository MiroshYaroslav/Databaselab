from flask import Blueprint, request, jsonify
from app.user.service.panel_service import PanelService

panel_bp = Blueprint("panel_bp", __name__, url_prefix="/api/panels")

# --- CRUD ---
@panel_bp.route("", methods=["GET"])
def list_panels():
    return jsonify(PanelService.list_panels())

@panel_bp.route("/<int:panel_id>", methods=["GET"])
def get_panel(panel_id):
    p = PanelService.get_panel(panel_id)
    if not p:
        return jsonify({"message": "Not found"}), 404
    return jsonify(p)

@panel_bp.route("", methods=["POST"])
def create_panel():
    data = request.json
    return jsonify(PanelService.create_panel(data)), 201

@panel_bp.route("/<int:panel_id>", methods=["PUT"])
def update_panel(panel_id):
    data = request.json
    res = PanelService.update_panel(panel_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@panel_bp.route("/<int:panel_id>", methods=["DELETE"])
def delete_panel(panel_id):
    ok = PanelService.delete_panel(panel_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})

# --- M:1 relationships ---
@panel_bp.route("/<int:panel_id>/station", methods=["GET"])
def get_station_of_panel(panel_id):
    station = PanelService.get_station_of_panel(panel_id)
    if not station:
        return jsonify({"message": "Not found"}), 404
    return jsonify(station)

@panel_bp.route("/<int:panel_id>/type", methods=["GET"])
def get_type_of_panel(panel_id):
    type_ = PanelService.get_type_of_panel(panel_id)
    if not type_:
        return jsonify({"message": "Not found"}), 404
    return jsonify(type_)
