from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LedgerEntry(Base):
    __tablename__ = "ledger_entries"

    id = Column(Integer, primary_key=True)
    operation = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, nullable=False, unique=True)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False)
