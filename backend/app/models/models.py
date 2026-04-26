from typing import Optional
from datetime import datetime, timezone
from sqlmodel import SQLModel, Field

class LogEntry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    level: str = Field(index=True)
    message: str
    service_name: str = Field(index=True)
    metadata_json: Optional[str] = Field(default=None) # Store extra info as JSON string
    is_anomaly: bool = Field(default=False)

class Alert(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    type: str
    severity: str
    message: str
    is_resolved: bool = Field(default=False)
    log_id: Optional[int] = Field(default=None, foreign_key="logentry.id")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
