"""Simple heuristic-based insights placeholder."""

from typing import List, Dict


def generate_insight(stats: List[Dict]):
    if not stats:
        return "No usage data available."
    top = stats[0]
    bottom = stats[-1] if len(stats) > 1 else stats[0]
    return (
        f"Top feature '{top['feature_name']}' has {top['total_clicks']} clicks. "
        f"Least used feature '{bottom['feature_name']}' has {bottom['total_clicks']} clicks."
    )
