from fastapi import HTTPException
from app.models.product import Product
from app.crud.product import product_crud
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, session):
        self.session = session

    async def _check_name_duplicate(self, product_name: str) -> None:
        product = await product_crud.get_product_by_name(product_name, self.session)
        if product is not None:
            raise HTTPException(
                status_code=400, detail="Продукт с таким именем уже существует!"
            )

    async def create_product(self, product: ProductCreate):
        await self._check_name_duplicate(product.name)
        new_product = await product_crud.create(product, self.session)
        return new_product

    async def update_product(self, product: Product, obj_in: ProductUpdate):
        if obj_in.name:
            await self._check_name_duplicate(obj_in.name)
        product = await product_crud.update(product, obj_in, self.session)
        return product
