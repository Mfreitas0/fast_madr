from fastapi import APIRouter


router = APIRouter()


@router.get("/books/", tags=["books"])
def read_books():
    return {"detail": "Paciencia moreno."}
