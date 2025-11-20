from app.common.base_dao import BaseDAO
from app.user.domain.models import Address

class AddressDAO(BaseDAO):
    model = Address
