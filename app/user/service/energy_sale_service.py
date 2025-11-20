from app.user.dao.energy_sale_dao import EnergySaleDAO
from app.user.domain.schemas import energy_sale_schema, energy_sales_schema, station_schema

class EnergySaleService:
    @staticmethod
    def list_sales():
        return energy_sales_schema.dump(EnergySaleDAO.get_all())

    @staticmethod
    def get_sale(sale_id):
        s = EnergySaleDAO.get_by_id(sale_id)
        return energy_sale_schema.dump(s) if s else None

    @staticmethod
    def create_sale(data):
        s = EnergySaleDAO.create(data)
        return energy_sale_schema.dump(s)

    @staticmethod
    def update_sale(sale_id, data):
        s = EnergySaleDAO.update(sale_id, data)
        return energy_sale_schema.dump(s) if s else None

    @staticmethod
    def delete_sale(sale_id):
        return EnergySaleDAO.delete(sale_id)

    # --- M:1 ---
    @staticmethod
    def get_station_of_sale(sale_id):
        s = EnergySaleDAO.get_by_id(sale_id)
        if not s or not s.station:
            return None
        return station_schema.dump(s.station)
