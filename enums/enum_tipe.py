from enum import Enum


class Tipe(str, Enum):
    def __str__(self):
        return str(self.value)

    INCOME = "INCOME"
    PURCHASE = "PURCHASE"
    INVEST = "INVEST"
