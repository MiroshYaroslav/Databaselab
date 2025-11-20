from app.user.dao.battery_dao import BatteryDAO
from app.user.domain.schemas import battery_schema, batteries_schema, station_schema, battery_charges_schema

class BatteryService:
    @staticmethod
    def list_batteries():
        return batteries_schema.dump(BatteryDAO.get_all())

    @staticmethod
    def get_battery(battery_id):
        b = BatteryDAO.get_by_id(battery_id)
        return battery_schema.dump(b) if b else None

    @staticmethod
    def create_battery(data):
        b = BatteryDAO.create(data)
        return battery_schema.dump(b)

    @staticmethod
    def update_battery(battery_id, data):
        b = BatteryDAO.update(battery_id, data)
        return battery_schema.dump(b) if b else None

    @staticmethod
    def delete_battery(battery_id):
        return BatteryDAO.delete(battery_id)

    # --- M:1 ---
    @staticmethod
    def get_station_of_battery(battery_id):
        b = BatteryDAO.get_by_id(battery_id)
        if not b or not b.station:
            return None
        return station_schema.dump(b.station)

    # --- M:M ---
    @staticmethod
    def get_charges_of_battery(battery_id):
        b = BatteryDAO.get_by_id(battery_id)
        if not b:
            return []
        return battery_charges_schema.dump(b.charges)
