from fastapi import APIRouter, Response , HTTPException , status
from app import utils ,database, schemas
from typing import Optional

router = APIRouter(
    prefix="/quotes"
)

@router.get("/random")
def get_random_quote():
    quotes_count = database.count_quotes()    #getting total quotes in the databse
    quote_id = utils.random_number(1, quotes_count+1)  #getting a random quote number
    quote = database.get_quote(quote_id)  # gettting a quote with a specified random quote number

    #TODO: validate response using a pydantic model
    return { 
        "quote": quote['quote'],
        "author": quote['author']
    }

@router.get("/author_id={author_id}")
def get_author_quotes( author_id: str, limit:Optional[str]=None):
    if limit != None:
        if utils.to_integer(limit) == None:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="invalid limit number")
    
    #TODO: validate response with a pydantic model
    return  database.get_author_quotes(author_id, limit)