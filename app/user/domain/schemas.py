from app.common.db import ma
from app.user.domain.models import *

class GenericSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        include_relationships = True
        load_instance = True

UserSchema = type("UserSchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": User})})
AddressSchema = type("AddressSchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": Address})})
StationSchema = type("StationSchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": Station})})
PanelTypeSchema = type("PanelTypeSchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": PanelType})})
PanelSchema = type("PanelSchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": Panel})})
BatterySchema = type("BatterySchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": Battery})})
PanelGenerationSchema = type("PanelGenerationSchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": PanelGeneration})})
BatteryChargeSchema = type("BatteryChargeSchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": BatteryCharge})})
EnergySaleSchema = type("EnergySaleSchema", (GenericSchema,), {"Meta": type("Meta", (), {"model": EnergySale})})

user_schema = UserSchema()
users_schema = UserSchema(many=True)
address_schema = AddressSchema()
addresses_schema = AddressSchema(many=True)
station_schema = StationSchema()
stations_schema = StationSchema(many=True)
panel_type_schema = PanelTypeSchema()
panel_types_schema = PanelTypeSchema(many=True)
panel_schema = PanelSchema()
panels_schema = PanelSchema(many=True)
battery_schema = BatterySchema()
batteries_schema = BatterySchema(many=True)
panel_generation_schema = PanelGenerationSchema()
panel_generations_schema = PanelGenerationSchema(many=True)
battery_charge_schema = BatteryChargeSchema()
battery_charges_schema = BatteryChargeSchema(many=True)
energy_sale_schema = EnergySaleSchema()
energy_sales_schema = EnergySaleSchema(many=True)
