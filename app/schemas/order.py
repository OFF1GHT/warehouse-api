from pydantic import BaseModel
from enum import Enum
from typing import List
from app.schemas.order_item import OrderItemCreate, OrderItem
from datetime import datetime


class OrderStatus(str, Enum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"


class OrderBase(BaseModel):
    status: OrderStatus


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderUpdate(OrderBase):
    pass


class OrderDB(OrderBase):
    id: int
    created_at: datetime
    items: List[OrderItem]

    class Config:
        orm_mode = True
