from enum import Enum


class Method(str, Enum):
    def __str__(self):
        return str(self.value)

    CASH = "CASH"
    EWALLET = "EWALLET"
    BANK = "BANK"
