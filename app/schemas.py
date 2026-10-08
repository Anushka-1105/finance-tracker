from datetime import date, datetime
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

class TransactionCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    type: Literal['income', 'expense']
    category: str = Field(min_length=1, max_length=50)
    transaction_date: date

class TransactionOut(TransactionCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)