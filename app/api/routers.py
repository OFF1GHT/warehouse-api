from fastapi import APIRouter
from app.api.endpoints import product_router, order_router

main_router = APIRouter()
main_router.include_router(
    product_router,
    prefix="/product",
    tags=["products"],
)
main_router.include_router(
    order_router,
    prefix="/order",
    tags=["orders"],
)
