from app.user.dao.panel_dao import PanelDAO
from app.user.domain.schemas import panel_schema, panels_schema, station_schema, panel_type_schema

class PanelService:
    @staticmethod
    def list_panels():
        return panels_schema.dump(PanelDAO.get_all())

    @staticmethod
    def get_panel(panel_id):
        p = PanelDAO.get_by_id(panel_id)
        return panel_schema.dump(p) if p else None

    @staticmethod
    def create_panel(data):
        p = PanelDAO.create(data)
        return panel_schema.dump(p)

    @staticmethod
    def update_panel(panel_id, data):
        p = PanelDAO.update(panel_id, data)
        return panel_schema.dump(p) if p else None

    @staticmethod
    def delete_panel(panel_id):
        return PanelDAO.delete(panel_id)

    # --- M:1 ---
    @staticmethod
    def get_station_of_panel(panel_id):
        p = PanelDAO.get_by_id(panel_id)
        if not p or not p.station:
            return None
        return station_schema.dump(p.station)

    @staticmethod
    def get_type_of_panel(panel_id):
        p = PanelDAO.get_by_id(panel_id)
        if not p or not p.type:
            return None
        return panel_type_schema.dump(p.type)
