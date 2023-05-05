from datetime import datetime
from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel
from dto.dto_common import BasePage
from enums.enum_method import Method

from enums.enum_tipe import Tipe
from model.model_transaction import Transaction
from util.util_date_time import convert_datetime_str


class InputTransaction(BaseModel):
    tipe: Tipe
    amount: int
    notes: Optional[str]
    method: Method


class OutputTransactionPage(BasePage):
    data: List[Transaction]

    class Config:
        json_encoders = {ObjectId: str, datetime: convert_datetime_str}
