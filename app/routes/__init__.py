# app/routes/__init__.py
from app.user.controller.user_controller import user_bp
from app.user.controller.station_controller import station_bp
from app.user.controller.generic_controller import generic_bp
from app.user.controller.battery_controller import battery_bp
from app.user.controller.panel_generation_controller import panel_generation_bp
from app.user.controller.battery_charge_controller import battery_charge_bp
from app.user.controller.energy_sale_controller import energy_sale_bp
from app.user.controller.panel_controller import panel_bp
from app.user.controller.panel_type_controller import panel_type_bp
from app.user.controller.address_controller import address_bp


def register_routes(app):
    # Основні ресурси
    app.register_blueprint(user_bp)
    app.register_blueprint(station_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(panel_type_bp)
    app.register_blueprint(panel_bp)

    # Інші таблиці
    app.register_blueprint(battery_bp)
    app.register_blueprint(panel_generation_bp)
    app.register_blueprint(battery_charge_bp)
    app.register_blueprint(energy_sale_bp)

    # Для generic CRUD (за потреби)
    app.register_blueprint(generic_bp)
