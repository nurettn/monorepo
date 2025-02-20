import enum
from datetime import datetime

from pydantic import BaseModel


class LedgerOpMeta(enum.EnumMeta):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        required_ops = namespace.get("_required_operations")
        if required_ops is not None:
            missing = set(required_ops) - set(cls.__members__)
            if missing:
                raise TypeError(f"Missing required operations: {', '.join(missing)}")


class CoreLedgerOperation(enum.Enum, metaclass=LedgerOpMeta):
    _required_operations = {"DAILY_REWARD", "SIGNUP_CREDIT", "CREDIT_SPEND", "CREDIT_ADD"}

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
