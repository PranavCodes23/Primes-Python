from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.dashboard import DashboardData
from app.models.domain import ZoneDataDB
from app.database import get_db

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["dashboard"],
)

@router.get("/zone-data", response_model=DashboardData)
@router.post("/zone-data", response_model=DashboardData)
def get_zone_data(date: str = None, payload: dict = None, db: Session = Depends(get_db)):
    # Support both GET with query param and POST with JSON body (like Next.js did)
    target_date_str = date
    if payload and "date" in payload:
        target_date_str = payload["date"]
    
    if not target_date_str:
        # Default to some date or return empty
        return DashboardData(currData=[], previousYData=[])

    try:
        # Assuming target_date_str is YYYY-MM-DD
        # The database stores exactly Midnight UTC, so we query based on that exact date object
        query_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        
        # Query Prisma's timezone format
        # Alternatively, we can cast to DATE in mysql, but direct match is faster
        results = db.query(ZoneDataDB).filter(ZoneDataDB.date == query_date).all()
        
        # Map to Pydantic model
        curr_data = []
        for r in results:
            curr_data.append({
                "booking_loc": r.booking_loc,
                "tktbkd": r.tktbkd,
                "tktcan": r.tktcan,
                "psgnbkg": r.psgnbkg,
                "psgncanc": r.psgncanc,
                "earning": r.earning,
                "refund": r.refund,
                "net": r.net,
                "loadingtime": str(r.loadingtime) if r.loadingtime else ""
            })
            
        return {"currData": curr_data, "previousYData": []}
    except Exception as e:
        print(f"Error querying db: {e}")
        return DashboardData(currData=[], previousYData=[])

@router.post("/stats-data")
def get_stats_data(payload: dict = None, db: Session = Depends(get_db)):
    try:
        start_date = datetime.strptime("2025-01-01", "%Y-%m-%d")
        end_date = datetime.strptime("2025-01-15", "%Y-%m-%d")
        
        results = db.query(ZoneDataDB).filter(
            ZoneDataDB.booking_loc == 'ALL',
            ZoneDataDB.date >= start_date,
            ZoneDataDB.date <= end_date
        ).order_by(ZoneDataDB.date.asc()).all()
        
        stats_data = []
        for r in results:
            stats_data.append({
                "date": r.date.isoformat(),
                "tktbkd": r.tktbkd,
                "tktcan": r.tktcan,
                "psgnbkg": r.psgnbkg,
                "psgncanc": r.psgncanc,
                "earning": r.earning,
                "refund": r.refund,
                "net": r.net
            })
            
        return {"statsData": stats_data}
    except Exception as e:
        print(f"Error querying stats db: {e}")
        return {"statsData": []}

