from app.common.db import db

class BaseDAO:
    model = None

    @classmethod
    def get_all(cls):
        return cls.model.query.all()

    @classmethod
    def get_by_id(cls, id_):
        return cls.model.query.get(id_)

    @classmethod
    def create(cls, data):
        obj = cls.model(**data)
        try:
            db.session.add(obj)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        return obj

    @classmethod
    def update(cls, id_, data):
        obj = cls.get_by_id(id_)
        if not obj:
            return None
        for k, v in data.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        return obj

    @classmethod
    def delete(cls, id_):
        obj = cls.get_by_id(id_)
        if not obj:
            return False
        try:
            db.session.delete(obj)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
        return True

    @classmethod
    def query(cls):
        return cls.model.query
