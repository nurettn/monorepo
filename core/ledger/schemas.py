import enum
from datetime import datetime

from pydantic import BaseModel


class LedgerOpMeta(enum.EnumMeta):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if cls.__name__ != "BaseLedgerOperation":
            required = set(BaseLedgerOperation.__members__)
            current = set(cls.__members__)
            missing = required - current
            if missing:
                raise TypeError(
                    f"{cls.__name__} missing required operations: {', '.join(sorted(missing))}"
                )

class BaseLedgerOperation(enum.Enum, metaclass=LedgerOpMeta):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


class BaseLedgerEntryCreate(BaseModel):
    operation: str
    amount: int
    nonce: str
    owner_id: str
    created_on: datetime