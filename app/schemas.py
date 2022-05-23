from pydantic import  BaseModel


class Quote(BaseModel):
    quote: str
    author: str