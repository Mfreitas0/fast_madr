from fastapi import FastAPI, HTTPException
from .model import UserModel


app = FastAPI()


@app.get("/")
def read_rot():
    return {"Hello": "Wold"}


@app.get("/users/")
def read_users():
    return {}


@app.post("/user/")
def create_user(user: UserModel):
    return {user.username, user.email, user.password}


@app.put("/user/{user_id}")
def update_user(user_id: int, user: UserModel):
    if not user_id:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"username": user.username, "email": user.email, "password": user.password}


@app.delete("/user/{user_id}")
def delete_user(user_id: int, user: UserModel):
    if not user_id:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"detail": "User deleted"}
