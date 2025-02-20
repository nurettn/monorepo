from sqlalchemy.orm import Session

from app1.src.ledger.schemas import LedgerEntryCreate, LedgerOperation
from core.ledger.models import LedgerEntry

LEDGER_CONFIG = {
    LedgerOperation.DAILY_REWARD.value: 1,
    LedgerOperation.SIGNUP_CREDIT.value: 3,
    LedgerOperation.CREDIT_SPEND.value: -1,
    LedgerOperation.CREDIT_ADD.value: 10,
    LedgerOperation.CONTENT_CREATION.value: -5,
    LedgerOperation.CONTENT_ACCESS.value: 0
}


class LedgerService:
    def get_balance(self, db: Session, owner_id: str) -> int:
        entries = db.query(LedgerEntry).filter_by(owner_id=owner_id).all()
        return sum(LEDGER_CONFIG[e.operation] for e in entries)

    def create_entry(self, db: Session, entry: LedgerEntryCreate) -> LedgerEntry:
        if db.query(LedgerEntry).filter_by(nonce=entry.nonce).first():
            raise ValueError("Duplicate nonce")

        if LEDGER_CONFIG[entry.operation.value] < 0:
            balance = self.get_balance(db, entry.owner_id)
            if balance + LEDGER_CONFIG[entry.operation.value] < 0:
                raise ValueError("Insufficient balance")

        db_entry = LedgerEntry(**entry.dict())
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)
        return db_entry