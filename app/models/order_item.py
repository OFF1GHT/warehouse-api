from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.db import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(
        Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False
    )
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    # Связи
    order = relationship("Order", back_populates="items")
    product = relationship("Product")

    def __repr__(self):
        return (
            f"<OrderItem(order_id={self.order_id}, "
            f"product_id={self.product_id}, quantity={self.quantity})>"
        )
