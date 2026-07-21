from fastapi import APIRouter
from app.models.dashboard import DashboardData, ZoneData

router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["dashboard"],
)

@router.get("/zone-data", response_model=DashboardData)
def get_zone_data():
    curr_data = [
        ZoneData(booking_loc="CR", tktbkd=1000, psgnbkg=2000, earning=50000, refund=1000, can_tktbkd=50, can_psgnbkg=100),
        ZoneData(booking_loc="EC", tktbkd=1200, psgnbkg=2400, earning=60000, refund=1200, can_tktbkd=60, can_psgnbkg=120),
        ZoneData(booking_loc="EO", tktbkd=800, psgnbkg=1600, earning=40000, refund=800, can_tktbkd=40, can_psgnbkg=80),
        ZoneData(booking_loc="ER", tktbkd=1500, psgnbkg=3000, earning=75000, refund=1500, can_tktbkd=75, can_psgnbkg=150),
        ZoneData(booking_loc="KR", tktbkd=500, psgnbkg=1000, earning=25000, refund=500, can_tktbkd=25, can_psgnbkg=50),
        ZoneData(booking_loc="NC", tktbkd=900, psgnbkg=1800, earning=45000, refund=900, can_tktbkd=45, can_psgnbkg=90),
        ZoneData(booking_loc="NE", tktbkd=1100, psgnbkg=2200, earning=55000, refund=1100, can_tktbkd=55, can_psgnbkg=110),
        ZoneData(booking_loc="NF", tktbkd=1300, psgnbkg=2600, earning=65000, refund=1300, can_tktbkd=65, can_psgnbkg=130),
        ZoneData(booking_loc="NR", tktbkd=1600, psgnbkg=3200, earning=80000, refund=1600, can_tktbkd=80, can_psgnbkg=160),
        ZoneData(booking_loc="NW", tktbkd=700, psgnbkg=1400, earning=35000, refund=700, can_tktbkd=35, can_psgnbkg=70),
        ZoneData(booking_loc="SB", tktbkd=600, psgnbkg=1200, earning=30000, refund=600, can_tktbkd=30, can_psgnbkg=60),
        ZoneData(booking_loc="SC", tktbkd=1400, psgnbkg=2800, earning=70000, refund=1400, can_tktbkd=70, can_psgnbkg=140),
        ZoneData(booking_loc="SE", tktbkd=850, psgnbkg=1700, earning=42500, refund=850, can_tktbkd=42, can_psgnbkg=85),
        ZoneData(booking_loc="SO", tktbkd=950, psgnbkg=1900, earning=47500, refund=950, can_tktbkd=47, can_psgnbkg=95),
        ZoneData(booking_loc="SR", tktbkd=1700, psgnbkg=3400, earning=85000, refund=1700, can_tktbkd=85, can_psgnbkg=170),
        ZoneData(booking_loc="SW", tktbkd=1050, psgnbkg=2100, earning=52500, refund=1050, can_tktbkd=52, can_psgnbkg=105),
        ZoneData(booking_loc="WC", tktbkd=650, psgnbkg=1300, earning=32500, refund=650, can_tktbkd=32, can_psgnbkg=65),
        ZoneData(booking_loc="WR", tktbkd=1550, psgnbkg=3100, earning=77500, refund=1550, can_tktbkd=77, can_psgnbkg=155),
    ]

    prev_data = [
        ZoneData(booking_loc="CR", tktbkd=900, psgnbkg=1800, earning=45000, refund=900, can_tktbkd=45, can_psgnbkg=90),
        ZoneData(booking_loc="EC", tktbkd=1100, psgnbkg=2200, earning=55000, refund=1100, can_tktbkd=55, can_psgnbkg=110),
        ZoneData(booking_loc="EO", tktbkd=700, psgnbkg=1400, earning=35000, refund=700, can_tktbkd=35, can_psgnbkg=70),
        ZoneData(booking_loc="ER", tktbkd=1400, psgnbkg=2800, earning=70000, refund=1400, can_tktbkd=70, can_psgnbkg=140),
        ZoneData(booking_loc="KR", tktbkd=400, psgnbkg=800, earning=20000, refund=400, can_tktbkd=20, can_psgnbkg=40),
        ZoneData(booking_loc="NC", tktbkd=800, psgnbkg=1600, earning=40000, refund=800, can_tktbkd=40, can_psgnbkg=80),
        ZoneData(booking_loc="NE", tktbkd=1000, psgnbkg=2000, earning=50000, refund=1000, can_tktbkd=50, can_psgnbkg=100),
        ZoneData(booking_loc="NF", tktbkd=1200, psgnbkg=2400, earning=60000, refund=1200, can_tktbkd=60, can_psgnbkg=120),
        ZoneData(booking_loc="NR", tktbkd=1500, psgnbkg=3000, earning=75000, refund=1500, can_tktbkd=75, can_psgnbkg=150),
        ZoneData(booking_loc="NW", tktbkd=600, psgnbkg=1200, earning=30000, refund=600, can_tktbkd=30, can_psgnbkg=60),
        ZoneData(booking_loc="SB", tktbkd=500, psgnbkg=1000, earning=25000, refund=500, can_tktbkd=25, can_psgnbkg=50),
        ZoneData(booking_loc="SC", tktbkd=1300, psgnbkg=2600, earning=65000, refund=1300, can_tktbkd=65, can_psgnbkg=130),
        ZoneData(booking_loc="SE", tktbkd=750, psgnbkg=1500, earning=37500, refund=750, can_tktbkd=37, can_psgnbkg=75),
        ZoneData(booking_loc="SO", tktbkd=850, psgnbkg=1700, earning=42500, refund=850, can_tktbkd=42, can_psgnbkg=85),
        ZoneData(booking_loc="SR", tktbkd=1600, psgnbkg=3200, earning=80000, refund=1600, can_tktbkd=80, can_psgnbkg=160),
        ZoneData(booking_loc="SW", tktbkd=950, psgnbkg=1900, earning=47500, refund=950, can_tktbkd=47, can_psgnbkg=95),
        ZoneData(booking_loc="WC", tktbkd=550, psgnbkg=1100, earning=27500, refund=550, can_tktbkd=27, can_psgnbkg=55),
        ZoneData(booking_loc="WR", tktbkd=1450, psgnbkg=2900, earning=72500, refund=1450, can_tktbkd=72, can_psgnbkg=145),
    ]

    return DashboardData(currData=curr_data, previousYData=prev_data)
