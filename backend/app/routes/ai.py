# app/routes/ai.py
from fastapi import APIRouter, HTTPException
from app.services.analytics import build_location_summary
from app.services.ai_service import generate_location_recommendation
from app.state import collisions_df

router = APIRouter(prefix="/ai", tags=["ai"])

@router.get("/recommendation/{geo_id}")
def get_ai_recommendation(geo_id: str):
    summary = build_location_summary(collisions_df, geo_id)

    if not summary:
        raise HTTPException(status_code=404, detail="Zone introuvable")

    result = generate_location_recommendation(summary)

    return {
        "geo_id": geo_id,
        "location": summary.get("location"),
        "data_summary": summary,
        "ai_analysis": result
    }