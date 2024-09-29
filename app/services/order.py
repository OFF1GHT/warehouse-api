from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product import Product
from app.crud.order import order_crud
from app.schemas.order import OrderCreate
from app.schemas.order_item import OrderItemCreate
from typing import List


class OrderService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _validate_product_availability(
        self, items: List[OrderItemCreate]
    ) -> None:
        """Проверка наличия достаточного количества товара на складе."""
        for item in items:
            product = await self.session.get(Product, item.product_id)

            if not product:
                raise HTTPException(
                    status_code=404, detail=f"Товар с ID {item.product_id} не найден."
                )

            if product.stock < item.quantity:
                raise HTTPException(
                    status_code=400,
                    detail=f"Недостаточно товара {product.name} на складе.",
                )

    async def create_order(self, order_in: OrderCreate) -> Order:
        await self._validate_product_availability(order_in.items)

        order = Order()
        self.session.add(order)
        await self.session.flush()

        for item in order_in.items:
            product = await self.session.get(Product, item.product_id)
            order_item = OrderItem(
                order_id=order.id, product_id=product.id, quantity=item.quantity
            )
            self.session.add(order_item)
            product.stock -= item.quantity

        await self.session.commit()
        await self.session.refresh(order)
        return order

    async def update_order_status(self, order_id: int, new_status: str):
        """Обновление статуса заказа"""
        order = await order_crud.get_order_by_id(order_id, self.session)
        if not order:
            return None
        order.status = new_status
        self.session.add(order)
        await self.session.commit()
        await self.session.refresh(order)
        return order
