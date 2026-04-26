from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...models.models import Alert
from sqlmodel import select

router = APIRouter()

@router.get("/", response_model=List[Alert])
def read_alerts(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    alerts = db.execute(select(Alert).offset(offset).limit(limit)).scalars().all()
    return alerts
