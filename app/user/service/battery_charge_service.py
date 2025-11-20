from app.user.dao.battery_charge_dao import BatteryChargeDAO
from app.user.domain.schemas import battery_charge_schema, battery_charges_schema, battery_schema

class BatteryChargeService:
    @staticmethod
    def list_charges():
        return battery_charges_schema.dump(BatteryChargeDAO.get_all())

    @staticmethod
    def get_charge(charge_id):
        c = BatteryChargeDAO.get_by_id(charge_id)
        return battery_charge_schema.dump(c) if c else None

    @staticmethod
    def create_charge(data):
        c = BatteryChargeDAO.create(data)
        return battery_charge_schema.dump(c)

    @staticmethod
    def update_charge(charge_id, data):
        c = BatteryChargeDAO.update(charge_id, data)
        return battery_charge_schema.dump(c) if c else None

    @staticmethod
    def delete_charge(charge_id):
        return BatteryChargeDAO.delete(charge_id)

    # --- M:1 ---
    @staticmethod
    def get_battery_of_charge(charge_id):
        c = BatteryChargeDAO.get_by_id(charge_id)
        if not c or not c.battery:
            return None
        return battery_schema.dump(c.battery)
