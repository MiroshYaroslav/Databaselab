from app.common.base_dao import BaseDAO
from app.user.domain.models import PanelGeneration

class PanelGenerationDAO(BaseDAO):
    model = PanelGeneration
