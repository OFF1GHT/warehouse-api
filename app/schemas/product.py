from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductDB(ProductBase):
    id: int

    class Config:
        orm_mode = True
