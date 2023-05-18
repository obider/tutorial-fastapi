from bson import ObjectId

from util.util_date_time import convert_str_date


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class InputDateGue(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return convert_str_date(v)
        except ValueError:
            raise ValueError("Invalid format date (DD-MM-YYYY)")

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
