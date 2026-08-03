from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base
from datetime import datetime

class ZoneDataDB(Base):
    __tablename__ = "ZoneData"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    booking_loc = Column(String(50))
    tktbkd = Column(Integer, default=0)
    tktcan = Column(Integer, default=0)
    psgnbkg = Column(Integer, default=0)
    psgncanc = Column(Integer, default=0)
    earning = Column(Float, default=0.0)
    refund = Column(Float, default=0.0)
    net = Column(Float, default=0.0)
    loadingtime = Column(String(255))
