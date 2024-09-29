from app.models.product import Product
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.base import CRUDBase
from typing import Optional
from sqlalchemy import select


class CRUDProduct(CRUDBase):
    async def get_product_by_id(
        self, product_id: int, session: AsyncSession
    ) -> Optional[Product]:
        result = await session.execute(select(Product).where(Product.id == product_id))
        return result.scalars().first()

    async def get_product_by_name(
        self,
        product_name: str,
        session: AsyncSession,
    ) -> Optional[Product]:
        result = await session.execute(
            select(Product).where(Product.name == product_name)
        )
        return result.scalars().first()


product_crud = CRUDProduct(Product)
