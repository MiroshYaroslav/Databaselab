from flask import Blueprint, request, jsonify
from app.user.service.panel_generation_service import PanelGenerationService

panel_generation_bp = Blueprint("panel_generation_bp", __name__, url_prefix="/api/panel-generations")

# --- CRUD ---
@panel_generation_bp.route("", methods=["GET"])
def list_generations():
    return jsonify(PanelGenerationService.list_generations())

@panel_generation_bp.route("/<int:generation_id>", methods=["GET"])
def get_generation(generation_id):
    g = PanelGenerationService.get_generation(generation_id)
    if not g:
        return jsonify({"message": "Not found"}), 404
    return jsonify(g)

@panel_generation_bp.route("", methods=["POST"])
def create_generation():
    data = request.json
    return jsonify(PanelGenerationService.create_generation(data)), 201

@panel_generation_bp.route("/<int:generation_id>", methods=["PUT"])
def update_generation(generation_id):
    data = request.json
    res = PanelGenerationService.update_generation(generation_id, data)
    if not res:
        return jsonify({"message": "Not found"}), 404
    return jsonify(res)

@panel_generation_bp.route("/<int:generation_id>", methods=["DELETE"])
def delete_generation(generation_id):
    ok = PanelGenerationService.delete_generation(generation_id)
    if not ok:
        return jsonify({"message": "Not found"}), 404
    return jsonify({"message": "deleted"})

# --- M:1 ---
@panel_generation_bp.route("/<int:generation_id>/panel", methods=["GET"])
def get_panel_of_generation(generation_id):
    panel = PanelGenerationService.get_panel_of_generation(generation_id)
    if not panel:
        return jsonify({"message": "Not found"}), 404
    return jsonify(panel)
