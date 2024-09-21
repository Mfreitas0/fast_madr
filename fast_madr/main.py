from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .database import User, get_db
from .model import UserModel


app = FastAPI()


@app.get("/")
def read_rot():
    return {"Hello": "Wold"}


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    q = db.query(User).order_by(User.id).all()
    return q


@app.post("/user/")
def create_user(user: UserModel, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter((User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists.")
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"username": user.username, "emal": user.email, "password": user.password}


@app.put("/user/{user_id}")
def update_user(user_id: int, user: UserModel, db: Session = Depends(get_db)):
    up_user = db.get(User, user_id)
    if not up_user:
        raise HTTPException(status_code=404, detail="User not found.")
    else:
        up_user.username = user.username
        up_user.email = user.email
        up_user.password = user.password
    db.commit()
    db.refresh(up_user)

    return {
        "id": user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password,
    }


@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    existing_user = db.get(User, user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found.")
    db.delete(existing_user)
    db.commit()
    return {"detail": "User deleted"}
