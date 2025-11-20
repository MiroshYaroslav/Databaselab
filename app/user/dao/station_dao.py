from app.common.base_dao import BaseDAO
from app.user.domain.models import Station
from sqlalchemy.orm import joinedload

class StationDAO(BaseDAO):
    model = Station

    @classmethod
    def get_with_address(cls, station_id):
        return Station.query.options(joinedload(Station.address)).filter_by(id=station_id).first()

    @classmethod
    def get_with_panels_and_batteries(cls, station_id):
        return Station.query.options(
            joinedload(Station.panels).joinedload('type'),
            joinedload(Station.batteries)
        ).filter_by(id=station_id).first()

    @classmethod
    def find_by_name_like(cls, name_part):
        return Station.query.filter(Station.name.ilike(f"%{name_part}%")).all()
