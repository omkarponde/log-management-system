from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    user_id: int
