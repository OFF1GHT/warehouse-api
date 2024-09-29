from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def get(self, obj_id: int, session: AsyncSession):
        result = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalars().first()

    async def get_all(self, session: AsyncSession):
        result = await session.execute(select(self.model))
        return result.scalars().all()

    async def create(self, obj_in, session: AsyncSession):
        db_obj = self.model(**obj_in.dict())
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(self, obj_id: int, obj_in, session: AsyncSession):
        db_obj = await self.get(obj_id, session)
        if db_obj is None:
            return None
        for var, value in vars(obj_in).items():
            setattr(db_obj, var, value) if value is not None else None
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
        self,
        db_obj,
        session: AsyncSession,
    ):
        await session.delete(db_obj)
        await session.commit()
        return db_obj
