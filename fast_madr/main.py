from fastapi import FastAPI
from fast_madr.routers import users


app = FastAPI()
app.include_router(users.router)


@app.get("/")
def read_rot():
    return {"Hello": "Wold"}
