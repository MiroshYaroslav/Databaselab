from app.user.dao.panel_type_dao import PanelTypeDAO
from app.user.domain.schemas import panel_type_schema, panel_types_schema

class PanelTypeService:
    @staticmethod
    def list_panel_types():
        return panel_types_schema.dump(PanelTypeDAO.get_all())

    @staticmethod
    def get_panel_type(panel_type_id):
        pt = PanelTypeDAO.get_by_id(panel_type_id)
        return panel_type_schema.dump(pt) if pt else None

    @staticmethod
    def create_panel_type(data):
        pt = PanelTypeDAO.create(data)
        return panel_type_schema.dump(pt)

    @staticmethod
    def update_panel_type(panel_type_id, data):
        pt = PanelTypeDAO.update(panel_type_id, data)
        return panel_type_schema.dump(pt) if pt else None

    @staticmethod
    def delete_panel_type(panel_type_id):
        return PanelTypeDAO.delete(panel_type_id)
