from app.user.dao.address_dao import AddressDAO
from app.user.domain.schemas import address_schema, addresses_schema, users_schema

class AddressService:
    @staticmethod
    def list_addresses():
        return addresses_schema.dump(AddressDAO.get_all())

    @staticmethod
    def get_address(address_id):
        a = AddressDAO.get_by_id(address_id)
        return address_schema.dump(a) if a else None

    @staticmethod
    def create_address(data):
        a = AddressDAO.create(data)
        return address_schema.dump(a)

    @staticmethod
    def update_address(address_id, data):
        a = AddressDAO.update(address_id, data)
        return address_schema.dump(a) if a else None

    @staticmethod
    def delete_address(address_id):
        return AddressDAO.delete(address_id)

    # --- M:1 ---
    @staticmethod
    def get_users_by_address(address_id):
        address = AddressDAO.get_by_id(address_id)
        if not address:
            return None
        return users_schema.dump(address.users)
