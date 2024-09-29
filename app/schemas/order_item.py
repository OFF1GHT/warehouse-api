from pydantic import BaseModel, Field


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True
