from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from enums.enum_method import Method

from enums.enum_tipe import Tipe
from model.model_common import PyObjectId
from util.util_date_time import convert_datetime_str


class Transaction(BaseModel):
    id: PyObjectId = Field(alias="_id", default_factory=ObjectId)
    created_time: datetime = Field(default_factory=datetime.now)
    tipe: Tipe
    amount: int
    notes: Optional[str]
    method: Method
    user_id: str

    class Config:
        json_encoders = {ObjectId: str, datetime: convert_datetime_str}
