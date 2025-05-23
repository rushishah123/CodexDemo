from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import models, analytics, insights

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Feature Analytics API")

@app.post("/api/clicks")
def create_click(event: models.ClickEventCreate, db: Session = Depends(get_db)):
    db_event = models.ClickEvent.from_create(event)
    db.add(db_event)
    db.commit()
    return {"status": "ok"}

@app.get("/api/analytics")
def get_analytics(feature: str | None = None, db: Session = Depends(get_db)):
    return analytics.compute_analytics(db, feature)

@app.get("/api/insights")
def get_insights(feature: str | None = None, db: Session = Depends(get_db)):
    stats = analytics.compute_analytics(db, feature)
    return {"insight": insights.generate_insight(stats)}
