from pydantic import BaseModel
from typing import List

class ZoneData(BaseModel):
    booking_loc: str
    tktbkd: int
    psgnbkg: int
    earning: int
    refund: int
    can_tktbkd: int
    can_psgnbkg: int

class DashboardData(BaseModel):
    currData: List[ZoneData]
    previousYData: List[ZoneData]
