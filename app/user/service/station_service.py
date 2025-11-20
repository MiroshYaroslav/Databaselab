from app.user.dao.station_dao import StationDAO
from app.user.domain.schemas import station_schema, stations_schema, address_schema, users_schema

class StationService:
    @staticmethod
    def list_stations():
        return stations_schema.dump(StationDAO.get_all())

    @staticmethod
    def get_station(station_id):
        s = StationDAO.get_by_id(station_id)
        return station_schema.dump(s) if s else None

    @staticmethod
    def create_station(data):
        s = StationDAO.create(data)
        return station_schema.dump(s)

    @staticmethod
    def update_station(station_id, data):
        s = StationDAO.update(station_id, data)
        return station_schema.dump(s) if s else None

    @staticmethod
    def delete_station(station_id):
        return StationDAO.delete(station_id)

    # --- M:1 ---
    @staticmethod
    def get_address_of_station(station_id):
        s = StationDAO.get_by_id(station_id)
        if not s or not s.address:
            return None
        return address_schema.dump(s.address)

    # --- M:M ---
    @staticmethod
    def get_users_of_station(station_id):
        s = StationDAO.get_by_id(station_id)
        if not s:
            return None
        return users_schema.dump(s.users)
