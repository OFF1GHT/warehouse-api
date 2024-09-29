from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.order import OrderCreate, OrderDB, OrderUpdate
from app.services.order import OrderService
from app.core.db import get_async_session
from app.crud.order import order_crud

router = APIRouter()


# Эндпоинт для создания заказа
@router.post("/orders", response_model=OrderDB)
async def create_order(
    order_in: OrderCreate, session: AsyncSession = Depends(get_async_session)
):
    order_service = OrderService(session)
    order = await order_service.create_order(order_in)
    return order


# Эндпоинт для получения списка заказов
@router.get("/orders", response_model=List[OrderDB])
async def get_orders(session: AsyncSession = Depends(get_async_session)):
    orders = await order_crud.get_all(session)
    return orders


# Эндпоинт для получения информации о заказе по ID
@router.get("/orders/{order_id}", response_model=OrderDB)
async def get_order_by_id(
    order_id: int, session: AsyncSession = Depends(get_async_session)
):
    order = await order_crud.get_order_by_id(session, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order


# Эндпоинт для обновления статуса заказа
@router.patch("/orders/{order_id}/status", response_model=OrderDB)
async def update_order_status(
    order_id: int,
    order_status: OrderUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    order_service = OrderService(session)
    updated_order = await order_service.update_order_status(
        order_id, order_status.status
    )
    if not updated_order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return updated_order
