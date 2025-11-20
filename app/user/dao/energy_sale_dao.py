from app.common.base_dao import BaseDAO
from app.user.domain.models import EnergySale

class EnergySaleDAO(BaseDAO):
    model = EnergySale
