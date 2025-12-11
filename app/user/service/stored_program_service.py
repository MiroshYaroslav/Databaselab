from app.user.dao.stored_program_dao import StoredProgramDAO

class StoredProgramService:

    @staticmethod
    def add_panel_type(data):
        return StoredProgramDAO.call_insert_panel_type(data.get('name'), data.get('max_power_watt'))

    @staticmethod
    def link_user_station(data):
        return StoredProgramDAO.call_link_user_station(data.get('email'), data.get('station_name'))

    @staticmethod
    def generate_dummy_users():
        return StoredProgramDAO.call_insert_nonames()

    @staticmethod
    def get_aggregation(data):
        return StoredProgramDAO.call_dynamic_aggregation(
            data.get('table'),
            data.get('column'),
            data.get('func')
        )

    @staticmethod
    def run_dynamic_tables():
        return StoredProgramDAO.call_cursor_tables()

    @staticmethod
    def create_station_test(name):
        return StoredProgramDAO.create_test_station(name)

    @staticmethod
    def add_log_test(data):
        return StoredProgramDAO.add_maintenance_log(data.get('station_id'), data.get('description'))

    @staticmethod
    def delete_station_test(station_id):
        return StoredProgramDAO.delete_station_raw(station_id)

    @staticmethod
    def get_audit():
        return StoredProgramDAO.get_audit_logs()

    @staticmethod
    def get_logs(station_id=None):
        return StoredProgramDAO.get_all_maintenance_logs(station_id)