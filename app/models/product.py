from sqlalchemy import Column, Integer, Float, String

from app.core.db import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, stock={self.stock})>"
