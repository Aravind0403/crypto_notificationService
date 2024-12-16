## database Models how the API interacts with it

from sqlalchemy import Column, Integer, String , Float , DateTime , enum
from sqlalchemy.ext.declarative import  declarative_base
from datetime import datetime
from enum import EnumMeta


Base = declarative_base()

class NotificationStatus(str,enum.Enum):
    pending = "Pending"
    sent = "Sent"
    failed = "Failed"

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer,primary_key = True , index = True)
    price = Column(Float,nullable=False)
    percentage_change = Column(Float,nullable = False)
    message = Column(String , nullable=False)
    status = Column(EnumMeta(NotificationStatus), default=NotificationStatus.pending)
    created_at = Column(DateTime,default=datetime.utcnow())
    updated_at = Column(DateTime,default=datetime.utcnow(),onupdate= datetime.utcnow())

