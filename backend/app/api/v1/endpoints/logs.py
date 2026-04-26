from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ...db.session import get_db
from ...models.models import LogEntry
from sqlmodel import select

router = APIRouter()

@router.get("/", response_model=List[LogEntry])
def read_logs(
    db: Session = Depends(get_db),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    level: Optional[str] = None,
    service_name: Optional[str] = None
):
    query = select(LogEntry)
    if level:
        query = query.where(LogEntry.level == level)
    if service_name:
        query = query.where(LogEntry.service_name == service_name)
    
    logs = db.execute(query.offset(offset).limit(limit)).scalars().all()
    return logs

@router.post("/", response_model=LogEntry)
def create_log(log: LogEntry, db: Session = Depends(get_db)):
    # Here we would also trigger anomaly detection
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
