from collections import defaultdict
from sqlalchemy.orm import Session
from .models import ClickEvent


def compute_analytics(db: Session, feature: str | None = None):
    query = db.query(ClickEvent)
    if feature:
        query = query.filter(ClickEvent.feature_name == feature)
    events = query.all()
    stats = defaultdict(lambda: {"total_clicks": 0, "users": set()})
    for e in events:
        s = stats[e.feature_name]
        s["total_clicks"] += 1
        s["users"].add(e.user_id)
    result = []
    for fname, s in stats.items():
        result.append({
            "feature_name": fname,
            "total_clicks": s["total_clicks"],
            "unique_users": len(s["users"])
        })
    result.sort(key=lambda i: i["total_clicks"], reverse=True)
    return result
