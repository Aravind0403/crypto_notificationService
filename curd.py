from  app import models ,Schemas
from sqlalchemy.orm import Session
from typing import List , Optional



def create_notification(db:Session , notification: Schemas.NotificationCreate) -> models.Notification:
    db_notification = models.Notification(
    price = notification.price,
    percentage_change=notification.percentage_change,
    trading_volume = notification.trading_volume,
    message=notification.message,
    status= notification.status  or "Pending")
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification
def list_notifications(db:Session , status : Optional[str] = None) -> List[models.Notification]:
    query = db.query(models.Notification)
    if status:
        query = query.filter(models.Notification.status == status)
    return query.all()

## def update_notification

