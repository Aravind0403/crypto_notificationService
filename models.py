## database Models how the API interacts with it
import enum

from sqlalchemy import Column, Integer, String , Float , DateTime , Enum
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import  declarative_base
from datetime import datetime


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
    status = Column(Enum(NotificationStatus), default=NotificationStatus.pending)
    created_at = Column(DateTime,default=datetime.utcnow())
    updated_at = Column(DateTime,default=datetime.utcnow(),onupdate= datetime.utcnow())

