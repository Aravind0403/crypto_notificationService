# crypto_notificationService
## Create a Notification server which has the following end points --> REST API

## Features

- **Create Notifications**: Add a notification with Bitcoin price, percentage change, and trading volume.
- **List Notifications**: Retrieve all notifications with optional filters (status: `Pending`, `Sent`, `Failed`).

## Second Phase : TODO:
- **Update Notifications**: Modify notification details (e.g., update price or message).
- **Delete Notifications**: Soft delete a notification (mark it as deleted).

---

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Testing**: Pytest

---

## Installation and Setup

### Prerequisites
- Python 3.9+
- Pip (Python package manager)
