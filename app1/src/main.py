from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app1.src.ledger.schemas import LedgerEntryCreate
from app1.src.ledger.service import LedgerService
from core.database import get_db

app = FastAPI()
service = LedgerService()


@app.post("/ledger")
async def create_entry(entry: LedgerEntryCreate, db: Session = Depends(get_db)):
    try:
        return service.create_entry(db, entry)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/ledger/{owner_id}")
def get_balance(owner_id: str, db: Session = Depends(get_db)):
    return {"balance": service.get_balance(db, owner_id)}
