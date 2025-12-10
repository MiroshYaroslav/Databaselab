from flask import Blueprint, request, jsonify
from app.user.service.stored_program_service import StoredProgramService

sp_bp = Blueprint('stored_programs', __name__, url_prefix='/api/proc')

@sp_bp.route('/panel-type', methods=['POST'])
def add_panel_type():
    # Body: {"name": "EcoPanel", "max_power_watt": 450}
    data = request.json
    success = StoredProgramService.add_panel_type(data)
    if success:
        return jsonify({"message": "Panel type added via procedure"}), 201
    return jsonify({"error": "Failed to add"}), 400

@sp_bp.route('/link-user-station', methods=['POST'])
def link_user_station():
    # Body: {"email": "user@ex.com", "station_name": "Station 1"}
    data = request.json
    res = StoredProgramService.link_user_station(data)
    if res is True:
        return jsonify({"message": "Linked successfully"}), 200
    return jsonify({"error": res}), 400

@sp_bp.route('/generate-users', methods=['POST'])
def generate_users():
    res = StoredProgramService.generate_dummy_users()
    return jsonify({"message": res}), 200

@sp_bp.route('/aggregate', methods=['POST'])
def aggregate_data():
    # Body: {"table": "battery", "column": "capacity_kwh", "func": "AVG"}
    data = request.json
    result = StoredProgramService.get_aggregation(data)
    return jsonify({"result": result}), 200

@sp_bp.route('/create-dynamic-tables', methods=['POST'])
def create_dynamic_tables():
    res = StoredProgramService.run_dynamic_tables()
    return jsonify({"message": res}), 200


@sp_bp.route('/test/log', methods=['POST'])
def add_test_log():
    data = request.json
    res = StoredProgramService.add_log_test(data)

    if res is True:
        return jsonify({"message": "Log added successfully"}), 201

    return jsonify({"error_from_trigger": res}), 400


@sp_bp.route('/test/station/<int:id>', methods=['DELETE'])
def delete_test_station(id):
    res = StoredProgramService.delete_station_test(id)
    if res is True:
        return jsonify({"message": "Station deleted. Check audit log."}), 200
    return jsonify({"error_from_trigger": res}), 400


@sp_bp.route('/test/audit', methods=['GET'])
def get_audit_log():
    res = StoredProgramService.get_audit()
    return jsonify(res), 200