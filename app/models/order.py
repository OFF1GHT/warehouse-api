from sqlalchemy import Column, Integer, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum as PyEnum
from app.core.db import Base


class OrderStatus(PyEnum):
    pending = "pending"
    shipped = "shipped"
    delivered = "delivered"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)  # Статус заказа

    # Связь с элементами заказа
    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    def __repr__(self):
        return (
            f"<Order(id={self.id}, status={self.status}, created_at={self.created_at})>"
        )
