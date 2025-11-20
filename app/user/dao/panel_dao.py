from app.common.base_dao import BaseDAO
from app.user.domain.models import Panel

class PanelDAO(BaseDAO):
    model = Panel
