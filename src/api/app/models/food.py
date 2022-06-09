from pydantic import BaseModel


class Food(BaseModel):
    _id: str
    name: str
    origination: str
    created: str
    date: str
