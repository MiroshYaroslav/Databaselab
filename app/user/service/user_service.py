from app.user.dao.user_dao import UserDAO
from app.user.domain.schemas import user_schema, users_schema, stations_schema

class UserService:
    @staticmethod
    def list_users():
        return users_schema.dump(UserDAO.get_all())

    @staticmethod
    def get_user(user_id):
        u = UserDAO.get_by_id(user_id)
        return user_schema.dump(u) if u else None

    @staticmethod
    def create_user(data):
        u = UserDAO.create(data)
        return user_schema.dump(u)

    @staticmethod
    def update_user(user_id, data):
        u = UserDAO.update(user_id, data)
        return user_schema.dump(u) if u else None

    @staticmethod
    def delete_user(user_id):
        return UserDAO.delete(user_id)

    # --- M:M ---
    @staticmethod
    def get_stations_by_user(user_id):
        user = UserDAO.get_by_id(user_id)
        if not user:
            return None
        return stations_schema.dump(user.stations)
