from app.user.dao.panel_generation_dao import PanelGenerationDAO
from app.user.domain.schemas import panel_generation_schema, panel_generations_schema, panel_schema

class PanelGenerationService:
    @staticmethod
    def list_generations():
        return panel_generations_schema.dump(PanelGenerationDAO.get_all())

    @staticmethod
    def get_generation(generation_id):
        g = PanelGenerationDAO.get_by_id(generation_id)
        return panel_generation_schema.dump(g) if g else None

    @staticmethod
    def create_generation(data):
        g = PanelGenerationDAO.create(data)
        return panel_generation_schema.dump(g)

    @staticmethod
    def update_generation(generation_id, data):
        g = PanelGenerationDAO.update(generation_id, data)
        return panel_generation_schema.dump(g) if g else None

    @staticmethod
    def delete_generation(generation_id):
        return PanelGenerationDAO.delete(generation_id)

    # --- M:1 ---
    @staticmethod
    def get_panel_of_generation(generation_id):
        g = PanelGenerationDAO.get_by_id(generation_id)
        if not g or not g.panel:
            return None
        return panel_schema.dump(g.panel)
