from pydantic import BaseModel


class Order(BaseModel):
    order_id: int
    item_id: int
    quantity: int
    user_id: int
