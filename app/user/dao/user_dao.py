from app.common.base_dao import BaseDAO
from app.user.domain.models import User

class UserDAO(BaseDAO):
    model = User
