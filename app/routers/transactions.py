from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . . import schemas, models
from . .database import get_db

router = APIRouter(prefix="/transactions", tags=["transactions"])
@router.post("/", response_model=schemas.TransactionOut, status_code=201)
def create_transaction(data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    txn = models.Transaction(**data.model_dump())
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn

@router.get("/", response_model=list[schemas.TransactionOut])
def list_transactions(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return db.query(models.Transaction).offset(skip).limit(limit).all()


@router.get("/{txn_id}", response_model=schemas.TransactionOut)
def get_transaction(txn_id: int, db: Session = Depends(get_db)):
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return txn


@router.delete("/{txn_id}", status_code=204)
def delete_transaction(txn_id: int, db: Session = Depends(get_db)):
    txn = db.query(models.Transaction).filter(models.Transaction.id == txn_id).first()
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(txn)
    db.commit()