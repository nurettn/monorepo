from core.ledger.schemas import BaseLedgerEntryCreate, BaseLedgerOperation


class LedgerOperation(BaseLedgerOperation):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

    # app specific
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


class LedgerEntryCreate(BaseLedgerEntryCreate):
    operation: LedgerOperation

    class Config:
        use_enum_values = True