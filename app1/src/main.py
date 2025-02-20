from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app1.src.ledger.schemas import LedgerEntryCreate
from app1.src.ledger.service import LedgerService
from core.database import get_db

app = FastAPI()
service = LedgerService()


@app.post("/ledger")
def create_entry(entry: LedgerEntryCreate, db: Session = Depends(get_db)):
    return service.create_entry(db, entry)


@app.get("/ledger/{owner_id}")
def get_balance(owner_id: str, db: Session = Depends(get_db)):
    return {"balance": service.get_balance(db, owner_id)}
