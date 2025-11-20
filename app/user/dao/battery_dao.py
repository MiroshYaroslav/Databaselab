from app.common.base_dao import BaseDAO
from app.user.domain.models import Battery

class BatteryDAO(BaseDAO):
    model = Battery
