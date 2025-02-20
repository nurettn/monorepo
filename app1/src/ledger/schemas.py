from enum import Enum

from core.ledger.schemas import BaseLedgerEntryCreate, CoreLedgerOperation


class LedgerOperation(Enum):
    DAILY_REWARD = CoreLedgerOperation.DAILY_REWARD.value
    SIGNUP_CREDIT = CoreLedgerOperation.SIGNUP_CREDIT.value
    CREDIT_SPEND = CoreLedgerOperation.CREDIT_SPEND.value
    CREDIT_ADD = CoreLedgerOperation.CREDIT_ADD.value

    # App-specific
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


class LedgerEntryCreate(BaseLedgerEntryCreate):
    operation: LedgerOperation

    class Config:
        use_enum_values = True
