from sqlalchemy import text
from app.common.db import db

class StoredProgramDAO:

    @staticmethod
    def call_insert_panel_type(name, max_power):
        sql = text("CALL sp_insert_panel_type(:name, :power)")
        try:
            db.session.execute(sql, {"name": name, "power": max_power})
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error: {e}")
            return False

    @staticmethod
    def call_link_user_station(email, station_name):
        sql = text("CALL sp_link_user_to_station(:email, :station)")
        try:
            db.session.execute(sql, {"email": email, "station": station_name})
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return str(e)

    @staticmethod
    def call_insert_nonames():
        sql = text("CALL sp_insert_nonames()")
        try:
            db.session.execute(sql)
            db.session.commit()
            return "Batch insert completed"
        except Exception as e:
            db.session.rollback()
            return str(e)

    @staticmethod
    def call_dynamic_aggregation(table, column, func):
        try:
            sql_call = text(f"CALL sp_dynamic_aggregation(:t, :c, :f, @res)")
            db.session.execute(sql_call, {"t": table, "c": column, "f": func})
            result = db.session.execute(text("SELECT @res")).scalar()
            return result
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def call_cursor_tables():
        sql = text("CALL sp_cursor_create_tables()")
        try:
            db.session.execute(sql)
            db.session.commit()
            return "Dynamic tables created"
        except Exception as e:
            return str(e)


    @staticmethod
    def create_test_station(name):
        sql = text("INSERT INTO station (name, address_id) VALUES (:name, NULL)")
        try:
            db.session.execute(sql, {"name": name})
            db.session.commit()
            res = db.session.execute(text("SELECT LAST_INSERT_ID()")).scalar()
            return res
        except Exception as e:
            db.session.rollback()
            return str(e)

    @staticmethod
    def add_maintenance_log(station_id, text_val):
        sql = text("INSERT INTO maintenance_logs (station_id, description) VALUES (:sid, :desc)")
        try:
            db.session.execute(sql, {"sid": station_id, "desc": text_val})
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return str(e)

    @staticmethod
    def delete_station_raw(station_id):
        sql = text("DELETE FROM station WHERE id = :sid")
        try:
            db.session.execute(sql, {"sid": station_id})
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return str(e)

    @staticmethod
    def get_audit_logs():
        sql = text("SELECT * FROM audit_log_deleted ORDER BY id DESC LIMIT 5")
        try:
            result = db.session.execute(sql).mappings().all()
            return [dict(row) for row in result]
        except Exception as e:
            return str(e)

    @staticmethod
    def get_all_maintenance_logs(station_id=None):
        if station_id:
            sql = text("SELECT * FROM maintenance_logs WHERE station_id = :sid ORDER BY log_date DESC")
            params = {"sid": station_id}
        else:
            sql = text("SELECT * FROM maintenance_logs ORDER BY log_date DESC")
            params = {}

        try:
            result = db.session.execute(sql, params).mappings().all()

            logs = []
            for row in result:
                row_dict = dict(row)
                if row_dict.get('log_date'):
                    row_dict['log_date'] = str(row_dict['log_date'])
                logs.append(row_dict)

            return logs
        except Exception as e:
            return str(e)