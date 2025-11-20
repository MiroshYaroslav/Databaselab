from app.common.base_dao import BaseDAO
from app.user.domain.models import BatteryCharge

class BatteryChargeDAO(BaseDAO):
    model = BatteryCharge
