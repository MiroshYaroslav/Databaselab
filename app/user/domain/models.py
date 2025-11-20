from app.common.db import db
from app.common.models_base import BaseModel

user_station = db.Table(
    'user_station',
    db.Column('user_id', db.BigInteger, db.ForeignKey('user.id'), primary_key=True),
    db.Column('station_id', db.BigInteger, db.ForeignKey('station.id'), primary_key=True)
)

class User(BaseModel):
    __tablename__ = 'user'
    surname = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    stations = db.relationship('Station', secondary=user_station, back_populates='users')

class Address(BaseModel):
    __tablename__ = 'address'
    city = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    house_number = db.Column(db.String(10), nullable=False)
    stations = db.relationship('Station', back_populates='address')

class Station(BaseModel):
    __tablename__ = 'station'
    name = db.Column(db.String(100), nullable=False)
    installation_date = db.Column(db.Date)
    address_id = db.Column(db.BigInteger, db.ForeignKey('address.id'))
    address = db.relationship('Address', back_populates='stations')
    users = db.relationship('User', secondary=user_station, back_populates='stations')
    panels = db.relationship('Panel', back_populates='station')
    batteries = db.relationship('Battery', back_populates='station')
    energy_sales = db.relationship('EnergySale', back_populates='station')

class PanelType(BaseModel):
    __tablename__ = 'panel_type'
    name = db.Column(db.String(50), nullable=False)
    max_power_watt = db.Column(db.Float, nullable=False)
    panels = db.relationship('Panel', back_populates='type')

class Panel(BaseModel):
    __tablename__ = 'panel'
    station_id = db.Column(db.BigInteger, db.ForeignKey('station.id'), nullable=False)
    type_id = db.Column(db.BigInteger, db.ForeignKey('panel_type.id'), nullable=False)
    angle = db.Column(db.Float)
    installation_date = db.Column(db.Date)
    station = db.relationship('Station', back_populates='panels')
    type = db.relationship('PanelType', back_populates='panels')
    generations = db.relationship('PanelGeneration', back_populates='panel')

class Battery(BaseModel):
    __tablename__ = 'battery'
    station_id = db.Column(db.BigInteger, db.ForeignKey('station.id'), nullable=False)
    capacity_kwh = db.Column(db.Float, nullable=False)
    lifetime_years = db.Column(db.Integer)
    station = db.relationship('Station', back_populates='batteries')
    charges = db.relationship('BatteryCharge', back_populates='battery')

class PanelGeneration(BaseModel):
    __tablename__ = 'panel_generation'
    panel_id = db.Column(db.BigInteger, db.ForeignKey('panel.id'), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    power_generated_kw = db.Column(db.Float)
    panel = db.relationship('Panel', back_populates='generations')

class BatteryCharge(BaseModel):
    __tablename__ = 'battery_charge'
    battery_id = db.Column(db.BigInteger, db.ForeignKey('battery.id'), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    charge_percent = db.Column(db.Integer)
    battery = db.relationship('Battery', back_populates='charges')

class EnergySale(BaseModel):
    __tablename__ = 'energy_sale'
    station_id = db.Column(db.BigInteger, db.ForeignKey('station.id'), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    energy_sold_kwh = db.Column(db.Float)
    price_per_kwh = db.Column(db.Float)
    station = db.relationship('Station', back_populates='energy_sales')
