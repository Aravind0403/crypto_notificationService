## App Main .py
from http.client import responses

from fastapi import FastAPI, HTTPException
from fastapi.params import Depends

from  app import Schemas , curd, database
from  sqlalchemy.orm import Session

from typing import List , Optional

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


## Create
@app.post("/notifications", response_model=Schemas.Notification)
def create_notification(notifications: Schemas.NotificationCreate , db : Session = Depends(get_db)):
    return curd.create_notification(db=db, notification=notifications)

    ## Status0
@app.get("/notifications", response_model= List[Schemas.Notification])
def list_notifications(status: Optional[str] = None, db: Session = Depends(get_db)):
    return curd.list_notifications(db=db, status=status)

## Update
##
##@app.put("/notifications/{id}")
##def update_notification()

