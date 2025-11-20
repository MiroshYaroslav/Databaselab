from app.common.base_dao import BaseDAO
from app.user.domain.models import PanelType

class PanelTypeDAO(BaseDAO):
    model = PanelType
