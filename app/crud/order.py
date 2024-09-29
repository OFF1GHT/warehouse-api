from app.models.order import Order
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base import CRUDBase
from typing import Optional
from sqlalchemy import select


class CRUDOrder(CRUDBase):
    async def get_order_by_id(
        self, order_id: int, session: AsyncSession
    ) -> Optional[Order]:
        result = await session.execute(select(Order).where(Order.id == order_id))
        return result.scalars().first()


order_crud = CRUDOrder(Order)
