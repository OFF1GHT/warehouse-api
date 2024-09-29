from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.product import ProductCreate, ProductUpdate, ProductDB
from app.services.product import ProductService
from app.core.db import get_async_session
from app.crud.product import product_crud

router = APIRouter()


# Эндпоинт для создания товара
@router.post("/products", response_model=ProductDB)
async def create_product(
    product_in: ProductCreate, session: AsyncSession = Depends(get_async_session)
):
    product_service = ProductService(session)
    product = await product_service.create_product(product_in)
    return product


# Эндпоинт для получения списка товаров
@router.get("/products", response_model=List[ProductDB])
async def get_products(session: AsyncSession = Depends(get_async_session)):
    products = await product_crud.get_all(session)
    return products


# Эндпоинт для получения информации о товаре по ID
@router.get("/products/{product_id}", response_model=ProductDB)
async def get_product_by_id(
    product_id: int, session: AsyncSession = Depends(get_async_session)
):
    product = await product_crud.get_product_by_id(product_id, session)
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    return product


# Эндпоинт для обновления информации о товаре
@router.put("/products/{product_id}", response_model=ProductDB)
async def update_product(
    product_id: int,
    product_in: ProductUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    product_service = ProductService(session)
    updated_product = await product_service.update_product(product_id, product_in)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Невозможно обновить товар")
    return updated_product


# Эндпоинт для удаления товара
@router.delete("/products/{product_id}", response_model=ProductDB)
async def delete_product(
    product_id: int, session: AsyncSession = Depends(get_async_session)
):
    # Получаем продукт по ID
    product = await product_crud.get_product_by_id(product_id, session)

    # Проверяем, что продукт найден
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")

    # Удаляем продукт, передавая объект продукта, а не его ID
    await product_crud.remove(product, session)
    return product
