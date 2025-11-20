from app.user.domain.schemas import (
    address_schema, addresses_schema,
    panel_type_schema, panel_types_schema,
    panel_generation_schema, panel_generations_schema,
    battery_charge_schema, battery_charges_schema,
    energy_sale_schema, energy_sales_schema
)

class GenericService:
    schema_map = {
        "address": (address_schema, addresses_schema),
        "panel_type": (panel_type_schema, panel_types_schema),
        "panel_generation": (panel_generation_schema, panel_generations_schema),
        "battery_charge": (battery_charge_schema, battery_charges_schema),
        "energy_sale": (energy_sale_schema, energy_sales_schema),
    }

    @staticmethod
    def serialize(obj, name):
        schema, _ = GenericService.schema_map[name]
        return schema.dump(obj)

    @staticmethod
    def serialize_many(objs, name):
        _, schema_many = GenericService.schema_map[name]
        return schema_many.dump(objs)
