from pydantic import BaseModel
from typing import List, Optional

class ZoneData(BaseModel):
    booking_loc: str
    tktbkd: Optional[int] = 0
    tktcan: Optional[int] = 0
    psgnbkg: Optional[int] = 0
    psgncanc: Optional[int] = 0
    earning: Optional[float] = 0.0
    refund: Optional[float] = 0.0
    net: Optional[float] = 0.0
    loadingtime: Optional[str] = ""

class DashboardData(BaseModel):
    currData: List[ZoneData]
    previousYData: List[ZoneData]
