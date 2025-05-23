from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import Session
from datetime import datetime
from .database import Base

class ClickEvent(Base):
    __tablename__ = "click_events"

    id = Column(Integer, primary_key=True, index=True)
    feature_name = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(String, index=True)
    x = Column(Float, nullable=True)
    y = Column(Float, nullable=True)

    @classmethod
    def from_create(cls, event: "ClickEventCreate"):
        return cls(
            feature_name=event.feature_name,
            timestamp=event.timestamp or datetime.utcnow(),
            user_id=event.user_id,
            x=event.x,
            y=event.y,
        )

class ClickEventCreate(BaseModel):
    feature_name: str
    timestamp: datetime | None = None
    user_id: str
    x: float | None = None
    y: float | None = None

class FeatureStats(BaseModel):
    feature_name: str
    total_clicks: int
    unique_users: int

