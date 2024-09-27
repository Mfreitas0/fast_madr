from fastapi import FastAPI
from fast_madr.routers import users, books


app = FastAPI()
app.include_router(users.router)
app.include_router(books.router)


@app.get("/")
def read_rot():
    return {"Hello": "Wold"}
