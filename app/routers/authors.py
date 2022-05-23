from fastapi import APIRouter
from app import database

router = APIRouter(
    prefix="/authors"
)

@router.get("/")
def get_all_authors():

    return database.get_authors()