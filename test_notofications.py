from starlette.testclient import TestClient
from app.main import app
from app.models import  Base
from app.database import Session_local , engine


Base.metdata.create_all(bind=engine)


client =TestClient(app)

def test_db():
        db =Session_local()
        try:
            yield db
        finally:
            db.close()

def test_create_notifications():
    payload = {
        "price ":30000.50,
        "percentage_change" :15.35,
        "trading_volume" :1200.35,
        "message": "Bitcoin Prices has Increased hurray !!",
    }
    response = client.post("/notifications",json=payload)
    assert response.status.code == 200
    data = response.json
    assert data["price"] == payload["price"]
    assert data["percentage_change"] == payload["percentage_change"]
    assert data["trading_volume"] == payload["trading_volume"]
    assert data["message"] == payload["message"]
    assert  data["status"] == "Pending"
def test_list_notifications():
    response = client.get("/notifications")
    assert response.status_code ==200
    data = response.json()
    assert isinstance(data,list)
    assert len(data) > 0