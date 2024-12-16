from pydantic import BaseModel
from datetime import  datetime
from typing import Optional

class NotificationBase(BaseModel):
    price : float
    percentage_change: float
    trading_volume : float
    message:str
class NotificationCreate(NotificationBase):
    status: Optional [str] = None
    pass
class NotificationUpdate(BaseModel):
    price: Optional [float] = None
    percentage_change: Optional [float] = None
    trading_volume: Optional [float] = None
    message: Optional [str] = None

class Notification(NotificationBase):
    id:int
    status : str
    created_at: datetime
    updated_at : datetime

    class config:
        orm_mode = True
